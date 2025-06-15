import requests
import streamlit as st
from style.custom_css import apply_custom_style

apply_custom_style()

from utils.sidebar import display_logo_in_sidebar

display_logo_in_sidebar()

# Styles spécifiques à cette page uniquement
st.markdown("""
    <style>
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        background-color: #198754 !important;  /* Vert Valider */
        color: white !important;
        transition: opacity 0.2s ease-in-out;
    }

    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button:hover {
        opacity: 0.85;
    }

    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background-color: #dc3545 !important;  /* Rouge Annuler */
        color: white !important;
        transition: opacity 0.2s ease-in-out;
    }

    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button:hover {
        opacity: 0.85;
    }
    </style>
""", unsafe_allow_html=True)

SAFE_API = "http://localhost:8081"

st.title("Opérations frauduleuses détectées")

# --- Récupération des opérations frauduleuses ---
try:
    r = requests.get(f"{SAFE_API}/frauds")
    r.raise_for_status()
    transactions = r.json()
except Exception as e:
    st.warning("Impossible de récupérer les fraudes. Données mock affichées.")
    transactions = [
        {
            "safe_transaction_id": "tx1-123",
            "amount": 1200.00,
            "counterparty_name": "Alice Dupont",
            "status": "FRAUD_DETECTED"
        },
        {
            "safe_transaction_id": "tx2-456",
            "amount": 890.00,
            "counterparty_name": "Jean Martin",
            "status": "FRAUD_DETECTED"
        }
    ]

if not transactions:
    st.info("Aucune fraude détectée.")
else:
    for tx in transactions:
        st.markdown(f"""
        **Transaction ID :** {tx['safe_transaction_id']}  
        **Montant :** {tx['amount']:.2f} €  
        **Émetteur :** {tx['counterparty_name']}  
        **Statut :** {tx['status']}
        """)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Valider", key=f"valider_{tx['safe_transaction_id']}"):
                try:
                    res = requests.post(
                        f"{SAFE_API}/frauds/validate",
                        params={"transaction_id": tx["safe_transaction_id"]}
                    )
                    res.raise_for_status()
                    st.success("Transaction validée.")
                except Exception as e:
                    st.error(f"Erreur : {e}")

        with col2:
            if st.button("Annuler", key=f"annuler_{tx['safe_transaction_id']}"):
                try:
                    res = requests.post(
                        f"{SAFE_API}/frauds/reject",
                        params={"transaction_id": tx["safe_transaction_id"]}
                    )
                    res.raise_for_status()
                    st.success("Transaction annulée.")
                except Exception as e:
                    st.error(f"Erreur : {e}")

        st.markdown("---")
