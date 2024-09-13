import streamlit as st

# Titre de l'application
st.title("Dashboard des Accidents de Voiture")

import pandas as pd
import numpy as np

# Simuler des données
np.random.seed(0)
dates = pd.date_range('2015-01-01', periods=2000, freq='D')
data = {
    'Date': dates,
    'Accidents': np.random.poisson(2, size=len(dates)),
    'Weather_Condition': np.random.choice(['Clear', 'Rainy', 'Snowy', 'Foggy'], size=len(dates)),
    'Weekend': (dates.weekday >= 5).astype(int)
}
df = pd.DataFrame(data)

# Convertir 'Date' en index datetime
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Ajouter des colonnes pour l'année, le mois, et le jour de la semaine
df['Year'] = df.index.year
df['Month'] = df.index.month
df['Weekday'] = df.index.weekday

print(df.head())
df
# Sélectionner l'année
selected_year = st.selectbox('Sélectionner l\'année:', df['Year'].unique())

# Filtrer les données en fonction de l'année sélectionnée
filtered_df = df[df['Year'] == selected_year]

import plotly.express as px

# Graphique de tendance mensuelle
st.subheader('Nombre mensuel d\'accidents')
monthly_accidents = filtered_df.resample('M')['Accidents'].sum()
fig_monthly_trend = px.line(monthly_accidents, x=monthly_accidents.index, y='Accidents', title='Nombre mensuel d\'accidents')

st.plotly_chart(fig_monthly_trend)
