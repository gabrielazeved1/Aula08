import pandas as pd
import os 
import glob  

""""
1 funcao de extract que le e consolida os json 

1 funcao que transforma 

1 funcao que da load em csv ou parquet


"""


def extrair_dados(pasta:str) -> pd.DataFrame:
    #buscando todos os arquivos JSON dentro de uma pasta específica.
    arquivos_json = glob.glob(os.path.join(pasta,'*.json'))

    #transformando arquivos em dt
    df_list = [pd.read_json(i) for i in  arquivos_json]
    #concatenar dataframe
    df_total = pd.concat(df_list,ignore_index=True)
    return df_total

#funcao que transforma
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df ["Total"] = df[ "Quantidade"] * df[ "Venda"]
    return df

# print (calcular_kpi_de_total_de_vendas(data_frame))

# carregar dados (load) ou csv ou parquet
# parametro que vai ser ou csv ou parquet
def carregar_dados(df: pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if formato == 'csv': 
            df.to_csv("dados.csv")
        if formato == 'parquet':
            df.to_parquet("dados.parquet")
            return
        


def pipeline_calcular_kpi_de_vendas_consolidades(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado,formato_de_saida)