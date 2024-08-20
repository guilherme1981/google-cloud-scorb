import logging
import re
import pandas as pd
from google.cloud import bigquery

# Configuração do logging
logging.basicConfig(level=logging.INFO)

OSCORB_CCOMD_QUERY = """
        SELECT 
      C.NRO_CCOMD AS CENTRO_DE_CUSTO,
      C.CC_OMD AS DESCRICAO,
      C.BP AS BP_RESPONSAVEL,
      C.CANAL,
      C.CAPEX,
      C.DIRETORIA
FROM 
    `elm_gold_zone.CCOMD` C
    """

def query_ccomd_table(bq_client, query: str) -> pd.DataFrame:
    try:
        query_job = bq_client.query(query)
        df = query_job.result().to_dataframe()
        logging.info(
            f"Consulta do CCOMD foi bem sucedida. Total de linhas: {len(df.index)}"
        )
    except Exception as error:
        logging.error(f"Erro ao consultar API do BQ: {error}")
        raise error
    return df

# Configura o cliente BigQuery
bq_client = bigquery.Client()

# Executa a função
df_ccomd = query_ccomd_table(bq_client, OSCORB_CCOMD_QUERY)

# Exibe as primeiras linhas do DataFrame retornado
print(df_ccomd.head())

#teste do git
