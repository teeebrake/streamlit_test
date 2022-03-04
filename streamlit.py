#import std libraries

import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import datetime
import requests

#connect to tankerkoenig.de api and retrieve live infos

api_key = 'dc0d5dcb-4386-6f2a-74df-83221c34fd55'

headers = {'Authorization': 'Bearer {}'.format(api_key)}
search_api_url = 'https://creativecommons.tankerkoenig.de/json/prices.php?'
params = {'ids': '813ed58c-b58d-4d17-895b-2078cb302649',
        'apikey': 'dc0d5dcb-4386-6f2a-74df-83221c34fd55',
          }

response = requests.get(search_api_url, headers=headers, params=params, timeout=5)

print(response.url)
print(response.status_code)
print(response.headers)

data_dict = response.json()
current_time = datetime.datetime.now()
# Write a title
st.write('Gas Price Explorer')
# Write data taken from https://allisonhorst.github.io/palmerpenguins/
st.write('Little webapp for exploring [Aral Tankstelle	ARAL	Prinzenstraße	29] (http://i4.wikimapia.org/?x=140836&y=85993&zoom=18&type=map&lng=0)')

#http://wikimapia.org/11225557/de/Aral-Tankstelle-Prinzenstraße-29
# Put image
st.image('https://cdn.images.express.co.uk/img/dynamic/24/750x445/1075641.jpg')

st.write ('Current {current_time} price of Super at Ritterstraße', data_dict['prices']['813ed58c-b58d-4d17-895b-2078cb302649']['e5'])

# Write heading for Data
st.header('Data')
# Read csv file and output a sample of 20 data points
df_gas_price = pd.read_csv('ritter_all_14_22.csv', sep=',')
st.write('Display a sample of data points from `tankerkoenig.de`', df_gas_price)
#st.write('Display a sample of data points from `tankerkoenig.de`', df_gas_price.sample(20))
# Add a selectbox for type of fuel/gas

gas_type = st.selectbox('Choose a type of gas',['diesel','e5','e10'])
# Display a sample of 20 data points according to the species selected with corresponding title
df_gas_price = df_gas_price.filter(axis =1, like=gas_type) #[df_gas_price[:,'gas_type']]
st.write(f'Subset of data for {gas_type}',df_gas_price)
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
