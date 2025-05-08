import pandas as pd
from pandas import value_counts


## Lendo dataset.
df_amazon = pd.read_csv('../data/amazon.csv', encoding='latin1')
df_clean = pd.read_csv('../data/amazon_clean.csv', encoding='latin1')
# print(df_amazon)


def verifica_duplicados(df):
    ## Operação para remover linhas duplicadas.
    total_duplicados = df[df.duplicated(keep=False)]  # Visualiza linhas duplicadas.
    # print(total_duplicados)
    df_amazon_clean = df.drop_duplicates()  # Remove as linhas duplicadas.
    # print(df_amazon)
    print(f'Duplicatas removidas: {len(df) - len(df_amazon_clean)}')  # Calcula as linhas duplicadas removidas.
    return df_amazon_clean

def verifica_nulos(df):
    nulos = df.isnull().sum()
    return nulos
    # Conclusão: Não existe valores nulos.

def ajusta_colunas(df):
    ## Ajuste de colunas
    df.rename(columns={
        'number':'Numeros de queimadas',
        'year':'Ano',
        'month':'Mes',
        'date':'Data',
        'state':'Estado'
    }, inplace=True)

def converte_tipo(df):
    # Conversão de tipos
    df['Numeros de queimadas'] = df['Numeros de queimadas'].astype(int)
    df['Data'] = pd.to_datetime(df['Data'])

def cria_arquivo_csv(df):
    df_amazon_clean = df.to_csv('../data/amazon_clean.csv')  # criando um arquivo com dados atualizados (limpos)
    return df_amazon_clean


df_amazon = verifica_duplicados(df_amazon)
verifica_nulos(df_amazon)
ajusta_colunas(df_amazon)
converte_tipo(df_amazon)
cria_arquivo_csv(df_amazon)
print(df_clean)

