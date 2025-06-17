import requests
import streamlit as st
from style.custom_css import apply_custom_style
from utils.sidebar import display_logo_in_sidebar

apply_custom_style()
display_logo_in_sidebar()

# --- Configuration ---
BASE_API_URL = "http://localhost:8080"
USER_ID = "11111111-1111-1111-1111-111111111111"
ACCOUNT_ID = "aaaaaaa1-aaaa-aaaa-aaaa-aaaaaaaaaaaa"

# --- Libellés personnalisés ---
type_labels = {
    "CLASSIC_VIREMENT": "Virement classique",
    "SAFETRANSFER_VIREMENT": "Virement sécurisé",
    "SAFETRANSFER_PRELEVEMENT": "Prélèvement sécurisé",
    "CLASSIC_PRELEVEMENT": "Prélèvement",
    "CB": "Carte bancaire",
    "CHEQUE": "Chèque"
}

status_labels = {
    "PENDING_USER": "En attente utilisateur",
    "PENDING_FRAUD_CHECK": "Contrôle anti-fraude",
    "PENDING_RECIPIENT": "En attente destinataire",
    "VALIDATED": "Effectué",
    "REFUSED": "Refusé"
}


# --- API Calls ---
def get_user(user_id):
    try:
        return requests.get(f"{BASE_API_URL}/users/{user_id}").json()
    except:
        return {"name": "Inconnu", "email": "", "iban": "", "bic": ""}


def get_account(account_id):
    try:
        return requests.get(f"{BASE_API_URL}/accounts/{account_id}").json()
    except:
        return {"balance": 0.0, "name": "Compte inconnu"}


def get_transactions(account_id):
    try:
        return requests.get(f"{BASE_API_URL}/transactions/by-account/{account_id}").json()
    except:
        return []


# --- Données ---
user = get_user(USER_ID)
account = get_account(ACCOUNT_ID)
transactions = get_transactions(ACCOUNT_ID)

# --- Titre principal ---
st.title(f"Compte de {user['name']}")

# --- Boutons actions haut de page ---
col1, col2 = st.columns(2)
with col1:
    st.button("Virement classique")
with col2:
    if st.button("Virement SafeTransfer"):
        st.switch_page("pages/2_Virement_SafeTransfert.py")

# --- Solde ---
st.subheader("Solde du compte")
st.markdown(
    f"<div style='font-size: 32px; font-weight: bold;'>{account['balance']:.2f} €</div>",
    unsafe_allow_html=True
)

# --- Historique des transactions ---
st.subheader("Historique des transactions")

filtre = st.radio("Filtre", ["Tous", "Virements", "Prélèvements"], horizontal=True, label_visibility="collapsed")

# Mapping filtres
type_map = {
    "Virements": ["CLASSIC_VIREMENT", "SAFETRANSFER_VIREMENT"],
    "Prélèvements": ["CLASSIC_PRELEVEMENT", "SAFETRANSFER_PRELEVEMENT"]
}

# Application du filtre
filtered = [
    tx for tx in transactions
    if filtre == "Tous" or tx.get("transaction_type") in type_map[filtre]
]

# Affichage
if not filtered:
    st.info("Aucune transaction trouvée.")
else:
    for tx in filtered:
        montant = tx["amount"]
        signe = "+" if montant > 0 else "-"
        couleur = "green" if montant > 0 else "red"
        type_label = type_labels.get(tx["transaction_type"], tx["transaction_type"])
        statut = status_labels.get(tx["status"], tx["status"])

        st.markdown(
            f"""
            <div style='padding: 6px 0; border-bottom: 1px solid #eee;'>
                <strong>{type_label}</strong><br>
                Contrepartie : {tx['counterparty_name']}<br>
                <span style='color:{couleur}; font-weight:bold;'>{signe}{abs(montant):.2f} €</span>
                <span style='float:right;'>{statut}</span><br>
                Date : {tx['transaction_date'][:10]}
            </div>
            """,
            unsafe_allow_html=True
        )
