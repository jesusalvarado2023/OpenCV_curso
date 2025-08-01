import streamlit as st
from clases import clase1, clase2, clase3

st.sidebar.title("Clases de OpenCV")
st.sidebar.info("Dr. Jesus Alvarado-Huayhuaz")

opcion = st.sidebar.radio("Selecciona una clase:", ("Clase 1", "Clase 2", "Clase 3"))

if opcion == "Clase 1":
    clase1.mostrar()
elif opcion == "Clase 2":
    clase2.mostrar()
elif opcion == "Clase 3":
    clase3.mostrar()

