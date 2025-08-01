import streamlit as st
import cv2

def mostrar():
    st.title("Clase 2: Escala de Grises y Redimensionamiento")

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

    imagen = cv2.imread('imagenes/minion.png')
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(imagen, (200, 200))

    st.image(gris, caption="Escala de grises", channels="GRAY")
    st.image(resized[:, :, ::-1], caption="Redimensionada (200x200)")
