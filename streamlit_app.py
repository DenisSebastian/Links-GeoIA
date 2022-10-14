import streamlit as st
#from st_functions import st_button, load_css,
import pandas as pd

#parametros
w_img = 600

# pandas display options
pd.set_option('display.max_colwidth', -1)



#Funciones
#load_css()
def load_csv_data(path_csv):
    return pd.read_csv(path_csv, sep=";")

def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link
    return f'<a target="_blank" href="{link}">{text}</a>'

# data
df = load_csv_data("data/links.csv")
df['link'] = df['link'].apply(make_clickable)

df_tab1 = df.loc[(df['Item']=='GEOIA')].to_html(escape=False)
df_tab2 = df.loc[(df['Item']=='DRONE')].to_html(escape=False)
df_tab3 = df.loc[(df['Item']=='Territorial')].to_html(escape=False)


# Sidebar
st.sidebar.image('images/denis.jpeg')
st.sidebar.header('Denis Berroeta, Magister IA.')
st.sidebar.markdown("![follow](https://img.shields.io/twitter/follow/denis_berr?style=for-the-badge&logo=twitter)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/denis-berroeta-5a0065b7?style=for-the-badge&logo=linkedin)")

# Paneles
tab1, tab2, tab3 = st.tabs([
"Geo IA", "Drones", "Análisis Territorial"])

with tab1:
   st.header("Geo Inteligencia Artificial")
   st.image("images/Sentinel-2Poster.jpg",  width=500)
   st.write(df_tab1, unsafe_allow_html=True)


with tab2:
   st.header("Drones Inteligencia Artificial")
   st.image("images/drones_cover.jpeg", width=w_img)
   st.write(df_tab2, unsafe_allow_html=True)

with tab3:
    st.header("Análisis Territorial")
    st.image("images/deck_gl.jpg", width=w_img)
    st.write(df_tab3, unsafe_allow_html=True)
