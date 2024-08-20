import requests

# Defina as variáveis necessárias
empresa = "Grupo Soma"  # Nome da empresa
app_name = "api"  # Substitua pelo nome do app criado
username = "guilherme.villas@somagrupo.com.br"  # Substitua pelo seu nome de usuário
app_password = "778B749C41FF44738D9649971AA56023214595DFC1C84D5FABE70DFAE8D0E028"  # Substitua pela senha vinculada ao app

# URL do endpoint de token
url = f"https://scorb.com.br/token?empresa={empresa}&app={app_name}"

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

# Corpo da requisição
data = {
    "grant_type": "password",
    "username": username,
    "password": app_password
}

# Fazendo a requisição POST para obter o token
response = requests.post(url, headers=headers, data=data)

# Verificando a resposta
if response.status_code == 200:
    # Extraindo o token da resposta
    token_data = response.json()
    bearer_token = token_data.get("access_token")
    print("Bearer Token:", bearer_token)
else:
    print("Erro ao obter o token:", response.status_code, response.text)
