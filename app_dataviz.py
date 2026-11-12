
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Titre du dashboard
st.title("✈️ Dashboard Analyse du Trafic Aérien - Doïna")

st.write("Analyse de l'évolution du nombre de passagers aériens entre 1949 et 1960.")

# Charger les données avec le cache Streamlit
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
    return pd.read_csv(url)

# Récupérer les données
df = load_data()

# Afficher les 10 premières lignes
st.subheader("Aperçu des données")
st.dataframe(df.head(10))

# Afficher le nombre total de passagers
total_passagers = df["passengers"].sum()

st.metric(
    label="Nombre total de passagers",
    value=f"{total_passagers:,}"
)


# Évolution annuelle des passagers
st.subheader("📊 Évolution annuelle du trafic aérien")


# Filtrer les données par année
st.subheader("📅 Filtrer par période")

annees = st.slider(
    "Sélectionnez une plage d'années :",
    min_value=1949,
    max_value=1960,
    value=(1949, 1960)
)

# Filtrer le DataFrame
df_filtre = df[
    (df["year"] >= annees[0]) &
    (df["year"] <= annees[1])
]


# Liste des mois
mois = [
    "Tous les mois",
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
]

# Menu déroulant
mois_choisi = st.selectbox(
    "📅 Sélectionnez un mois :",
    mois
)

# Filtrer selon le mois sélectionné
if mois_choisi != "Tous les mois":
    df_filtre = df_filtre[
        df_filtre["month"] == mois_choisi
    ]


# KPI dynamique
total_filtre = df_filtre["passengers"].sum()

st.metric(
    label="✈️ Total des passagers sélectionnés",
    value=f"{total_filtre:,}"
)


# Regrouper les passagers par année
passagers_annuels = df_filtre.groupby("year")["passengers"].sum()

# Afficher le graphique
st.subheader("📊 Évolution annuelle du trafic aérien")
st.bar_chart(passagers_annuels)


# Heatmap interactive
st.subheader("🔥 Carte de chaleur du trafic aérien")

afficher_heatmap = st.checkbox("Afficher la Heatmap")

if afficher_heatmap:

    # Organiser les données par mois et année
    tableau_heatmap = df_filtre.pivot(
        index="month",
        columns="year",
        values="passengers"
    )

    # Créer le graphique
    fig, ax = plt.subplots(figsize=(12, 6))

    sns.heatmap(
        tableau_heatmap,
        annot=True,
        fmt=".0f",
        cmap="Blues",
        ax=ax
    )

    ax.set_title("Nombre de passagers par mois et par année")
    ax.set_xlabel("Année")
    ax.set_ylabel("Mois")

    # Afficher dans Streamlit
    st.pyplot(fig)
    plt.close(fig)
