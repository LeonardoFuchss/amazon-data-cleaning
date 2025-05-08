import pandas as pd
from pandas import value_counts

## Lendo dataset.
df_amazon = pd.read_csv('../data/amazon_clean.csv', encoding='latin1')
# print(df_amazon)

## Estatísticas
def media_incendios_por_ano():
    # Média de queimaduras por ano:
    media_por_ano = df_amazon.groupby('Ano')['Numeros de queimadas'].mean()
    media_por_ano = media_por_ano.round().sort_values(ascending=False)
    return media_por_ano

def media_incendios_por_estado():
    # Média de queimaduras por ano:
    media_por_estado = df_amazon.groupby('Estado')['Numeros de queimadas'].mean()
    media_por_estado = media_por_estado.round().sort_values(ascending=False)
    return media_por_estado


print(media_incendios_por_ano())
print("-----------------------")
print(media_incendios_por_estado())
