import pandas as pd
import streamlit as st
import numpy as np

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
st.subheader('Histograma')
if pd.api.types.is_numeric_dtype(df[coluna]):
    st.bar_chart(df[coluna].value_counts())
else:
    st.write("A coluna selecionada não é numérica e não pode ser exibida como histograma.")

# Criar gráfico de dispersão
st.subheader('Gráfico de Dispersão')
st.write("Gráfico de Dispersão entre Data e Quantidade")
st.line_chart(df.set_index('Data')['Quantidade'])

# Criar gráfico de barras
st.subheader('Gráfico de Barras')
bar_data = df.groupby(['Produto', 'Regiao'])['Quantidade'].sum().unstack().fillna(0)
st.bar_chart(bar_data)

# Criar gráfico de linha com média móvel de 7 dias
st.subheader('Gráfico de Linha com Média Móvel de 7 Dias')
line_data = df.pivot(index='Data', columns='Produto', values='Preco_Unitario')
line_data_ma = line_data.rolling(window=7).mean()
st.line_chart(line_data_ma)
