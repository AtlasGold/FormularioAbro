from PIL import Image
from os import write
import streamlit as st
from streamlit.proto.Selectbox_pb2 import Selectbox 
import Paginas.anamnese  
#@st.experimental_memo
#@st.cache
def pessoais():

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
    input_016 = st.number_input(label="Quantos ? ",format="%d",step=1)
    if input_016 > (1): 
        input_0016 = st.text_input("Como se Chamam ?")
    elif input_016 <= (1):
        input_00016 = st.text_input("Como se Chama?")

input_17 = st.selectbox("Tem Medo De Dentista ?",["","Sim","Não"])
input_18 = st.selectbox("Esta Satisfeito Com Sua Estética Facil e de Sorriso ? ",["","Sim","Não"])

input_19 = st.selectbox("Tem Facebook? ",["","Sim","Não"])
if input_19 == ("Sim"):
    input_019 = st.text_input("Qual?")
input_20 = st.selectbox("Tem Instagram ?",["","Sim","Não"])
if input_20 == ("Sim"):
    input_020 = st.text_input("Qual ?")

input_21 = st.selectbox("Tem Algum Hobby ?",["","Sim","Não"])
if input_21 == ("Sim"):
    input_021 = st.text_input("Quais ?")

input_22 = st.selectbox ("Gosta De Musica Ambiente ? ",["","Sim","Não"])
if input_22 == ("Sim"):
    input_022 = st.text_input("Qual Gênero/Ritmo Gosta de Ouvir ?")

input_23 = st.text_input ("Qual Tipo De Programa De Televisão Gosta De Assistir ?")
input_24 = st.text_input ("Qual Gênero De Filme Gosta ?")