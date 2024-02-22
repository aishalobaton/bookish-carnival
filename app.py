import streamlit as st
from PIL import Image

st.title("Carnaval")

st.header("Festival")
st.write("Parque de Diversiones")
image = Image.open('midway.jpg')

st.image(image, caption='Parque')


texto = st.text_input('Bienvenidos', 'Diviertanse')
st.write('Hola', texto)

st.subheader("Ahora presta atención a lo siguiente")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Primera columna")
  st.write("Este tipo de parques son divertidos")
  resp = st.checkbox('Claro que si')
  if resp:
    st.write('Asi es!')

with col2:
  st.subheader("Segunda columna")
  modo= st.radio("Qué te gusta mas de los parques de diversiones?", ('Atracciones', 'Comida', 'Música'))
  if modo == 'Atracciones':
    st.write('Las atracciones son divertidas')
  if modo == 'Comida':
    st.write('La comida es deliciosa')
  if modo == 'Música':
    st.write('La música es buena')

st.subheader("Uso de botones")
if st.button('Presiona el botón'):
  st.write('Por qué lo presionaste?')

else:
  st.write('Por qué no lo has presionado?')


