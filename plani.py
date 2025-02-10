import pandas as pd
import seaborn as sns
import streamlit as st
# Configurações
# Carregar o arquivo Excel
file_path = 'dados_ficticios.xlsx'
df = pd.read_excel(file_path)
st.title('Análise de Dados Fictícios')
genero = df['Gênero'].value_counts() # Contagem de gêneros
linguagem = df["Linguagem Fluente"].value_counts() # Contagem de linguagens
cargo = df["Cargo Atual"].value_counts() # Contagem de cargos
religiao = df["Religião"].value_counts() # Contagem de religiões
estado_de_saude = df["Estado de Saúde"].value_counts() # Contagem de estados de saúde
Estado_Civil = df["Estado Civil"].value_counts() # Contagem de estados civis
Salario = df["Salário Mensal"]
# ssd
st.sidebar.header('Filtros') # Título da barra lateral
# Filtro por Gênero
genero_selecionado = st.sidebar.multiselect('Gênero', df['Gênero'].unique(), df['Gênero'].unique()) # Seleção de gêneros
df_filtrado = df[df['Gênero'].isin(genero_selecionado)]

# Filtro por Linguagem Fluente
linguagem_selecionada = st.sidebar.multiselect('Linguagem Fluente', df['Linguagem Fluente'].unique(), df['Linguagem Fluente'].unique()) # Seleção de linguagens
df_filtrado = df_filtrado[df_filtrado['Linguagem Fluente'].isin(linguagem_selecionada)] # Filtrar o DataFrame

# Filtro por Cargo Atual
cargo_selecionado = st.sidebar.multiselect('Cargo Atual', df['Cargo Atual'].unique(), df['Cargo Atual'].unique())   # Seleção de cargos
df_filtrado = df_filtrado[df_filtrado['Cargo Atual'].isin(cargo_selecionado)] # Filtrar o DataFrame

# Filtro por Religião
religiao_selecionada = st.sidebar.multiselect('Religião', df['Religião'].unique(), df['Religião'].unique())     # Seleção de religiões
df_filtrado = df_filtrado[df_filtrado['Religião'].isin(religiao_selecionada)] # Filtrar o DataFrame

# Filtro por Estado de Saúde
estado_de_saude_selecionado = st.sidebar.multiselect('Estado de Saúde', df['Estado de Saúde'].unique(), df['Estado de Saúde'].unique()) # Seleção de estados de saúde
df_filtrado = df_filtrado[df_filtrado['Estado de Saúde'].isin(estado_de_saude_selecionado)] # Filtrar o DataFrame

# Filtro por Estado Civil
estado_civil_selecionado = st.sidebar.multiselect('Estado Civil', df['Estado Civil'].unique(), df['Estado Civil'].unique()) # Seleção de estados civis
df_filtrado = df_filtrado[df_filtrado['Estado Civil'].isin(estado_civil_selecionado)]   # Filtrar o DataFrame

# Atualizar gráficos com base nos filtros
genero = df_filtrado['Gênero'].value_counts()   # Contagem de gêneros
linguagem = df_filtrado["Linguagem Fluente"].value_counts() # Contagem de linguagens
cargo = df_filtrado["Cargo Atual"].value_counts() # Contagem de cargos
religiao = df_filtrado["Religião"].value_counts()   # Contagem de religiões
estado_de_saude = df_filtrado["Estado de Saúde"].value_counts() # Contagem de estados de saúde
Estado_Civil = df_filtrado["Estado Civil"].value_counts() # Contagem de estados civis

st.write("Gráfico de Gêneros:") # Título do gráfico
st.bar_chart(genero) # Gráfico de barras de gêneros

st.write("Contagem por Cargo") # Título do gráfico
st.line_chart(cargo) # Gráfico de linha de cargos com cor vermelha
st.write("Salário Mensal") # Título do gráfico


# Gráfico de área de salários

st.write("Linguagem Fluente") # Título do gráfico
st.area_chart(linguagem) # Gráfico de área de linguagens

st.write("Religião") # Título do gráfico
st.line_chart(religiao) # Gráfico de linha de religiões

st.write("Estado de Saúde") # Título do gráfico
st.area_chart(estado_de_saude) # Gráfico de área de estados de saúde

st.write("Estado Civil") # Título do gráfico
st.bar_chart(Estado_Civil) # Gráfico de barras de estados civis