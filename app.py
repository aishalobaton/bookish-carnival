import streamlit as st
from PIL import Image

st.title("Carnaval")

st.header("Festival")
st.write("Parque de Diversiones")
image = Image.open('midway.jpg')

st.image(image, caption='Parque')
