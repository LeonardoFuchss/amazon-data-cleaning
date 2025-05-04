import pandas as pd

def load_path(filepath):
    return pd.read_csv(filepath, encoding='latin1')

def duplicate_rows(df): # Visualiza linhas duplicadas.
    duplicated = df[df.duplicated()]
    return duplicated

def remove_duplicate_rows(df):
    remove = df.drop_duplicates()
    return remove

def show_duplicates_removed(df_original, df_amazon_clean):
    show = len(df_original) - len(df_amazon_clean)
    return show

def show_null_values(df):
    nulos = df.isnull().sum()
    return nulos

def rename_columns(df):
    return df.rename(columns={
        'number': 'Numeros de queimadas',
        'year': 'Ano',
        'month': 'Mes',
        'date': 'Data',
        'state': 'Estado'
    })

# Atribuindo os dados atualizados em um novo arquivo.
def dataset_clean(df, filepath): # Objetivo: Salvar o dataframe atualizado.
    df.to_csv(filepath, index=False) # Cria um novo arquivo, dentro do path definido.
    print(f'Dados salvos em {filepath}') # Show path



if __name__ == '__main__':
    # Carregamento de dados originais
    df_amazon_original = load_path('../data/amazon.csv')

    # Tratamento de duplicatas
    print('Linhas duplicadas:')
    print(duplicate_rows(df_amazon_original))
    df_original_clean = remove_duplicate_rows(df_amazon_original) # Remove linhas duplicadas (atualiza df original)

    # Valores nulos
    print('Valores nulos:')
    print(show_null_values(df_amazon_original))

    df_original_clean = rename_columns(df_original_clean) # Renomeando colunas (Atualizando df original)

    dataset_clean(df_original_clean, '../data/amazon_clean.csv') # Criando um novo dataframe com os dados limpos (atualizados)
    df_data_clean = load_path('../data/amazon_clean.csv') # Lendo esse novo dataframe

    print('Linhas duplicadas removidas:')
    print(show_duplicates_removed(df_amazon_original, df_data_clean)) # Total de linhas duplicadas removidas.




# O que faltaria para um cenário mais "profissional"?
# Uso de logging ao invés de print()
#
# Tratamento de erros (try/except)
#
# Uso de argparse para passar caminhos por linha de comando
#
# Testes automatizados (com pytest, por exemplo)
#
# Deploy do script em pipelines com Airflow, Luigi ou similar

