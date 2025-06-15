import requests
import streamlit as st

from style.custom_css import apply_custom_style

apply_custom_style()

from utils.sidebar import display_logo_in_sidebar

display_logo_in_sidebar()

# --- Config ---
SAFE_API = "http://localhost:8081"
USER_ID = "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb"  # Bob

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
sent = [tx for tx in pending_transactions if tx.get("user_source_id") == USER_ID]
received = [tx for tx in pending_transactions if tx.get("user_dest_id") == USER_ID]

# --- Section 1 : Envoyeur ---
st.subheader("Virements envoyés en attente")
if not sent:
    st.info("Aucun virement en attente en tant qu'émetteur.")
else:
    for tx in sent:
        st.markdown(f"""
        **Montant :** {tx['amount']:.2f} €  
        **Destinataire :** {tx['counterparty_name']}  
        **Statut :** {tx['status']}
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
        **Émetteur :** {tx['counterparty_name']}  
        """)
        code_input = st.text_input(
            label=f"Code de validation pour transaction {tx['safe_transaction_id'][:8]}...",
            key=f"code_{tx['safe_transaction_id']}"
        )
        if st.button(f"Valider transaction {tx['safe_transaction_id'][:8]}", key=f"btn_{tx['safe_transaction_id']}"):
            try:
                r2 = requests.post(
                    f"{SAFE_API}/transactions/beneficiary-validation",
                    params={
                        "transaction_id": tx["safe_transaction_id"],
                        "code": code_input
                    }
                )
                r2.raise_for_status()
                st.success("Virement validé avec succès.")
            except Exception as e:
                st.error(f"Erreur lors de la validation : {e}")
        st.markdown("---")
