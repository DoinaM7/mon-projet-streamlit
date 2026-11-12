# 🚀 Projet Data Analytics — Applications Streamlit

## 📌 Présentation du projet

Ce projet a été réalisé dans le cadre de ma formation Data Analyst.

L'objectif est de développer des applications web interactives avec Python et Streamlit, puis de les publier sur Streamlit Community Cloud.

Le projet comprend plusieurs applications :

- **Dashboard Taxis 🚕** : analyse des courses de taxis à New York avec des filtres et des indicateurs KPI.
- **Dashboard Trafic Aérien ✈️** : analyse de l'évolution du nombre de passagers aériens entre 1949 et 1960, avec graphiques, filtres et heatmap.
- **Application sécurisée 🔐** : formulaire d'authentification, navigation entre les pages, galerie photos et déconnexion.

## 🛠️ Technologies utilisées

- Python
- Pandas
- Streamlit
- Matplotlib
- Seaborn
- Plotly
- streamlit-option-menu
- bcrypt
- Git et GitHub
- Streamlit Community Cloud

## 📁 Structure du projet

```text
mon-projet-streamlit/
├── app.py
├── app_taxis.py
├── app_dataviz.py
├── app_securisee.py
├── accounts.csv
├── requirements.txt
├── README.md
└── .gitignore
```

Le fichier `accounts.csv` est utilisé localement pour l'exercice d'authentification. Il est exclu de GitHub tant qu'il contient des mots de passe en clair.

## 💻 Installation du projet en local

### 1. Cloner le dépôt GitHub

```powershell
git clone https://github.com/DoinaM7/mon-projet-streamlit.git
```

### 2. Accéder au dossier du projet

```powershell
cd mon-projet-streamlit
```

### 3. Créer un environnement virtuel

```powershell
python -m venv venv
```

### 4. Activer l'environnement virtuel

Sous Windows PowerShell :

```powershell
.\venv\Scripts\Activate.ps1
```

Sous macOS ou Linux :

```bash
source venv/bin/activate
```

### 5. Installer les dépendances

```powershell
python -m pip install -r requirements.txt
```

### 6. Lancer une application

Pour le dashboard Taxis :

```powershell
streamlit run app_taxis.py
```

Pour le dashboard aérien :

```powershell
streamlit run app_dataviz.py
```

Pour l'application avec authentification :

```powershell
streamlit run app_securisee.py
```

Cette dernière application nécessite une configuration d'authentification supplémentaire. Les identifiants réels ne sont pas fournis dans le dépôt public.

## 📊 Fonctionnalités

- Chargement et manipulation des données CSV avec Pandas.
- Visualisations interactives avec Streamlit et Seaborn.
- Filtrage des données par année et par mois.
- Affichage d'indicateurs KPI.
- Authentification des utilisateurs.
- Navigation entre plusieurs pages.
- Déconnexion et gestion de session.

## 🔐 Sécurité

Le projet utilise un fichier `.gitignore` afin d'exclure les fichiers sensibles et l'environnement virtuel.

Pour le déploiement public de l'application sécurisée, les identifiants doivent être configurés dans Streamlit Secrets, avec des mots de passe hachés.

## ⚠️ Difficultés rencontrées

Plusieurs difficultés techniques ont été rencontrées pendant le développement :

1. Mauvais emplacement initial du fichier `app.py`.
2. Configuration et activation de l'environnement virtuel Python.
3. Synchronisation du dépôt local avec GitHub.
4. Erreur `FileNotFoundError` liée au fichier `accounts.csv` sur Streamlit Cloud.
5. Erreur de filtrage des mois et de génération de la heatmap.

Ces difficultés ont permis de mieux comprendre le débogage Python, la gestion des dépendances et le déploiement d'applications.

## 🌐 Liens du projet

**Dépôt GitHub :**  
https://github.com/DoinaM7/mon-projet-streamlit

**Portfolio GitHub Pages :**  
https://doinam7.github.io/

**Applications Streamlit Cloud :**  
Liens publics à ajouter après validation des déploiements.

## 👩‍💻 Auteur

Doïna — Data Analyst en formation

Projet réalisé dans le cadre de l'apprentissage de Python, GitHub et Streamlit.
