import os

import streamlit as st


def display_logo_in_sidebar():
    try:
        # Résout le chemin absolu vers le logo depuis ce fichier
        logo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'mockbank_logo.png'))
        st.sidebar.image(logo_path, use_container_width=True)
    except Exception as e:
        st.sidebar.markdown("**Mockbank**")
        st.sidebar.caption(f"(Erreur chargement logo : {e})")
