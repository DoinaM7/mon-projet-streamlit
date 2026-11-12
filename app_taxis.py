
import streamlit as st
import pandas as pd

# Titre du dashboard
st.title("🚕 Dashboard Analyse Taxis - Doïna")

st.write("Analyse des courses de taxis à New York")

# Charger les données
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"

df = pd.read_csv(url)

# Choisir un quartier
quartier = st.selectbox(
    "Choisissez un quartier de départ :",
    df["pickup_borough"].dropna().unique()
)

# Filtrer les données
df_filtre = df[df["pickup_borough"] == quartier]

# Afficher les 5 premières lignes
st.subheader("Aperçu des courses")
st.dataframe(df_filtre.head())

# Afficher le KPI
st.metric(
    label="Nombre total de courses",
    value=len(df_filtre)
)
