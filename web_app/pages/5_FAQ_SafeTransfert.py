import uuid

import requests
import streamlit as st
from style.custom_css import apply_custom_style_sidebar
from utils.sidebar import display_logo_in_sidebar

apply_custom_style_sidebar()

st.markdown("""
    <style>
    /* Cacher la barre automatique entre la navigation et le contenu personnalisé */
    [data-testid="stSidebarNavSeparator"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

BASE_API_URL = "http://localhost:8081"

# --- Initialiser la session ---
if "faq_session_id" not in st.session_state:
    st.session_state["faq_session_id"] = None
    st.session_state["messages"] = []


# --- Fonction pour récupérer l'historique ---
def get_conversation_history(session_id):
    try:
        r = requests.get(f"{BASE_API_URL}/chat-ia/history/{session_id}")
        r.raise_for_status()
        data = r.json()
        interactions = data.get("interactions", [])
        history = []
        for interaction in interactions:
            history.append({"role": "user", "message": interaction.get("prompt", "")})
            history.append({"role": "assistant", "message": interaction.get("response", "")})
        return history
    except Exception as e:
        st.error(f"Erreur lors de la récupération de l'historique : {e}")
        return []


# --- Fonction pour envoyer une question ---
def send_question(prompt):
    try:
        payload = {"prompt": prompt}
        if st.session_state["faq_session_id"]:
            payload["session_id"] = st.session_state["faq_session_id"]

        r = requests.post(f"{BASE_API_URL}/chat-ia/ask", json=payload)
        r.raise_for_status()
        data = r.json()

        # Mise à jour du session_id
        st.session_state["faq_session_id"] = data.get("session_id")

        interactions = data.get("interactions", [])
        if interactions:
            return interactions[-1].get("response", "Pas de réponse.")
        else:
            return "Aucune réponse."
    except Exception as e:
        st.error(f"Erreur lors de l'envoi de la question : {e}")
        return "Erreur côté serveur."


# --- Contenu principal ---
st.title("FAQ - Assistance IA SafeTransfer")
st.caption("Posez vos questions sur le fonctionnement du système SafeTransfer")

# --- Contenu de la sidebar personnalisé (ajouté sous la navigation automatique) ---
with st.sidebar:
    if st.button("Nouvelle conversation"):
        st.session_state["faq_session_id"] = str(uuid.uuid4())
        st.session_state["messages"] = []
    st.markdown("---")
    display_logo_in_sidebar()

# --- Affichage de l'historique au premier chargement ---
if st.session_state["faq_session_id"] is not None and not st.session_state["messages"]:
    history = get_conversation_history(st.session_state["faq_session_id"])
    st.session_state["messages"] = history if history else []

# --- Affichage des messages (une seule fois) ---
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["message"])

# --- Zone de saisie utilisateur ---
if prompt := st.chat_input("Posez votre question ici..."):
    st.chat_message("user").write(prompt)
    st.session_state["messages"].append({"role": "user", "message": prompt})

    response = send_question(prompt)
    st.chat_message("assistant").write(response)
    st.session_state["messages"].append({"role": "assistant", "message": response})
