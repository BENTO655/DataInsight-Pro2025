import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

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
fig1, ax1 = plt.subplots()
vendas_produto.plot(kind='bar', ax=ax1)
ax1.set_ylabel('Total de Vendas')
st.pyplot(fig1)

# Gráfico 2: Vendas por Região
st.subheader('Vendas por Região')
vendas_regiao = df.groupby('Regiao')['Total_Venda'].sum()
fig2, ax2 = plt.subplots()
vendas_regiao.plot(kind='bar', ax=ax2)
ax2.set_ylabel('Total de Vendas')
st.pyplot(fig2)

# Gráfico 3: Quantidade Vendida por Data
st.subheader('Quantidade Vendida por Data')
fig3, ax3 = plt.subplots()
df.groupby('Data')['Quantidade'].sum().plot(ax=ax3)
ax3.set_ylabel('Quantidade Vendida')
st.pyplot(fig3)

# Gráfico 4: Preço Médio por Produto
st.subheader('Preço Médio por Produto')
preco_medio_produto = df.groupby('Produto')['Preco_Unitario'].mean()
fig4, ax4 = plt.subplots()
preco_medio_produto.plot(kind='bar', ax=ax4)
ax4.set_ylabel('Preço Médio')
st.pyplot(fig4)