import pandas as pd
import streamlit as st
import plotly.express as px

# Carregar o arquivo Excel
df = pd.read_excel('vendas_45000_linhas.xlsx')

# Título do dashboard
st.title('Dashboard de Análise de Vendas')

# Estatísticas descritivas
st.header('Estatísticas Descritivas')
st.write(df.describe())

# Filtros interativos
st.sidebar.header('Filtros')
categoria = st.sidebar.multiselect('Categoria', df['Categoria'].unique(), default=df['Categoria'].unique())
regiao = st.sidebar.multiselect('Região', df['Região'].unique(), default=df['Região'].unique())
faixa_etaria = st.sidebar.multiselect('Faixa Etária', df['Faixa Etária'].unique(), default=df['Faixa Etária'].unique())
sexo = st.sidebar.multiselect('Sexo', df['Sexo'].unique(), default=df['Sexo'].unique())
estado_civil = st.sidebar.multiselect('Estado Civil', df['Estado Civil'].unique(), default=df['Estado Civil'].unique())

# Aplicar filtros
df_filtered = df[(df['Categoria'].isin(categoria)) & 
                 (df['Região'].isin(regiao)) & 
                 (df['Faixa Etária'].isin(faixa_etaria)) & 
                 (df['Sexo'].isin(sexo)) & 
                 (df['Estado Civil'].isin(estado_civil))]

# Análise de vendas por categoria
st.header('Vendas por Categoria')
vendas_categoria = df_filtered.groupby('Categoria')['Valor Total'].sum().reset_index()
fig_categoria = px.bar(vendas_categoria, x='Categoria', y='Valor Total', color='Categoria', title='Vendas por Categoria')
st.plotly_chart(fig_categoria)

# Análise de vendas por região
st.header('Vendas por Região')
vendas_regiao = df_filtered.groupby('Região')['Valor Total'].sum().reset_index()
fig_regiao = px.bar(vendas_regiao, x='Região', y='Valor Total', color='Região', title='Vendas por Região')
st.plotly_chart(fig_regiao)

# Análise de vendas por faixa etária
st.header('Vendas por Faixa Etária')
vendas_faixa_etaria = df_filtered.groupby('Faixa Etária')['Valor Total'].sum().reset_index()
fig_faixa_etaria = px.bar(vendas_faixa_etaria, x='Faixa Etária', y='Valor Total', color='Faixa Etária', title='Vendas por Faixa Etária')
st.plotly_chart(fig_faixa_etaria)

# Análise de vendas por meio de pagamento
st.header('Vendas por Meio de Pagamento')
vendas_meio_pagamento = df_filtered.groupby('Meio de Pagamento')['Valor Total'].sum().reset_index()
fig_meio_pagamento = px.pie(vendas_meio_pagamento, names='Meio de Pagamento', values='Valor Total', title='Vendas por Meio de Pagamento')
st.plotly_chart(fig_meio_pagamento)

# Análise de vendas por sexo
st.header('Vendas por Sexo')
vendas_sexo = df_filtered.groupby('Sexo')['Valor Total'].sum().reset_index()
fig_sexo = px.bar(vendas_sexo, x='Sexo', y='Valor Total', color='Sexo', title='Vendas por Sexo')
st.plotly_chart(fig_sexo)

# Análise de vendas por cliente VIP
st.header('Vendas por Cliente VIP')
vendas_vip = df_filtered.groupby('Cliente VIP')['Valor Total'].sum().reset_index()
fig_vip = px.bar(vendas_vip, x='Cliente VIP', y='Valor Total', color='Cliente VIP', title='Vendas por Cliente VIP')
st.plotly_chart(fig_vip)

# Análise de correlação entre variáveis numéricas
st.header('Matriz de Correlação')
numeric_df = df_filtered.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_df.corr()
fig_corr = px.imshow(correlation_matrix, text_auto=True, title='Matriz de Correlação')
st.plotly_chart(fig_corr)

# Análise de tendências ao longo do tempo
st.header('Tendências de Vendas ao Longo do Tempo')
df_filtered['Data'] = pd.to_datetime(df_filtered['Data'])
vendas_tempo = df_filtered.groupby(df_filtered['Data'].dt.to_period('M'))['Valor Total'].sum().reset_index()
vendas_tempo['Data'] = vendas_tempo['Data'].dt.to_timestamp()
fig_tempo = px.line(vendas_tempo, x='Data', y='Valor Total', title='Tendências de Vendas ao Longo do Tempo')
st.plotly_chart(fig_tempo)

# Análise de sazonalidade
st.header('Sazonalidade das Vendas')
df_filtered['Mes'] = df_filtered['Data'].dt.month
vendas_mes = df_filtered.groupby('Mes')['Valor Total'].sum().reset_index()
fig_mes = px.line(vendas_mes, x='Mes', y='Valor Total', title='Sazonalidade das Vendas')
st.plotly_chart(fig_mes)

# Segmentação de clientes por faixa etária e sexo
st.header('Segmentação de Clientes por Faixa Etária e Sexo')
segmentacao_clientes = df_filtered.groupby(['Faixa Etária', 'Sexo'])['Valor Total'].sum().reset_index()
fig_segmentacao = px.bar(segmentacao_clientes, x='Faixa Etária', y='Valor Total', color='Sexo', barmode='group', title='Segmentação de Clientes por Faixa Etária e Sexo')
st.plotly_chart(fig_segmentacao)

# Análise de vendas por estado civil
st.header('Vendas por Estado Civil')
vendas_estado_civil = df_filtered.groupby('Estado Civil')['Valor Total'].sum().reset_index()
fig_estado_civil = px.bar(vendas_estado_civil, x='Estado Civil', y='Valor Total', color='Estado Civil', title='Vendas por Estado Civil')
st.plotly_chart(fig_estado_civil)

# Análise de distribuição de vendas por faixa etária e sexo
st.header('Distribuição de Vendas por Faixa Etária e Sexo')
dist_vendas = df_filtered[['Faixa Etária', 'Sexo', 'Valor Total']].groupby(['Faixa Etária', 'Sexo']).describe().reset_index()
st.write(dist_vendas)
