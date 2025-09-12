import streamlit as st
import cv2
import numpy as np

def mostrar():
    st.title("Ejemplo 3: Detección de Bordes (Canny)")

    st.code('''
import cv2

# Cargar imagen
imagen = cv2.imread('imagenes/spiderman.PNG')

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar detector de bordes Canny
bordes = cv2.Canny(gris, 100, 200)

# Mostrar bordes
cv2.imshow('Bordes Canny', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()
    ''')

    # Subir imagen
    archivo = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

    if archivo is not None:
        # Leer imagen subida en memoria
        file_bytes = np.asarray(bytearray(archivo.read()), dtype=np.uint8)
        imagen = cv2.imdecode(file_bytes, 1)
    else:
        # Imagen por defecto
        imagen = cv2.imread('imagenes/spiderman.PNG')

    # Mostrar imagen original
    st.info("Original")
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    st.image(imagen_rgb, caption="Imagen cargada", use_container_width=True)

    # Procesar bordes
    st.info("Bordes")
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    bordes = cv2.Canny(gris, 1, 2)
    st.image(bordes, caption="Bordes detectados (Canny)", channels="GRAY")




