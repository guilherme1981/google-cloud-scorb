import requests

# URL do endpoint de leitura
url = "https://api.suaurl.com/api/SCORC/crud/AlcanceTipo/read"

# Cabeçalhos da requisição
headers = {
    "Authorization": "A02ZIakGNLC0b2-FrIe2Nem0aUA0AtQwW_07DtFI_pu6UQbkxdzlEzXlgRUv5AyAGzzCjlMLBX5HNn_2z_ONQArxzb_Il1j4HfFxeI7JdwTY_U31h9aCwEq01dUM84hANQCM-lEtvu2aMbXgOimo9TVJM8H4CNDcNuezbgl4br0NEwBg3HTKDybMYOPXXaZnzREcxZ9zjqMFAKP5Hj4WRe0SalYtUL4fIgzuu8Aq03hQuwzF86eFUQAdsw9QO-oOHPD1dSf5CjRhbZwyxIE6TQ",  
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Corpo da requisição, ajustado para não trazer a descrição
data = {
    "Nome": "Guilherme",  # Substitua por um valor específico se necessário
    "Descrição": False,  # Não trazer a descrição
    "Posição": True,
    "ID Posição": True,
    "C.C. Código": True,
    "Expressão": True,
    "Expressão - Valor": "valor_desejado",
    "Status da Posição": True,
    "Promoção": True,
    "Período - Real": True,
    "Período - Projetado": True,
    "Tabela": True,
    "Empresa": True,
    "Divisão": True,
    "Localidade": True,
    "Centro de Custo": True,
    "Grupo C. C.": True
}

# Fazendo a requisição POST para o endpoint de leitura
response = requests.post(url, headers=headers, json=data)

# Verificando a resposta
if response.status_code == 200:
    # Extraindo e imprimindo os dados recebidos
    response_data = response.json()
    print("Dados recebidos:", response_data)
else:
    print("Erro ao realizar a leitura:", response.status_code, response.text)
