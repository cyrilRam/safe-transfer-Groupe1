import requests
import streamlit as st
from style.custom_css import apply_custom_style
from utils.sidebar import display_logo_in_sidebar

apply_custom_style()
display_logo_in_sidebar()

# --- Config ---
SAFE_API = "http://localhost:8081"
USER_ID = "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb"

st.markdown(f"## Compte de Bod Martin")

st.title("Virements SafeTransfer en attente de validation")

# --- Récupération des transactions en attente ---
try:
    r = requests.get(f"{SAFE_API}/transactions/pending/{USER_ID}")
    r.raise_for_status()
    pending_transactions = r.json()
except Exception as e:
    st.error(f"Erreur lors de la récupération des virements en attente de validation : {e}")
    pending_transactions = []

# --- Séparation des transactions envoyées / reçues ---
sent = [
    tx for tx in pending_transactions if tx.get("status") == "PENDING_USER"]
received = [
    tx for tx in pending_transactions if tx.get("status") == "PENDING_RECIPIENT"]

# --- Section 1 : Envoyeur ---
st.subheader("Virements envoyés en attente")
if not sent:
    st.info("Aucun virement en attente en tant qu'émetteur.")
else:
    for tx in sent:
        st.markdown(f"""
        **Montant :** {tx['amount']:.2f} €  
        **Destinataire :** {tx["user_beneficiary"]["name"]}  
        **Date :** {tx['transaction_date'][:10]}
        ---
        """)

# --- Section 2 : Bénéficiaire ---
st.subheader("Virements reçus en attente de validation")
if not received:
    st.info("Aucun virement à valider en tant que bénéficiaire.")
else:
    for tx in received:
        st.markdown(f"""
        **Montant :** {tx['amount']:.2f} €  
        **Émetteur :** {tx["user_sender"]["name"]}  
        **Date :** {tx['transaction_date'][:10]}
        """)

        code_input = st.text_input(
            label=f"Code de validation pour la transaction",
            key=f"code_{tx['id']}"
        )

        if st.button(f"Valider la transaction", key=f"btn_{tx['id']}"):
            try:
                r2 = requests.post(
                    f"{SAFE_API}/transactions/beneficiary-validation",
                    params={
                        "transaction_id": tx["id"],
                        "code": code_input
                    }
                )
                r2.raise_for_status()
                st.success("Virement validé avec succès.")
            except Exception as e:
                st.error(f"Erreur lors de la validation : {e}")

        st.markdown("---")
