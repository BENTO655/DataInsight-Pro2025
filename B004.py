import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st

# 1. Criando dados fictícios de vendas
data = {
    'Data': pd.date_range(start='2024-01-01', end='2024-12-31', freq='D'),
    'Produto': np.random.choice(['Camiseta', 'Calça', 'Tênis', 'Boné'], 366),
    'Quantidade': np.random.randint(1, 20, 366),
    'Preco_Unitario': np.random.uniform(20, 150, 366),
    'Regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], 366)
}

# Criando DataFrame
df = pd.DataFrame(data)
df['Valor_Total'] = df['Quantidade'] * df['Preco_Unitario'] # Adicionando coluna de valor total
df['Mes'] = df['Data'].dt.month_name() # Adicionando coluna de mês

# 2. Preparando os dados para os gráficos
vendas_por_produto = df.groupby('Produto')['Valor_Total'].sum().reset_index()
vendas_por_mes = df.groupby('Mes')['Valor_Total'].sum().reset_index()
vendas_por_regiao = df.groupby('Regiao')['Valor_Total'].sum().reset_index()

# 3. Criando subplots para exibir todos os gráficos na mesma página
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Vendas por Produto', 'Vendas por Mês', 
                    'Distribuição de Preços', 'Vendas por Região'),
    specs=[[{'type': 'xy'}, {'type': 'xy'}],
           [{'type': 'xy'}, {'type': 'domain'}]]
)

# Gráfico 1: Vendas por Produto (Barra)
bar_trace = px.bar(vendas_por_produto, x='Produto', y='Valor_Total').data[0]
fig.add_trace(bar_trace, row=1, col=1)

# Gráfico 2: Vendas por Mês (Linha)
line_trace = px.line(vendas_por_mes, x='Mes', y='Valor_Total').data[0]
fig.add_trace(line_trace, row=1, col=2)

# Gráfico 3: Distribuição de Preços por Produto (Box)
box_traces = px.box(df, x='Produto', y='Preco_Unitario').data
for trace in box_traces:
    fig.add_trace(trace, row=2, col=1)

# Gráfico 4: Vendas por Região (Pizza)
pie_trace = px.pie(vendas_por_regiao, values='Valor_Total', names='Regiao').data[0]
fig.add_trace(pie_trace, row=2, col=2)

# 4. Personalizando o layout
fig.update_layout(
    height=800, 
    width=1000,
    title_text="Análise de Vendas 2024 - Dashboard Interativo",
    showlegend=True
)

# Atualizando eixos
fig.update_xaxes(title_text="Produto", row=1, col=1)
fig.update_xaxes(title_text="Mês", row=1, col=2)
fig.update_xaxes(title_text="Produto", row=2, col=1)
fig.update_yaxes(title_text="Valor Total (R$)", row=1, col=1)
fig.update_yaxes(title_text="Valor Total (R$)", row=1, col=2)
fig.update_yaxes(title_text="Preço Unitário (R$)", row=2, col=1)

# 5. Exibindo o dashboard no Streamlit
st.plotly_chart(fig)
