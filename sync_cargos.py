import logging
import re
import pandas as pd
from google.cloud import bigquery

# Configuração do logging
logging.basicConfig(level=logging.INFO)

OSCORB_CARGOS_QUERY = """
    SELECT 
        C.CARGO,
        C.TIPO_CARGO,
        C.GRADE,
        C.COTA_JA,
        C.TARGET,
        C.PIPELINE
 FROM `somageg.elm_silver_zone.DEPARA_CARGO` C
    """

def query_CARGOS_table(bq_client, query: str) -> pd.DataFrame:
    try:
        query_job = bq_client.query(query)
        df = query_job.result().to_dataframe()
        logging.info(
            f"Consulta do Deparacargo foi bem sucedida. Total de linhas: {len(df.index)}"
        )
    except Exception as error:
        logging.error(f"Erro ao consultar API do BQ: {error}")
        raise error
    return df

# Configura o cliente BigQuery
bq_client = bigquery.Client()

# Executa a função
df_cargos = query_CARGOS_table(bq_client, OSCORB_CARGOS_QUERY)

# Exibe as primeiras linhas do DataFrame retornado
print(df_cargos.head())