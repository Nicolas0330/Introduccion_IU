import streamlit as st
from PIL import Image

st.title("Aplicaviones para Ciudades Inteligentes")

st.header("En este espacio podras obtener informacion sobre el patrimonio cultural de tu ciudad")

image = Image.open('Escultura.jpg')
st.image(image, caption='Inteligencia Urbana')
# st.write("Enlace para mi sistema de internet de las cosas")
# st.write("Ingresa al link")
