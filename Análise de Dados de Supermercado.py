import pandas as pd
import plotly.express as px

df = pd.read_csv("MODULO7_PROJETOFINAL_BASE_SUPERMERCADO - MODULO7_PROJETOFINAL_BASE_SUPERMERCADO (1).csv.csv")

df.head()

df.info()
df.describe()
df.isnull().sum()

# Convertendo colunas para numérico (caso necessário)
cols = ['Preco_Normal', 'Preco_Desconto', 'Preco_Anterior', 'Desconto']

for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Removendo valores nulos
df = df.dropna()

# Estatísticas principais da coluna de preço com desconto
media = df['Preco_Desconto'].mean()
mediana = df['Preco_Desconto'].median()
variancia = df['Preco_Desconto'].var()
desvio_padrao = df['Preco_Desconto'].std()

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Variância: {variancia}")
print(f"Desvio padrão: {desvio_padrao}")

categoria_total = df.groupby('Categoria')['Preco_Desconto'].sum().reset_index()

fig = px.bar(
    categoria_total,
    x='Categoria',
    y='Preco_Desconto',
    title='Faturamento por Categoria',
    color='Categoria'
)

fig.show()

fig = px.histogram(
    df,
    x='Preco_Desconto',
    title='Distribuição de Preços com Desconto'
)

fig.show()

fig = px.scatter(
    df,
    x='Preco_Normal',
    y='Preco_Desconto',
    color='Categoria',
    title='Relação entre Preço Normal e Preço com Desconto'
)

fig.show()

top10 = df.sort_values(by='Preco_Desconto', ascending=False).head(10)

fig = px.bar(
    top10,
    x='Preco_Desconto',
    y='title',
    orientation='h',
    title='Top 10 Produtos Mais Caros',
    color='Preco_Desconto'
)

fig.show()