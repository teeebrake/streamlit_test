#import std libraries

import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

# Write a title
st.write('Gas Price Explorer')
# Write data taken from https://allisonhorst.github.io/palmerpenguins/
st.write('Little app for exploring [Aral Tankstelle	ARAL	Prinzenstraße	29] (http://wikimapia.org/11225557/de/Aral-Tankstelle-Prinzenstraße-29)')

# Put image
st.image('https://cdn.images.express.co.uk/img/dynamic/24/750x445/1075641.jpg')
# Write heading for Data
st.header('Data')
# Read csv file and output a sample of 20 data points
df_gas_price = pd.read_csv('/data_diesel_ritter.csv', sep=',')
st.write('Display a sample of data points from `penguin`', df_gas_price.sample(20))
# Add a selectbox for species
#prices = st.selectbox('Choose a type of gas', df_gas_price['diesel','e5','e10'].unique())
# Display a sample of 20 data points according to the species selected with corresponding title
# df_species = df_gas_price.loc[df_gas_price[0]==prices]
# st.write(f'Subset of data for {species}',df_species)
# # Plotting seaborn
# st.subheader('Plotting')
# fig, ax=plt.subplots()
# ax = sns.scatterplot(data = df_penguin, x='bill_length_mm', y='island', size='sex')
# st.pyplot(fig)
# # Plotting plotly

# # Bar chart count of species per island
# # Maps
# st.map(df_penguin)
# st.write('')
# # pydeck
# # Reference https://deckgl.readthedocs.io/en/latest/
# # sidebar comment
# choice = st.sidebar.radio('The End', ['yes','no'])
# name = st.text_input('Recommendations')
# st.write(name)