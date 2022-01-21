import requests
import pandas as pd

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'
resultado = requests.get(url)

# Exibe os dados da API dos deputados
deputados = pd.DataFrame(resultado.json()['dados'])

# Quantidade de deputados
deputados.shape

# Exibe os dados
total.head()

# Gastos totais dos deputados
gastos = []
for id in deputados.id:
    url_despesa = 'https://dadosabertos.camara.leg.br/api/v2/'
    url_despesa = url_despesa + 'deputados/'+str(id)+'/despesas?ordem=ASC&ano=2019'
    resposta = requests.get(url_despesa)
    gasto = pd.DataFrame(resposta.json()['dados'])
    gasto['id'] = id
    gastos.append(gasto)

# Transformando os dados
total = pd.concat(gastos)

# Verifica valores ausentes
total.isnull().sum()

# Apaga coluna
del total['dataDocumento']

# Verifica quantas vezes não foram passados valores
total.urlDocumento.value_counts()