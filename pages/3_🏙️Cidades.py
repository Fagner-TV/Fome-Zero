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
#Importando dados e tratando
st.set_page_config(page_title = 'Cidades',layout= 'wide')
df = pd.read_csv('Ciclo/zomato.csv')
df1=df.copy()
df1 = df1.dropna(subset=["Cuisines"])
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
st.header("🏙️ Visão Cidades")
st.sidebar.markdown('## Filtros')
traffic_options = st.sidebar.multiselect('Escolha o País que deseja vizualizar as informações.', ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'], default=['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'])
st.sidebar.markdown('### Powered by Comunidade DS')
#Filtro de paises
linhas_selecionadas = df1['Country'].isin(traffic_options)
df1 = df1.loc[linhas_selecionadas,:]
#=====================================
#Layout Streamlit
#=====================================

with st.container():
   cidade_pais = df1[['City','Country']].groupby(['City','Country']).size().reset_index(name='Quantidade de Restaurantes')
   cidade_pais = cidade_pais.sort_values('Quantidade de Restaurantes', ascending = False)
   top5_paises = (cidade_pais.groupby('Country')['Quantidade de Restaurantes'].sum().sort_values(ascending=False).head(5).index)
   cidade_pais_top5 = cidade_pais[cidade_pais['Country'].isin(top5_paises)]
   cidade_pais_top10 = cidade_pais_top5.sort_values('Quantidade de Restaurantes', ascending = False).head(10)
   fig = px.bar(cidade_pais_top10,x = 'City', y = 'Quantidade de Restaurantes',color = 'Country',text_auto = True ,title= 'Top 10 de cidades com restaurantes', color_discrete_sequence = px.colors.qualitative.Bold,)
   fig
   
with st.container():
 col1,col2 = st.columns(2)
 with col1: 
   nivel = df1[df1['Aggregate rating']> 4]
   cidade_pais = nivel[['Country','City']].groupby(['City','Country']).size().reset_index(name ='Quantidade')
   cidade_pais = cidade_pais.sort_values('Quantidade', ascending = False)
   top5_paises = (cidade_pais.groupby('Country')['Quantidade'].sum().sort_values(ascending=False).head(5).index)
   cidade_pais_top5 = cidade_pais[cidade_pais['Country'].isin(top5_paises)]
   cidade_pais_top7 = cidade_pais_top5.sort_values('Quantidade', ascending = False).head(7)
   fig = px.bar(cidade_pais_top7,x = 'City', y = 'Quantidade',color = 'Country',title= 'Top 7 de restaurantes com a média de avalição acima de 4', color_discrete_sequence = px.colors.qualitative.Bold,text_auto = True)
   fig 
   
   with col2:
      nivel = df1[df1['Aggregate rating']< 2.5]
      cidade_pais = nivel[['Country','City']].groupby(['City','Country']).size().reset_index(name ='Quantidade')
      cidade_pais = cidade_pais.sort_values('Quantidade', ascending = False)
      top5_paises = (cidade_pais.groupby('Country')['Quantidade'].sum().sort_values(ascending=False).head(5).index)
      cidade_pais_top5 = cidade_pais[cidade_pais['Country'].isin(top5_paises)]
      cidade_pais_top7 = cidade_pais_top5.sort_values('Quantidade', ascending = False).head(7)
      fig = px.bar(cidade_pais_top7,x = 'City', y = 'Quantidade',color = 'Country',title= 'Top 7 de restaurantes com a média de avalição abaixo de 2.5', color_discrete_sequence = px.colors.qualitative.Bold,text_auto = True)
      fig 
   
with st.container():
      restaurante = df1.groupby(['City','Country'])['Cuisines'].nunique().reset_index(name='Quantidade')
      restaurante = restaurante.sort_values('Quantidade', ascending = False)
      top5_paises = (restaurante.groupby('Country')['Quantidade'].sum().sort_values(ascending=False).head(5).index)
      cidade_pais_top5 = restaurante[restaurante['Country'].isin(top5_paises)]
      restaurante_top10 =cidade_pais_top5.sort_values('Quantidade', ascending=False).head(10)
      fig = px.bar(restaurante_top10,x = 'City', y = 'Quantidade',color = 'Country',title= 'Top 10 Cidade mais restaurantes com culinária distinta', color_discrete_sequence = px.colors.qualitative.Bold,text_auto = True)

      fig           
