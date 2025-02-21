import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
# Criar dados fictícios
data = {
    'Data': pd.date_range(start='2024-01-01', end='2024-12-31', freq='D'),
    'Produto': np.random.choice(['Camiseta', 'Calça', 'Tênis', 'Boné'], 366),
    'Quantidade': np.random.randint(1, 20, 366),
    'Preco_Unitario': np.random.uniform(20, 150, 366),
    'Regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], 366)
}
df = pd.DataFrame(data)

# Título do dashboard
st.title('Dashboard de Análise de Dados')

# Selecionar coluna para visualização
coluna = st.selectbox('Selecione a coluna para visualização', df.columns)

# Criar gráfico de histograma
fig_hist = px.histogram(df, x=coluna)
st.plotly_chart(fig_hist)

# Criar gráfico de dispersão
fig_scatter = px.scatter(df, x='Data', y='Quantidade', color='Produto')
st.plotly_chart(fig_scatter)

# Criar gráfico de barras
fig_bar = px.bar(df, x='Produto', y='Quantidade', color='Regiao', barmode='group')
st.plotly_chart(fig_bar)

# Criar gráfico de linha
fig_line = px.line(df, x='Data', y='Preco_Unitario', color='Produto')
st.plotly_chart(fig_line)