import streamlit as st

from utils.sidebar import display_logo_in_sidebar

display_logo_in_sidebar()

# Page Title
st.title("Processus de transactions bancaires")

# Introduction
st.markdown("""
**Problématique :** 

Comment améliorer la performance et la sécurité des transactions bancaires (virements, prélèvements) ?
""")
