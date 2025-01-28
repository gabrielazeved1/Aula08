# Projeto ETL com Pandas, Pandera e Poetry

Este é um projeto Python que implementa um processo de **ETL** (Extração, Transformação e Carregamento) utilizando as bibliotecas **Pandas**, **Pandera**, e gerenciado com **Poetry**. O objetivo deste projeto é processar diversos arquivos **JSON**, transformá-los em um **DataFrame** e realizar as transformações necessárias antes de carregá-los para um formato desejado (como CSV ou Parquet).

## Tecnologias Utilizadas

- **Python 3.11**: A versão do Python utilizada no projeto.
- **Poetry**: Gerenciador de dependências e ambiente virtual para o Python.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Pandera**: Biblioteca para validação de esquemas de DataFrames (usada para validar os dados transformados).
- **JSON**: Formato dos arquivos de entrada.

## Funcionalidades

- **Extração (Extract)**: O projeto lê arquivos **JSON** localizados em um diretório especificado.
- **Transformação (Transform)**: Os dados extraídos são convertidos para **DataFrame** e transformados utilizando o Pandas.
- **Validação**: Utilizando o Pandera, o esquema dos dados é validado para garantir que atendem aos requisitos do projeto.
- **Carregamento (Load)**: Os dados transformados podem ser salvos em formatos como **CSV** ou **Parquet**.