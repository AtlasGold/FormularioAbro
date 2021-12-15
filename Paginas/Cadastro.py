from PIL import Image
from os import write
import streamlit as st
from streamlit.proto.Selectbox_pb2 import Selectbox 
import Paginas.anamnese  
import Paginas.pessoais as pessoais

#@st.cache

#trocar o nome da pagina e o icone
st.set_page_config(page_title = "Abro",
    page_icon=":smiley:")
#remover o botão de Menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: visible;}
            </style>
            
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
Paginas.anamnese.anamnesePage()
pessoais.pessoais()

st.sidebar.title("Navegue Pelo Questionario")
paginaselec = st.sidebar.selectbox("Selecione as Perguntas",["Cadastro","Saúde","Pessoais"])

st.form(key="form1")
st.title("Cadastro")
input_nome = st.text_input("Digite Seu Nome")
input_telefone = st.text_input("Telefone Para Contato")
input_email = st.text_input("E-mail")
proximo = st.button("proximo")

   
col1, col2, col3 = st.columns(3)
image = Image.open('abbro.png')
col2.image(image, use_column_width=True)
  
  


      