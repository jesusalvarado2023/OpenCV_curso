import streamlit as st
from clases import clase1, clase2, clase3

st.sidebar.title("Clases de OpenCV")
st.sidebar.info("Dr. Jesus Alvarado-Huayhuaz")

opcion = st.sidebar.radio("Selecciona una clase:", ("Ejemplo 1", "Ejemplo 2", "Ejemplo 3"))

if opcion == "Ejemplo 1":
    #clase1.mostrar()
elif opcion == "Ejemplo 2":
    #clase2.mostrar()
elif opcion == "Ejemplo 3":
    #clase3.mostrar()

