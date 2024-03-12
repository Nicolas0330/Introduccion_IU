import streamlit as st
from PIL import Image

st.title("Aplicaviones para Ciudades Inteligentes")

st.header("En este espacio podras obtener informacion de tu ciudad")

image = Image.open('Escultura.png')
st.image(image, caption='Inteligencia Urbana')
# st.write("Enlace para mi sistema de internet de las cosas")

