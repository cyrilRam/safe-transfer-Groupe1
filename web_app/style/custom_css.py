import streamlit as st


def apply_custom_style():
    st.markdown("""
        <style>
        /* Style des boutons */
        .stButton > button {
            background-color: #0C5DD6;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
        }

        .stButton > button:hover {
            background-color: #0949a4;
            color: white;
        }

        </style>
    """, unsafe_allow_html=True)
