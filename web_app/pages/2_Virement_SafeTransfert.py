import datetime

import requests
import streamlit as st
from style.custom_css import apply_custom_style
from utils.sidebar import display_logo_in_sidebar

apply_custom_style()
display_logo_in_sidebar()
# --- Config ---
BANK_API = "http://localhost:8080"
SAFE_API = "http://localhost:8081"
ACCOUNT_ID = "aaaaaaa1-aaaa-aaaa-aaaa-aaaaaaaaaaaa"

st.title("Virement SafeTransfer")

# --- Saisie email ---
destinataire_email = st.text_input("Adresse e-mail du destinataire")
destinataire = None

if destinataire_email:
    try:
        r = requests.get(f"{SAFE_API}/users/search", params={"email": destinataire_email})
        r.raise_for_status()
        destinataire = r.json()
        if not destinataire:
            st.error("Aucun utilisateur trouvé avec cet email.")
        else:
            st.success(f"Destinataire trouvé : {destinataire['name']}")
    except Exception as e:
        st.error(f"Erreur lors de la recherche : {e}")

# --- Saisie montant + bouton ---
montant = st.number_input("Montant", min_value=0.01, step=0.01, format="%.2f")
submitted = st.button("Effectuer le virement", disabled=destinataire is None)

if submitted and destinataire:
    try:
        now_iso = datetime.datetime.now().isoformat()
        payload = {
            "account_id": ACCOUNT_ID,
            "amount": montant,
            "transaction_date": now_iso,
            "status": "PENDING_USER",
            "fraud_detected": False,
            "transaction_type": "SAFETRANSFER_VIREMENT",
            "counterparty_name": destinataire["name"]
        }

        r2 = requests.post(
            f"{BANK_API}/transactions/?beneficiary_mail={destinataire_email}",
            json=payload
        )
        r2.raise_for_status()
        response = r2.json()
        safe_transaction_id = response.get("safe_transaction_id")

        if not safe_transaction_id:
            st.error("La transaction a échoué. Aucun ID reçu.")
        else:
            st.session_state["safe_transaction_id"] = safe_transaction_id
            st.session_state["validated"] = False
    except Exception as e:
        st.error(f"Erreur lors de la création : {e}")

# --- Double authentification ---
if st.session_state.get("safe_transaction_id") and not st.session_state.get("validated"):
    st.success("Transaction créée. Veuillez entrer le code de vérification.")
    st.subheader("Vérification en deux étapes")
    code = st.text_input("Code de vérification", max_chars=6)

    if st.button("Valider"):
        try:
            r3 = requests.post(
                f"{SAFE_API}/transactions/sender-validation",
                params={
                    "transaction_id": st.session_state["safe_transaction_id"],
                    "code": code
                }
            )
            r3.raise_for_status()
            st.session_state["validated"] = True
            st.success("Vérification réussie. Le virement est en cours.")
        except Exception as e:
            st.error(f"Erreur lors de la validation : {e}")

# --- Affichage final si validé ---
elif st.session_state.get("validated"):
    st.success("Vérification réussie. Le virement est en cours.")
    del st.session_state["safe_transaction_id"]
    del st.session_state["validated"]
