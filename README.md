# Tratamento e limpeza do Dataset de Queimadas na Amazonia
## Objetivo
#### Este projeto tem como objetivo aplicar práticas de engenharia de dados no tratamento, padronização e armazenamento de dados relacionados às queimadas na região Amazônica do Brasil. Os dados utilizados foram obtidos em formato CSV e passaram por um processo de limpeza para posterior uso em análises e visualizações.
## Etapas do Projeto
### Carregamento dos Dados

##### - Leitura de um dataset contendo informações sobre queimadas no Brasil, com codificação latin1.

### Limpeza de Dados

##### - Identificação e remoção de linhas duplicadas.

##### - Verificação de valores nulos.

##### - Renomeação de colunas para padronização e clareza semântica.

### Armazenamento

##### - Salvamento dos dados tratados em um novo arquivo .csv (amazon_clean.csv), preparado para consumo por ferramentas de análise ou visualização.

##### - Pré-Agrupamentos (opcional para visualização)

##### - Geração de médias de queimadas por ano, estado e mês.

##### - Exportação dos resultados para arquivos CSV separados na pasta data_visualization/.

### Tecnologias Utilizadas
##### - Python
##### - Pandas
