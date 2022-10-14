import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

# Sidebar
st.sidebar.image(Image.open('images/denis.jpeg'))
st.sidebar.header('Denis Berroeta, Magister IA.')
st.sidebar.markdown("![follow](https://img.shields.io/twitter/follow/denis_berr?style=for-the-badge&logo=twitter)")
st.sidebar.markdown("[linkedIn](https://www.linkedin.com/in/denis-berroeta-5a0065b7?style=for-the-badge&logo=linkedin)")

# Paneles
tab1, tab2, tab3, tab4 = st.tabs([
"Inteligencia Artificial", "Satellites", "Drones", "Análisis Territorial"])

with tab1:
   st.header("Inteligencia Artificial")
   st.image("images/geoIA.jpeg", width=400)

with tab2:
   st.header("Satelites")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("Drones")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab4:
      st.header("Análisis Territorial")
      st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
