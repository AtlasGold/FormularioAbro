from PIL import Image
from os import write
import streamlit as st
from streamlit.proto.Selectbox_pb2 import Selectbox 

st.sidebar.title("Navegue Pelo Questionario")
paginaselec = st.sidebar.selectbox("Selecione as Perguntas",["Cadastro","Saúde","Pessoais"])




if paginaselec ==("Cadastro"):
   #st.markdown("<h6 style='text-align: center; ;'>Cadastro</h6>", unsafe_allow_html=True)
   st.title("Cadastro")
   input_nome = st.text_input("Digite Seu Nome")
   input_telefone = st.text_input("Telefone Para Contato")
   input_email = st.text_input("E-mail")
   col1, col2, col3 = st.columns(3)
   image = Image.open('abbro.png')
   
   col2.image(image, use_column_width=True)




if paginaselec == ("Saúde") :
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
 input_06 = st.text_input("Quando Foi o Seu Ultimo Tratamento Odontológico ?")
 input_006 = st.selectbox ("Já Realizou Tratamento de Canal ? Prótese ? Implante ? Perdeu Algum Dente ?",["","Sim","Não"])
 input_07 = st.selectbox("Sua Gengiva Sangra Com Frequência ?",["","Sim","Não"])
 input_08 = st.selectbox("Você Fuma ?",["","Sim","Não"])
 input_09 = st.selectbox("Quando Você se Corta, Sangra Muito ?",["","Sim","Não"])
 input_10 = st.selectbox("Sente Dores de Dente ? Cabeça ? Dores na Face ? Ouvido ou Articulações ?",["","Sim","Não"])
 input_11 = st.selectbox("Teve Algum Desmaio, Ataques Nervoso, Epilepsia ou Convulções ? ",["","Sim","Não"])
 input_12 = st.selectbox("Pode Estar Gravida ?",["","Sim","Não"])
 input_25 = st.selectbox("Já Realizou Algum Procedimento Estético Facial ? Botox? Preenchimento com Ac. Hialurônico ou PMA ?",["","Sim","Não"])



elif paginaselec ==("Pessoais"):
 
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
