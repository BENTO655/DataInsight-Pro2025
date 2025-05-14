import pandas as pd
from sentence_transformers import SentenceTransformer,util # Importando a biblioteca para embeddings
import streamlit as st # Importando a biblioteca para criar o aplicativo web
# Carregando o arquivo Excel com perguntas e respostas


df = pd.read_excel('perguntas_respostas_produtos.xlsx')
preguntas = df['pergunta'].tolist() # Lista de perguntas
respostas = df['resposta'].tolist() # Lista de respostas


# Load the model from the Sentence Transformers pre-trained models
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')  # Using a pre-trained model available online
perguntas_embeddings = model.encode(preguntas, convert_to_tensor=True) # convertendo perguntas para embeddings
# Função para responder perguntas

def respoder_preguntas(pregunta_cliente): # Função para responder perguntas
    perguntas_embedding = model.encode(pregunta_cliente, convert_to_tensor=True) # Convertendo a pergunta do cliente para embedding
    similaridades = util.cos_sim(perguntas_embedding, perguntas_embeddings) # Calculando a similaridade entre a pergunta do cliente e as perguntas do dataframe
    indece_mais_similar = similaridades.argmax() # Encontrando o índice da pergunta mais similar
    return respostas[indece_mais_similar] # Retornando a resposta correspondente à pergunta mais similar

# Streamlit app

st.title("Sistema de Perguntas e Respostas")  # Título do aplicativo  
st.write("Este sistema responde perguntas sobre produtos com base em um arquivo Excel contendo perguntas e respostas.")

pergunta_cliente = st.text_input("Digite sua pergunta:")

if st.button("Enviar"): # Botão para enviar a pergunta
    if pergunta_cliente: # Verificando se a pergunta não está vazia
        resposta = respoder_preguntas(pergunta_cliente) # Chamando a função para responder a pergunta
        st.write("Resposta:", resposta) # Exibindo a resposta
    else:
     st.write("Por favor, digite uma pergunta.") # Exibindo mensagem se a pergunta estiver vazia