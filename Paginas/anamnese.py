
from PIL import Image
from os import write
import streamlit as st
from streamlit.proto.Selectbox_pb2 import Selectbox 
import Paginas.pessoais as pessoais
#@st.experimental_memo
#@st.cache
def anamnesePage():

 #with st.form(key="form2"):

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
  input_11 = st.selectbox("Teve Algum Desmaio, Ataques Nervoso, Epilepsia ou Convulsões ? ",["","Sim","Não"])
  input_12 = st.selectbox("Pode Estar Gravida ?",["","Sim","Não"])
  input_25 = st.selectbox("Já Realizou Algum Procedimento Estético Facial ? Botox? Preenchimento com Ac. Hialurônico ou PMA ?",["","Sim","Não"])
  proximo1 = st.button("prosseguir")
pessoais.pessoais()
