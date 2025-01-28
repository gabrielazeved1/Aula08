from etl import pipeline_calcular_kpi_de_vendas_consolidades 


pasta_argumento = 'data'
formato_de_saida: list = [ "parquet"]#arquivo csv ou parquet

pipeline_calcular_kpi_de_vendas_consolidades(pasta_argumento, formato_de_saida)
