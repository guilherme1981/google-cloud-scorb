import logging
import re
import pandas as pd
from google.cloud import bigquery

# Configuração do logging
logging.basicConfig(level=logging.INFO)

OSCORB_COLABORADORES_QUERY = """
SELECT 
      CLT.CHAPA,
      CLT.NOME,
      CLT.DT_ADMISSAO,
      CLT.CPF
 FROM `somageg.rm_gold_zone.VW_ATIVOS_CLT` CLT
    """

def query_COLABORADORES_table(bq_client, query: str) -> pd.DataFrame:
    try:
        query_job = bq_client.query(query)
        df = query_job.result().to_dataframe()
        logging.info(
            f"Consulta sobre o ativos foi bem sucedida. Total de linhas: {len(df.index)}"
        )
    except Exception as error:
        logging.error(f"Erro ao consultar API do BQ: {error}")
        raise error
    return df

# Configura o cliente BigQuery
bq_client = bigquery.Client()

# Executa a função
df_clt = query_COLABORADORES_table(bq_client, OSCORB_COLABORADORES_QUERY)

# Exibe as primeiras linhas do DataFrame retornado
print(df_clt.head())