import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # Ajout de l'importation de seaborn
st.set_option('deprecation.showPyplotGlobalUse', False)

# Charger les données
df = pd.read_csv ('sakila.csv')

# Sidebar pour filtrer par notation de film
selected_ratings = st.sidebar.multiselect('Sélectionnez les notations de film:', df['film_rating'].unique())

# Section : Aperçu du jeu de données
st.title('Analyse des données Sakila')
st.sidebar.header('Options de filtrage')

# Afficher des informations de base sur le dataframe
st.header('1. Aperçu du jeu de données')
st.subheader('1.1 Informations sur le dataframe')
st.write(f"Nombre de lignes et de colonnes : {df.shape}")
st.write(df.info())

# Afficher les premières et dernières lignes du dataframe
st.subheader('1.2 Premières et dernières lignes')
st.write("Premières lignes :")
st.write(df.head())
st.write("Dernières lignes :")
st.write(df.tail())

# Section : Nettoyage des données
st.header('2. Nettoyage des données')
st.subheader('2.1 Données nettoyées')
# Supprimer les lignes avec des valeurs manquantes
df_cleaned = df.dropna()
st.write(df_cleaned)

# Section : Statistiques descriptives
st.header('3. Statistiques descriptives')
st.write(df_cleaned.describe())

# Section : Analyse des taux de location
st.header('4. Analyse des taux de location')
# Moyenne de film_rental_rate
st.subheader('4.1 Moyenne de film_rental_rate')
st.write("Moyenne :", df_cleaned['film_rental_rate'].mean().round(2))

# Graphique de densité de film_rental_rate avec seaborn
st.subheader('4.2 Graphique de densité de film_rental_rate')
fig_density = plt.figure()
# Density plot of film_rental_rate with seaborn
st.subheader('4.2 Density Plot of film_rental_rate')
fig_density = plt.figure()
sns.histplot(df_cleaned['film_rental_rate'].values, kde=True, color='0.75')
st.pyplot(fig_density)

st.pyplot(fig_density)

# Graphique à barres de film_rental_rate
st.subheader('4.3 Graphique à barres de film_rental_rate')
B = df_cleaned['film_rental_rate'].value_counts().plot(kind='bar', figsize=(12, 5), color='0.75')
B.set_ylabel('Nombre de locations')
B.set_xlabel('Taux')
st.pyplot()

# Section : Analyse du retour sur investissement locatif
st.header('5. Analyse du retour sur investissement locatif')
# Calculer et afficher rental_gain_return
df_cleaned['rental_gain_return'] = df_cleaned['film_rental_rate'] / df_cleaned['film_replacement_cost'] * 100
st.subheader('5.1 Rental Gain Return')
st.write("Moyenne :", df_cleaned['rental_gain_return'].mean().round(2))
st.write("Médiane :", df_cleaned['rental_gain_return'].median().round(2))

# Graphique de densité de rental_gain_return avec lignes médiane et moyenne
st.subheader('5.2 Graphique de densité de Rental Gain Return')
ax = df_cleaned['rental_gain_return'].plot(kind='density', color='0.75', figsize=(14, 6))
ax.axvline(df_cleaned['rental_gain_return'].median().round(2)).set_color('steelblue')
ax.axvline(df_cleaned['rental_gain_return'].mean().round(2)).set_color('violet')
st.pyplot(ax.figure)

# Section : Coût de remplacement maximal
st.header('6. Coût de remplacement maximal du film')
# Coût de remplacement maximal et titre de film correspondant
max_replacement_cost = df_cleaned['film_replacement_cost'].max()
max_cost_films = df_cleaned.loc[df_cleaned['film_replacement_cost'] == max_replacement_cost, 'film_title'].unique()

st.write("Coût de remplacement maximal :", max_replacement_cost)
st.write("Titres de film avec coût de remplacement maximal :", max_cost_films)

# Section : Films avec notations 'PG' ou 'PG-13'
st.header('7. Films avec notations "PG" ou "PG-13"')
selected_films = df_cleaned.loc[(df_cleaned['film_rating'] == 'PG') | (df_cleaned['film_rating'] == 'PG-13')]
st.write(selected_films)


