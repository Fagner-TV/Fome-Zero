#Libraries
from haversine import haversine
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from datetime import datetime
#bliblioteca necessária
import pandas as pd
from PIL import Image
import folium
from streamlit_folium import folium_static
import numpy as np
from folium.plugins import MarkerCluster
hide_elements = """
<style>
    /* Remove menu superior, icones e animações */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Remove barra com o correr/editar (lápis) */
    div[data-testid="stToolbar"] {
        display: none !important;
    }

    /* Remove ícone do gato / Streamlit menu */
    div[data-testid="stDecoration"] {
        display: none !important;
    }
</style>
"""
st.markdown(hide_elements, unsafe_allow_html=True)
#Importando dados e tratando

df = pd.read_csv('Ciclo/zomato.csv')
df1=df.copy()
df1 = df1.dropna(subset=["Cuisines"])
st.set_page_config(page_title = 'Main Page')
# Preenchimento do nome dos países
COUNTRIES = {
 1: "India",
 14: "Australia",
 30: "Brazil",
 37: "Canada",
 94: "Indonesia",
 148: "New Zeland",
 162: "Philippines",
 166: "Qatar",
 184: "Singapure",
 189: "South Africa",
 191: "Sri Lanka",
 208: "Turkey",
 214: "United Arab Emirates",
 215: "England",
 216: "United States of America",
 }
def country_name(df):
   df['Country'] = df['Country Code'].map(COUNTRIES)
   return df
df1 = country_name(df1)
# Criação do Tipo de Categoria de Comida
def create_price_tye(Price_range):
 if Price_range == 1:
   return "cheap"
 elif Price_range == 2:
    return "normal"
 elif Price_range == 3:
    return "expensive"
 else:
   return "gourmet"
# Criação do nome das Cores
COLORS = {
 "3F7E00": "darkgreen",
 "5BA829": "green",
 "9ACD32": "lightgreen",
 "CDD614": "orange",
 "FFBA00": "red",
 "CBCBC8": "darkred",
 "FF7800": "darkred",
 }
def color_name(df):
   df['Color_name'] = df['Rating color'].map(COLORS)
   return df
df1 = color_name(df1)
# Renomear as colunas do DataFrame
def rename_columns(dataframe):
 df1 = dataframe.copy()
 title = lambda x: inflection.titleize(x)
 snakecase = lambda x: inflection.underscore(x)
 spaces = lambda x: x.replace(" ", "")
 cols_old = list(df1.columns)
 cols_old = list(map(title, cols_old))
 cols_old = list(map(spaces, cols_old))
 cols_new = list(map(snakecase, cols_old))
 df.columns = cols_new
 return df1
#Categorizando os restaurantes por um tipo de culinária
df1['Cuisines']=df1.loc[:,'Cuisines'].apply(lambda x: x.split(",")[0])
#Tirando informações duplicadas
df1.drop_duplicates(inplace=True)
#Resetando id
df1 = df1.reset_index(drop=True)
#=====================================
#Barra Lateral
#=====================================
st.title('Fome Zero 🍽️' )
st.header("O melhor lugar para encontrar seu mais novo restaurante favorito! ")
st.sidebar.markdown('## Filtros')
paises_selecionados = st.sidebar.multiselect('Escolha o País que deseja vizualizar as informações.', ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'], default=['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'])
st.sidebar.markdown('''___''')
st.sidebar.markdown('### Powered by Comunidade DS')
#Filtro de paises
mask_country = df1['Country'].isin(paises_selecionados)
df_filtrado = df1[mask_country]
#=====================================
#Layout Streamlit
#=====================================

with st.container():
  st.header('Temos as seguintes marcas dentro da nossa platafroma:')
  col1,col2,col3,col4,col5 = st.columns(5)
  with col1:
     restaurante = df1['Restaurant Name'].count() 
     col1.metric(label='Restaurantes Cadastrados',value = restaurante)
  with col2:
     paises = len(df1['Country'].unique()) 
     col2.metric(label= "Países Cadastrados", value= paises)
  with col3:
     cidades = len(df1['City'].unique()) 
     col3.metric(label ='Cidades Cadastradas',value = cidades)  
  with col4:
    avaliacao = df1['Votes'].sum()  
    col4.metric(label='Avaliações feitas na Plataforma',value=f"{avaliacao:,}".replace(".","."))
  with col5:
     culinaria = len(df1['Cuisines'].unique()) 
     col5.metric(label = 'Tipos de culinárias oferecidas' ,value = culinaria) 
     
with st.container():
    data_plot = (
        df1[['Country', 'City', 'Latitude', 'Longitude']]
        .groupby(['Country', 'City', 'Latitude', 'Longitude'])
        .size()
        .reset_index(name='Quantidade'))
    mapa = folium.Map(
        location=[data_plot['Latitude'].mean(), data_plot['Longitude'].mean()],zoom_start=2)
    marker_cluster = MarkerCluster().add_to(mapa)
    for _, row in data_plot.iterrows():
        popup_text = (
            f"<b>País:</b> {row['Country']}<br>"
            f"<b>Cidade:</b> {row['City']}<br>"
            f"<b>Quantidade de Restaurantes:</b> {row['Quantidade']}")
        folium.Marker(
            [row['Latitude'], row['Longitude']],
            popup=popup_text
        ).add_to(marker_cluster)
    folium_static(mapa, width=1024, height=600)







