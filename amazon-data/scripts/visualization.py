import pandas as pd
from pandas import value_counts

## Lendo dataset.
df_amazon = pd.read_csv('../data/amazon_clean.csv', encoding='latin1')
print(df_amazon)

## Estatísticas
def media_incendios_por_ano():
    # Média de queimadas por ano:
    media_ano = df_amazon.groupby('Ano')['Numeros de queimadas'].mean().round() # Quando esse groupby é feito, é criado uma serie (ano(index) -> media(valor))
    media_ano = media_ano.sort_index(ascending=False) # Ordenamos pelo index, pois queremos ordenar pelo ano, e como foi dito anteriormente, o ano é o index.
    media_ano.to_csv('../data/data_visualization/media_por_ano.csv')
    return media_ano

def media_incendios_por_estado():
    # Média de queimadas por ano:
    media_por_estado = df_amazon.groupby('Estado')['Numeros de queimadas'].mean()
    media_por_estado = media_por_estado.round().sort_values(ascending=False)
    media_por_estado.to_csv('../data/data_visualization/media_por_estado.csv')
    return media_por_estado

def media_por_mes():
    # Média de queimadas por mês:
    ordem_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                   'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    media_mes = df_amazon.groupby('Mes')['Numeros de queimadas'].mean().round()
    media_mes = media_mes.reindex(ordem_meses)
    media_mes.to_csv('../data/data_visualization/media_por_mes.csv')
    return media_mes

print(media_por_mes())




# print(media_incendios_por_ano())
# print("-----------------------")
# print(media_incendios_por_estado())
