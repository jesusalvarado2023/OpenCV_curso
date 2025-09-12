import streamlit as st
import cv2
import numpy as np

def mostrar():
    st.title("Ejemplo 2: Escala de Grises y Redimensionamiento")

    st.code('''
import cv2

# Cargar imagen
imagen = cv2.imread('imagenes/minion.png')

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Redimensionar imagen
resized = cv2.resize(imagen, (200, 200))

# Mostrar resultados
cv2.imshow('Grises', gris)
cv2.imshow('Redimensionada', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
    ''')

    # Subir imagen nueva
    archivo = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

    if archivo is not None:
        # Leer la imagen desde el uploader
        file_bytes = np.asarray(bytearray(archivo.read()), dtype=np.uint8)
        imagen = cv2.imdecode(file_bytes, 1)
    else:
        # Imagen por defecto
        imagen = cv2.imread('imagenes/pecera.PNG')

    # Escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Redimensionar (200x200)
    resized = cv2.resize(imagen, (200, 200))

    # Mostrar resultados
    st.info("Imagen en escala de grises")
    st.image(gris, caption="Escala de grises", channels="GRAY")

    st.info("Imagen redimensionada")
    st.image(resized[:, :, ::-1], caption="Redimensionada (200x200)")
