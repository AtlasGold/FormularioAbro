from PIL import Image
from os import write
import streamlit as st
from streamlit.elements.number_input import Number
from streamlit.proto.Selectbox_pb2 import Selectbox 
import pandas as pd
import pyodbc 




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


#conexão

cnxn = pyodbc.connect("DRIVER={MySQL ODBC 8.0 Unicode Driver}; SERVER=127.0.0.1:3306;DATABASE=abro; UID=root; PASSWORD=@JpK92!1SHa50.; Trusted_Connection=yes;")
cursor = cnxn.cursor()


def inserir(nome,telefone,cpf):
    cursor.execute("INSERT INTO cadastro VALUES (0,'{}','{}','{}')".format(nome,telefone,cpf))
    cnxn.commit()


def inserir_an(motivo,tratamento,medicamento,qmedicamentos,alergia,qalergias,anestesia,ultimo,canal,gengiva,fuma,sangra,dor,desmaio,gravida,procedimento,cpf,nome):
    cursor.execute("INSERT INTO anamnese1 VALUES (0,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(motivo,tratamento,medicamento,qmedicamentos,alergia,qalergias,anestesia,ultimo,canal,gengiva,fuma,sangra,dor,desmaio,gravida,procedimento,cpf,nome))
    cnxn.commit()

def inserir_so(profissão,time,qtime,animal,qanimal,filho,nfilho,medo,sorriso,facebook,instagram,qinstagram,hobby,qhobby,ambiente,generom,programação, generof,cpf,nome):
    cursor.execute("INSERT INTO sociais VALUES (0,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(profissão,time,qtime,animal,qanimal,filho,nfilho,medo,sorriso,facebook,instagram,qinstagram,hobby,qhobby,ambiente,generom,programação, generof,cpf,nome))
    cnxn.commit()

    





st.title("Cadastro")
input_nome = st.text_input("Digite Seu Nome Completo")
input_telefone = st.text_input("Telefone Para Contato")
input_CPF = st.text_input("CPF")

   
col1, col2, col3 = st.columns(3)
image = Image.open('abbro.png')
col2.image(image, use_column_width=True)

st.title("Anamnese")
input_01 = st.text_input("Qual O Motivo Da Consulta ? ") 
input_02 = st.selectbox("Está Fazendo Algum Tratamento Médico ou Tem Algum Problema de Saúde ? ",["","Sim","Não"])
input_03 = st.selectbox("Está Tomando Algum Medicamento?",["","Sim","Não"])
if input_03 ==("Sim"):
     input_003 =st.text_input("Quais Medicamentos ?")
input_04 = st.selectbox("Tem Alergia a Algum Medicamento ?",["","Sim","Não"])
if input_04 ==("Sim"):
     input_004 = st.text_input("Apresenta Alergia a Quais Medicamentos ?")
input_05 = st.selectbox("Teve Alguma Reação a Anestesia Local ?",["","Sim","Não"])
input_06 = st.date_input("Quando Foi o Seu Ultimo Tratamento Odontológico ?")
input_006 = st.selectbox ("Já Realizou Tratamento de Canal ? Prótese ? Implante ? Perdeu Algum Dente ?",["","Sim","Não"])
input_07 = st.selectbox("Sua Gengiva Sangra Com Frequência ?",["","Sim","Não"])
input_08 = st.selectbox("Você Fuma ?",["","Sim","Não"])
input_09 = st.selectbox("Quando Você se Corta, Sangra Muito ?",["","Sim","Não"])
input_10 = st.selectbox("Sente Dores de Dente ? Cabeça ? Dores na Face ? Ouvido ou Articulações ?",["","Sim","Não"])
input_11 = st.selectbox("Teve Algum Desmaio, Ataques Nervoso, Epilepsia ou Convulsões ? ",["","Sim","Não"])
input_12 = st.selectbox("Pode Estar Gravida ?",["","Sim","Não"])
input_25 = st.selectbox("Já Realizou Algum Procedimento Estético Facial ? Botox? Preenchimento com Ac. Hialurônico ou PMA ?",["","Sim","Não"])


st.title("Sobre Você")

input_13 = st.text_input("Qual Sua Profissão ?")
input_14 = st.selectbox("Gosta de Futebol ?",["","Sim","Não"])
if input_14 == ("Sim") :
    input_014 = st.text_input("Para Quais Times Você Torce ?")
input_15 = st.selectbox("Tem Algum Animal De Estimação ?",["","Sim","Não"])
if input_15 == ("Sim"):
    input_015 = st.text_input("Qual ?")


input_16 = st.selectbox("Tem Filhos ?",["","Sim","Não"])
if input_16 == ("Sim"):
    input_0016 = st.text_input("Como se Chamam ?")


input_17 = st.selectbox("Tem Medo De Dentista ?",["","Sim","Não"])
input_18 = st.selectbox("Esta Satisfeito Com Sua Estética Facil e de Sorriso ? ",["","Sim","Não"])

input_19 = st.selectbox("Tem Facebook? ",["","Sim","Não"])

input_20 = st.selectbox("Tem Instagram ?",["","Sim","Não"])
if input_20 == ("Sim"):
    input_020 = st.text_input("Qual?",key='chave')

input_21 = st.selectbox("Tem Algum Hobby ?",["","Sim","Não"])
if input_21 == ("Sim"):
    input_021 = st.text_input("Quais ?")

input_22 = st.selectbox ("Gosta De Musica Ambiente ? ",["","Sim","Não"])
if input_22 == ("Sim"):
    input_022 = st.text_input("Qual Gênero/Ritmo Gosta de Ouvir ?")

input_23 = st.text_input ("Qual Tipo De Programa De Televisão Gosta De Assistir ?")
input_24 = st.text_input ("Qual Gênero De Filme Gosta ?")





if st.button("Enviar"):
    if input_03 == 'Não':
        input_003 = 'Não'
    if input_04 == 'Não':
        input_004 = 'Não'
    if input_14 == 'Não':
        input_014 = 'Nenhum'
    if input_15 == 'Não':
        input_015 = 'Nenhum'
    if input_16 == 'Não':
        input_0016 = 'Não tenho'
    if input_20 == 'Não':
        input_020 = 'Não tenho'
    if input_21 == 'Não':
        input_021 = 'Não tenho'
    if input_22 == 'Não':
        input_022 = 'Não gosto'        
    inserir(input_nome,input_telefone,input_CPF)
    inserir_an(input_01,input_02,input_03,input_003,input_04,input_004,input_05,input_06,input_006,input_07,input_08,input_09,input_10,input_11,input_12,input_25,input_CPF,input_nome )
    inserir_so(input_13,input_14,input_014,input_15,input_015,input_16,input_0016,input_17,input_18,input_19,input_20,input_020,input_21,input_021,input_22,input_022,input_23,input_24,input_CPF,input_nome)

    st.success('Dados enviados')