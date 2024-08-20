# Bibliotecas Python
import logging
import os
from typing import Optional

# Bibliotecas GCP
import functions_framework
from google.cloud import bigquery

# Bibliotecas Internas IMPORTAR as bibliotecas



@functions_framework.http
def sync_oscorb(request) -> Optional[tuple]:
    logging.info("Iniciando sincronizacao oscorb.")

    data = request.form or {}
    domain = data.get("domain", "users")
    token = os.getenv("UOL_LMS_TOKEN")

    try:
        bq_client = bigquery.Client()
        uol_service = UolLMS(token)
        if domain == "users":
            query_and_sync_employees(uol_service, bq_client)
        elif domain == "teams":
            query_and_sync_teams(bq_client, uol_service)
        else:
            logging.error(f"Domínio {domain} inválido.")
            raise ValueError(f"Domínio {domain} inválido.")
        return (f"AÇÃO {domain}: sincronização realizada com sucesso.", 200)
    except Exception as error:
        logging.error(f"Erro ao sincronizar dados: {error}")
        return (f"AÇÃO {domain}: Erro ao sincronizar dados: {error}", 500)
