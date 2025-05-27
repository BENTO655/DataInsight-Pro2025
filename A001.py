import pandas as pd
import streamlit as st

st.write("Olá, *Seja bem vindo! Bento* :sunglasses:")
st.title("Calculadora de horas trabalhadas!")


imagem = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])
if imagem is not None:
    st.image(imagem, caption='Imagem carregada', use_column_width=True)
    
# Function to calculate hours worked
def calcular_horas_trabalhadas(hora_inicio, hora_fim):
    formato = "%H:%M"
    hora_inicio = pd.to_datetime(hora_inicio, format=formato)
    hora_fim = pd.to_datetime(hora_fim, format=formato)
    horas_trabalhadas = (hora_fim - hora_inicio).seconds / 3600
    return horas_trabalhadas

# Sidebar date input
data = st.sidebar.date_input("Selecione a data")

# Streamlit inputs
hora_inicio = st.text_input("Hora de início (HH:MM)", "07:00")
hora_fim = st.text_input("Hora de término (HH:MM)", "17:00")

# Calculate and display hours worked
if st.button("Calcular"):
    horas_trabalhadas = calcular_horas_trabalhadas(hora_inicio, hora_fim)
    st.write(f"Horas trabalhadas em {data}: {horas_trabalhadas:.2f}")
