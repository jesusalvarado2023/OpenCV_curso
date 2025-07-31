import streamlit as st
import cv2

def mostrar():
    st.title("Clase 3: Detección de Bordes (Canny)")

    st.code('''
import cv2

# Cargar imagen
imagen = cv2.imread('imagenes/ejemplo.jpg')

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar detector de bordes Canny
bordes = cv2.Canny(gris, 100, 200)

# Mostrar bordes
cv2.imshow('Bordes Canny', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()
    ''')

    imagen = cv2.imread('imagenes/ejemplo.jpg')
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    bordes = cv2.Canny(gris, 100, 200)

    st.image(bordes, caption="Bordes detectados (Canny)", channels="GRAY")
