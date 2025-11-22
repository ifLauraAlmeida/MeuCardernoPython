import plotly.express as px
import pandas as pd

# --- SEU CÓDIGO BASE ---
real = float(input('Quanto dinheiro você tem na carteira?: R$'))

# Dicionário com moedas e cotações
cotacoes = {
    'USD': 5.30, 'EUR': 6.12, 'JPY': 0.035, 'GBP': 6.95, 'AUD': 3.45,
    'CAD': 3.77, 'CHF': 6.58, 'CNY': 0.74, 'SEK': 0.55, 'NZD': 3.00
}

# Conversão e print (seu estilo original)
for moeda, valor in cotacoes.items():
    conversao = real / valor
    print(f'Com R$ {real:.2f} você pode comprar {moeda} {conversao:.2f}')

# --- MAPA SIMPLES ---
# DataFrame com países e moedas (precisamos associar cada moeda ao país principal)
dados = {
    'country': ['United States', 'Eurozone', 'Japan', 'United Kingdom',
                'Australia', 'Canada', 'Switzerland', 'China', 'Sweden', 'New Zealand'],
    'currency': list(cotacoes.keys()),
    'rate_brl': list(cotacoes.values())
}

df = pd.DataFrame(dados)

# Cria mapa mundi colorido
fig = px.choropleth(
    df,
    locations='country',
    locationmode='country names',
    color='rate_brl',
    hover_name='currency',
    color_continuous_scale='RdYlGn_r',
    title='Valor do Real em Relação às Principais Moedas (verde = real mais caro)'
)

fig.show()