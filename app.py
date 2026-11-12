
import streamlit as st
import pandas as pd

st.title("Mon Premier Dashboard Streamlit 🚀")

st.write("Bienvenue sur mon application interactive dédiée à l'analyse de données.")

st.subheader("Mes premières interactions")

if st.button("Cliquez ici"):
    st.success("Bravo ! Mon premier bouton fonctionne 🎉")


# Case à cocher
afficher_details = st.checkbox("Afficher plus d'informations")

if afficher_details:
    st.info("Je suis en formation Data Analyst et j'apprends Streamlit.")


# Menu déroulant
outil = st.selectbox(
    "Choisissez votre outil de visualisation préféré :",
    ["Seaborn", "Matplotlib", "Plotly", "Power BI"]
)

st.write(f"Vous avez choisi : **{outil}**")


# Sélection de plusieurs compétences
competences = st.multiselect(
    "Sélectionnez vos compétences Data :",
    ["Python", "SQL", "Pandas", "Machine Learning", "Git"],
    default=["Python", "SQL"]
)

st.write("Compétences sélectionnées :", competences)
