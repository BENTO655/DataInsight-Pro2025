import streamlit as st
import pandas as pd
import numpy as np

# Gerando os dados
data = {
    'Data': pd.date_range(start='2024-01-01', end='2024-12-31', freq='D'),
    'Produto': np.random.choice(['Camiseta', 'Calça', 'Tênis', 'Boné'], 366),
    'Quantidade': np.random.randint(1, 20, 366),
    'Preco_Unitario': np.random.uniform(20, 150, 366),
    'Regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], 366)
}
df = pd.DataFrame(data)
df['Total_Venda'] = df['Quantidade'] * df['Preco_Unitario']

# Configurando o Streamlit
st.title('Dashboard de Vendas')

# Gráfico 1: Vendas por Produto
st.subheader('Vendas por Produto')
vendas_produto = df.groupby('Produto')['Total_Venda'].sum()
st.bar_chart(vendas_produto)

# Gráfico 2: Vendas por Região
st.subheader('Vendas por Região')
vendas_regiao = df.groupby('Regiao')['Total_Venda'].sum()
st.bar_chart(vendas_regiao)

# Gráfico 3: Quantidade Vendida por Data
st.subheader('Quantidade Vendida por Data')
quantidade_vendida_por_data = df.groupby('Data')['Quantidade'].sum()
st.line_chart(quantidade_vendida_por_data)

# Gráfico 4: Preço Médio por Produto
st.subheader('Preço Médio por Produto')
preco_medio_produto = df.groupby('Produto')['Preco_Unitario'].mean()
st.bar_chart(preco_medio_produto)
