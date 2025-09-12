import streamlit as st
import cv2
import numpy as np
from PIL import Image

def mostrar():
    st.title("Ejemplo 1: Cargar y Mostrar Imágenes")

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

    # Subida de imagen
    archivo = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

    if archivo is not None:
        # Leer la imagen subida
        file_bytes = np.asarray(bytearray(archivo.read()), dtype=np.uint8)
        imagen = cv2.imdecode(file_bytes, 1)
    else:
        # Imagen por defecto
        imagen = cv2.imread('imagenes/minion.png')

    # Convertir a RGB para mostrar en Streamlit
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    st.image(imagen_rgb, caption="Imagen cargada", use_container_width=True)
