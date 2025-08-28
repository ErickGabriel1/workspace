import streamlit as st
import main

st.title("Gerador e Validador de CPF")

if st.button("Gerar CPF"):
    st.success(main.gerar_cpf())

cpf_input = st.text_input("Digite um CPF para verificar:")
if st.button("Verificar CPF"):
    resultado = main.verificar_cpf()
    st.info(resultado)