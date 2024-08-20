import requests

# Suposição: Já temos o token após a autenticação (substitua 'seu_token' pelo token real)
token = "A02ZIakGNLC0b2-FrIe2Nem0aUA0AtQwW_07DtFI_pu6UQbkxdzlEzXlgRUv5AyAGzzCjlMLBX5HNn_2z_ONQArxzb_Il1j4HfFxeI7JdwTY_U31h9aCwEq01dUM84hANQCM-lEtvu2aMbXgOimo9TVJM8H4CNDcNuezbgl4br0NEwBg3HTKDybMYOPXXaZnzREcxZ9zjqMFAKP5Hj4WRe0SalYtUL4fIgzuu8Aq03hQuwzF86eFUQAdsw9QO-oOHPD1dSf5CjRhbZwyxIE6TQ"

# Definindo o endpoint
url = f"//api/SCORC/crud/AlcanceTipo/read"

# Cabeçalho da requisição, incluindo o token para autenticação
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Corpo da requisição (exemplo de dados que podem ser enviados)
body =  {
    "Nome": "Guilherme Villas Boas Gabriel",  # Substitua por um valor específico se necessário
    "Descrição": False,
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

# Fazendo a requisição POST para o endpoint
response = requests.post(url, headers=headers, json=body)

# Verificando a resposta
if response.status_code == 200:
    dados = response.json()  # Recebe os dados do Centro de Custo
    print("Dados do Colaborador:", dados)
else:
    print("Erro:", response.status_code, response.text)
