import streamlit as st
import pandas as pd
import plotly.express as px

st.title('🎈 Alexx_project')

st.write('Welcome to DS')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

with st.expander("Data"):
  st.write("X")
  X_raw = df.drop("species", axis=1)
  st.dataframe(X_raw)

  st.write("y")
  y_raw = df.species
  st.dataframe(y_raw)

with st.sidebar:
    st.header("Введите признаки: ")
    
    island = st.selectbox('Island', ['Dream', 'Biscoe'])
    
    bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 44.5)
    bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.3)
    flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 200.0)  # Исправлено
    body_mass_g = st.slider('Body mass (g)', 2700, 6300, 4500)  # Исправлено
    
    gender = st.selectbox("Gender", ['female', 'male'])

import plotly.express as px

st.subheader('Data Visualization')
fig = px.scatter(
    df,
    x='bill_length_mm',
    y='bill_depth_mm',
    color='island',
    title='Bill Length vs. Bill Depth by Island'
)
st.plotly_chart(fig)

fig2 = px.histogram(
    df, 
    x='body_mass_g', 
    nbins=30, 
    title='Distribution of Body Mass'
)
st.plotly_chart(fig2)

