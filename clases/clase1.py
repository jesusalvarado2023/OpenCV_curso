import streamlit as st
import cv2
from PIL import Image
import numpy as np

def mostrar():
    st.title("Clase 1: Cargar y Mostrar Imágenes")

    st.code('''
import cv2

# Cargar imagen
imagen = cv2.imread('imagenes/minion.png')

# Mostrar imagen en ventana
cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
    ''')

    st.write("Resultado en Streamlit:")

    imagen = cv2.imread('imagenes/minion.png')
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    #st.image(imagen_rgb, caption="Imagen cargada", use_column_width=True)
    st.image(imagen_rgb, caption="Imagen cargada", use_container_width=True)
