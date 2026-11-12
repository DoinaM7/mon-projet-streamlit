
import streamlit as st
import pandas as pd
from pathlib import Path
from streamlit_option_menu import option_menu

# ----------------------------------
# 1. CONFIGURATION DE L'APPLICATION
# ----------------------------------

st.set_page_config(
    page_title="Application Data - Doïna",
    page_icon="🔐",
    layout="wide"
)

# ----------------------------------
# 2. CHARGEMENT DES UTILISATEURS
# ----------------------------------

# Chemin du CSV dans le dossier du projet
CSV_PATH = Path(__file__).parent / "accounts.csv"

def load_accounts():
    accounts = pd.read_csv(
        CSV_PATH,
        dtype={"name": str, "password": str}
    )

    # Nettoyer les espaces accidentels
    accounts.columns = accounts.columns.str.strip()
    accounts["name"] = accounts["name"].str.strip()
    accounts["password"] = accounts["password"].str.strip()

    return accounts


# ----------------------------------
# 3. VERIFICATION DES IDENTIFIANTS
# ----------------------------------

def authenticate(username, password):
    accounts = load_accounts()

    utilisateur = accounts[
        (accounts["name"] == username.strip()) &
        (accounts["password"] == password)
    ]

    return not utilisateur.empty


# ----------------------------------
# 4. INITIALISATION DE LA SESSION
# ----------------------------------

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""


# ----------------------------------
# 5. PAGE DE CONNEXION
# ----------------------------------

if not st.session_state["logged_in"]:

    st.title("🔐 Connexion à l'application Data")
    st.subheader("Veuillez vous identifier")

    with st.form("login_form"):

        username = st.text_input(
            "Nom d'utilisateur"
        )

        password = st.text_input(
            "Mot de passe",
            type="password"
        )

        connexion = st.form_submit_button(
            "Se connecter"
        )

    if connexion:

        if authenticate(username, password):

            st.session_state["logged_in"] = True
            st.session_state["username"] = username.strip()

            st.rerun()

        else:
            st.error(
                "Identifiant ou mot de passe incorrect."
            )

# ----------------------------------
# 6. APPLICATION APRES CONNEXION
# ----------------------------------

else:

    # Barre latérale
    with st.sidebar:

        st.success(
            f"Bienvenue {st.session_state['username']} !"
        )

        if st.button("🚪 Se déconnecter"):

            st.session_state["logged_in"] = False
            st.session_state["username"] = ""

            st.rerun()

        st.divider()

        # Menu de navigation
        selected_page = option_menu(
            menu_title="Navigation principale",
            options=["Accueil", "Galerie Photos"],
            icons=["house", "images"],
            default_index=0
        )

    # ----------------------------------
    # PAGE ACCUEIL
    # ----------------------------------

    if selected_page == "Accueil":

        st.title("🏠 Bienvenue sur mon application Data")

        st.write(
            "Cette application a été développée "
            "avec Python et Streamlit."
        )

        st.subheader("Mes compétences Data")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Python", "100 %")

        with col2:
            st.metric("Pandas", "100 %")

        with col3:
            st.metric("Streamlit", "100 %")

        st.info(
            "Utilisez le menu latéral pour "
            "accéder à la galerie photos."
        )

    # ----------------------------------
    # PAGE GALERIE PHOTOS
    # ----------------------------------

    elif selected_page == "Galerie Photos":

        st.title("📸 Galerie Photos")

        st.write("Découvrez notre galerie d'animaux.")

        images = [
            "https://static.streamlit.io/examples/cat.jpg",
            "https://static.streamlit.io/examples/dog.jpg",
            "https://static.streamlit.io/examples/owl.jpg"
        ]

        cols = st.columns(3)

        for i, image in enumerate(images):

            with cols[i]:
                st.image(
                    image,
                    caption=f"Photo {i + 1}",
                    use_container_width=True
                )
