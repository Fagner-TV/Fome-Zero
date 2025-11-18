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
st.set_page_config(page_title = 'Cozinha',layout= 'wide')

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
st.header("🍽️ Visão Tipos de Culinárias")
st.sidebar.markdown('## Filtros')
paises_selecionados = st.sidebar.multiselect('Escolha o País que deseja vizualizar as informações.', ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'], default=['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'])
st.sidebar.markdown('''___''')
valor_slider = st.sidebar.select_slider('Selecione a quantidade de restaurantes que deseja vizualizar',options= list(range(1,21)),value = 10)
culinarias_selecionadas = st.sidebar.multiselect('Escolha os tipos de culinária.', ['Italian', 'European', 'Filipino', 'American', 'Korean', 'Pizza',
       'Taiwanese', 'Japanese', 'Coffee', 'Chinese', 'Seafood',
       'Singaporean', 'Vietnamese', 'Latin American', 'Healthy Food',
       'Cafe', 'Fast Food', 'Brazilian', 'Argentine', 'Arabian', 'Bakery',
       'Tex-Mex', 'Bar Food', 'International', 'French', 'Steak',
       'German', 'Sushi', 'Grill', 'Peruvian', 'North Eastern',
       'Ice Cream', 'Burger', 'Mexican', 'Vegetarian', 'Contemporary',
       'Desserts', 'Juices', 'Beverages', 'Spanish', 'Thai', 'Indian',
       'Mineira', 'BBQ', 'Mongolian', 'Portuguese', 'Greek', 'Asian',
       'Author', 'Gourmet Fast Food', 'Lebanese', 'Modern Australian',
       'African', 'Coffee and Tea', 'Australian', 'Middle Eastern',
       'Malaysian', 'Tapas', 'New American', 'Pub Food', 'Southern',
       'Diner', 'Donuts', 'Southwestern', 'Sandwich', 'Irish',
       'Mediterranean', 'Cafe Food', 'Korean BBQ', 'Fusion', 'Canadian',
       'Breakfast', 'Cajun', 'New Mexican', 'Belgian', 'Cuban', 'Taco',
       'Caribbean', 'Polish', 'Deli', 'British', 'California', 'Others',
       'Eastern European', 'Creole', 'Ramen', 'Ukrainian', 'Hawaiian',
       'Patisserie', 'Yum Cha', 'Pacific Northwest', 'Tea', 'Moroccan',
       'Burmese', 'Dim Sum', 'Crepes', 'Fish and Chips', 'Russian',
       'Continental', 'South Indian', 'North Indian', 'Salad',
       'Finger Food', 'Mandi', 'Turkish', 'Kerala', 'Pakistani',
       'Biryani', 'Street Food', 'Nepalese', 'Goan', 'Iranian', 'Mughlai',
       'Rajasthani', 'Mithai', 'Maharashtrian', 'Gujarati', 'Rolls',
       'Momos', 'Parsi', 'Modern Indian', 'Andhra', 'Tibetan', 'Kebab',
       'Chettinad', 'Bengali', 'Assamese', 'Naga', 'Hyderabadi', 'Awadhi',
       'Balti', 'Scottish', 'Cantonese', 'Sri Lankan', 'Khaleeji',
       'South African', 'Drinks Only', 'Durban', 'World Cuisine',
       'Izgara', 'Home-made', 'Giblets', 'Fresh Fish', 'Restaurant Cafe',
       'Kumpir', 'Döner', 'Turkish Pizza', 'Ottoman', 'Old Turkish Bars',
       'Kokoreç'], default=['Italian', 'European', 'Filipino', 'American', 'Korean', 'Pizza',
       'Taiwanese', 'Japanese', 'Coffee', 'Chinese', 'Seafood',
       'Singaporean', 'Vietnamese', 'Latin American', 'Healthy Food',
       'Cafe', 'Fast Food', 'Brazilian', 'Argentine', 'Arabian', 'Bakery',
       'Tex-Mex', 'Bar Food', 'International', 'French', 'Steak',
       'German', 'Sushi', 'Grill', 'Peruvian', 'North Eastern',
       'Ice Cream', 'Burger', 'Mexican', 'Vegetarian', 'Contemporary',
       'Desserts', 'Juices', 'Beverages', 'Spanish', 'Thai', 'Indian',
       'Mineira', 'BBQ', 'Mongolian', 'Portuguese', 'Greek', 'Asian',
       'Author', 'Gourmet Fast Food', 'Lebanese', 'Modern Australian',
       'African', 'Coffee and Tea', 'Australian', 'Middle Eastern',
       'Malaysian', 'Tapas', 'New American', 'Pub Food', 'Southern',
       'Diner', 'Donuts', 'Southwestern', 'Sandwich', 'Irish',
       'Mediterranean', 'Cafe Food', 'Korean BBQ', 'Fusion', 'Canadian',
       'Breakfast', 'Cajun', 'New Mexican', 'Belgian', 'Cuban', 'Taco',
       'Caribbean', 'Polish', 'Deli', 'British', 'California', 'Others',
       'Eastern European', 'Creole', 'Ramen', 'Ukrainian', 'Hawaiian',
       'Patisserie', 'Yum Cha', 'Pacific Northwest', 'Tea', 'Moroccan',
       'Burmese', 'Dim Sum', 'Crepes', 'Fish and Chips', 'Russian',
       'Continental', 'South Indian', 'North Indian', 'Salad',
       'Finger Food', 'Mandi', 'Turkish', 'Kerala', 'Pakistani',
       'Biryani', 'Street Food', 'Nepalese', 'Goan', 'Iranian', 'Mughlai',
       'Rajasthani', 'Mithai', 'Maharashtrian', 'Gujarati', 'Rolls',
       'Momos', 'Parsi', 'Modern Indian', 'Andhra', 'Tibetan', 'Kebab',
       'Chettinad', 'Bengali', 'Assamese', 'Naga', 'Hyderabadi', 'Awadhi',
       'Balti', 'Scottish', 'Cantonese', 'Sri Lankan', 'Khaleeji',
       'South African', 'Drinks Only', 'Durban', 'World Cuisine',
       'Izgara', 'Home-made', 'Giblets', 'Fresh Fish', 'Restaurant Cafe',
       'Kumpir', 'Döner', 'Turkish Pizza', 'Ottoman', 'Old Turkish Bars',
       'Kokoreç'])
st.sidebar.markdown('### Powered by Comunidade DS')
#Filtro de paises
mask_country = df1['Country'].isin(paises_selecionados)
mask_cuisines = df1['Cuisines'].isin(culinarias_selecionadas)
df_filtrado = df1[mask_country & mask_cuisines]
#=====================================
#Layout Streamlit
#=====================================

st.subheader("Melhores Restaurantes dos Principais tipos Culinários")

# 5 colunas lado a lado
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
   culinaria = df1[(df1['Cuisines'] == 'Italian') & (df1['Country'] == 'India')]
   restaurante = culinaria[['Restaurant Name','Aggregate rating','Average Cost for two']].groupby('Restaurant Name').mean(numeric_only=True).reset_index()
   restaurante = restaurante.sort_values('Aggregate rating', ascending=False).reset_index(drop=True)

   if restaurante.empty:
     col1.metric(label="Italiana | Darshan",value="4.9/5.0",help="País: Indian ,  Cidade: Pune,  Média de prato para dois: 700(Indian Rupees(RS.).")
   else:
     idx_max = culinaria['Aggregate rating'].idxmax()
     maior_restaurante = culinaria.loc[idx_max,'Restaurant Name']
     quantidade = float(round(culinaria.loc[idx_max, 'Aggregate rating'], 1))
     cidade = culinaria.loc[idx_max, 'City']
     preco_medio = int(culinaria.loc[idx_max,'Average Cost for two'])
     moeda = "₹"
     col1.metric(label=f"Italiana: {maior_restaurante} | País: Índia",
        value=f"{quantidade}/5.0",
        help=f"País: India, Cidade: {cidade}, Preço médio p/ dois: 2500(Indian Rupees({moeda}.)")

with col2:
  
  culinaria = df1[(df1['Cuisines'] == 'American') & (df1['Country'] == 'England')]
  restaurante = culinaria[['Restaurant Name','Aggregate rating','Average Cost for two']].groupby('Restaurant Name').mean(numeric_only=True).reset_index()
  restaurante = restaurante.sort_values('Aggregate rating', ascending=False).reset_index(drop=True)
  if restaurante.empty:
    col2.metric(label="Italiana | Celino's",value="4.9/5.0",help="País: England ,  Cidade: Glasgow,  Média de prato para dois: 45 Pounds({€}.))")
  else:
   idx_max = culinaria['Aggregate rating'].idxmax()
   maior_restaurante = culinaria.loc[idx_max,'Restaurant Name']
   quantidade = float(round(culinaria.loc[idx_max, 'Aggregate rating'], 1))
   cidade = culinaria.loc[idx_max, 'City']
   preco_medio = int(culinaria.loc[idx_max,'Average Cost for two'])
   moeda = "£"
   col2.metric(label=f"Italiana: {maior_restaurante} | País: England ",value=f"{quantidade}/5.0",help=f"País: England, Cidade: {cidade}, Preço médio p/ dois:  45 Pounds({moeda}.)) ")
  
with col3:
  culinaria = df1[(df1['Cuisines'] == 'Arabian') & (df1['Country'] == 'India')]
  restaurante = culinaria[['Restaurant Name','Aggregate rating','Average Cost for two']].groupby('Restaurant Name').mean(numeric_only=True).reset_index()
  restaurante = restaurante.sort_values('Aggregate rating', ascending=False).reset_index(drop=True)

  if restaurante.empty:
    col3.metric(label="Italiana |Zolocrust - Hotel Clarks",value="4.9/5.0",help="País:India ,  Cidade:Jaipur,  Média de prato para dois:2500 Indian Rupees(RS.))")
  else:
    idx_max = culinaria['Aggregate rating'].idxmax() 
    maior_restaurante = culinaria.loc[idx_max,'Restaurant Name']
    quantidade = float(round(culinaria.loc[idx_max, 'Aggregate rating'], 1))
    cidade = culinaria.loc[idx_max, 'City']
    preco_medio = int(culinaria.loc[idx_max,'Average Cost for two'])
    moeda = "₹"
    col3.metric(label=f"Italiana: {maior_restaurante} | País: Índia",value=f"{quantidade}/5.0",help=f"País: India, Cidade: {cidade}, Preço médio p/ dois: 600 Indian Rupees({moeda}.))")

with col4:
 culinaria = df1[(df1['Cuisines'] == 'Japanese') & (df1['Country'] == 'England')]
 restaurante = culinaria[['Restaurant Name','Aggregate rating','Average Cost for two']].groupby('Restaurant Name').mean(numeric_only = True).reset_index()
 restaurante = restaurante.sort_values('Aggregate rating', ascending=False).reset_index(drop=True)
 if restaurante.empty:
    col4.metric(label="Italiana |Bocca Di Lupo",value="4.9/5.0",help="País:England ,  Cidade:London,  Média de prato para dois: 110 Pounds({€}.))")
 else:
     idx_max = culinaria['Aggregate rating'].idxmax()
     maior_restaurante = culinaria.loc[idx_max,'Restaurant Name']
     quantidade = float(round(culinaria.loc[idx_max, 'Aggregate rating'], 1))
     cidade = culinaria.loc[idx_max, 'City']
     preco_medio = int(culinaria.loc[idx_max,'Average Cost for two'])
     quantidade = float(round(restaurante.iloc[0, 1], 1))
     moeda = "£" 

     col4.metric(label=f"Italiana: {maior_restaurante} | País: England",value=f"{quantidade}/5.0",help=f"País:England ,  Cidade:{cidade},  Média de prato para dois: 110 Pounds({moeda}.))")

with col5:
  
 culinaria = df1[(df1['Cuisines'] == 'Brazilian') & (df1['Country'] == 'Brazil')]
 restaurante = culinaria[['Restaurant Name','Aggregate rating','Average Cost for two']].groupby('Restaurant Name').mean(numeric_only= True).reset_index()
 restaurante = restaurante.sort_values('Aggregate rating', ascending=False).reset_index(drop=True)
 if restaurante.empty:
    col5.metric(label="Italiana |Braseiro da Gávea",value="4.9/5.0",help="País:Brazil ,  Cidade:Rio de Janeiro,  Média de prato para dois: 110 Brazilian Real({R$}.))")
 else:
     idx_max = culinaria['Aggregate rating'].idxmax()
     maior_restaurante = culinaria.loc[idx_max,'Restaurant Name']
     quantidade = float(round(culinaria.loc[idx_max, 'Aggregate rating'], 1))
     cidade = culinaria.loc[idx_max, 'City']
     preco_medio = int(culinaria.loc[idx_max,'Average Cost for two'])
     quantidade = float(round(restaurante.iloc[0, 1], 1))
     moeda = "R$" 
     col5.metric(label=f"Italiana: {maior_restaurante} | País: Brazil",value=f"{quantidade}/5.0",help=f"País:Brazil ,  Cidade:{cidade},  Média de prato para dois: 100  Brazilian Real({moeda}.))")

with st.container():
  st.title(f'Top {valor_slider} Restaurantes')
  if df_filtrado.empty:
    st.warning("Nenhum restaurante encontrado com os filtros selecionados.")
  else:
    idx = df_filtrado.groupby('Restaurant Name')['Aggregate rating'].idxmax()
    restaurante = df_filtrado.loc[idx, ['Restaurant ID','Country','City','Cuisines',
            'Average Cost for two','Votes','Restaurant Name','Aggregate rating']]
    restaurante = restaurante.sort_values('Aggregate rating', ascending=False)
    st.dataframe(restaurante.head(valor_slider))

with st.container():
  col1,col2 = st.columns(2)
  with col1:
   df_culinarias = df1[mask_country] 
   culinaria = (df_culinarias.groupby('Cuisines')['Aggregate rating'].mean().reset_index().rename(columns={'Cuisines': 'Tipo de Culinária','Aggregate rating':'Média de Avaliações'}).sort_values('Média de Avaliações',ascending=False))
   top_culinarias = culinaria.head(valor_slider) 
   fig = go.Figure()
   fig.add_trace(go.Bar(x=top_culinarias['Tipo de Culinária'],y=top_culinarias['Média de Avaliações'],text=top_culinarias['Média de Avaliações'].round(2),textposition='outside'))
   fig.update_layout(title=f"Top {valor_slider} Melhores Tipos de Culinárias",xaxis_title="Tipo de Culinária",yaxis_title="Média de Avaliações",xaxis_tickangle=-45,height=500)
   st.plotly_chart(fig,use_container_width=True)
   
  with col2:
   df_culinarias = df1[mask_country]  
   culinaria = (df_culinarias.groupby('Cuisines')['Aggregate rating'].mean().reset_index().rename(columns={'Cuisines': 'Tipo de Culinária','Aggregate rating':'Média de Avaliações'}).sort_values('Média de Avaliações',ascending=True))
   top_culinarias = culinaria.head(valor_slider) 
   fig = go.Figure()
   fig.add_trace(go.Bar(x=top_culinarias['Tipo de Culinária'],y=top_culinarias['Média de Avaliações'],text=top_culinarias['Média de Avaliações'].round(2),textposition='outside'))
   fig.update_layout(title=f"Top {valor_slider} Piores Tipos de Culinárias",xaxis_title="Tipo de Culinária",yaxis_title="Média de Avaliações",xaxis_tickangle=-45,height=500)
   st.plotly_chart(fig)   
   