import pandas as pd

notas = pd.Series([10, 8, 7, 9])

# Média das notas do aluno:
media = notas.mean()

# Somando as notas do aluno:
soma = notas.sum()

# Desvio padrão das notas do aluno:
desvio = notas.std()

# Quantidade de notas do aluno:
quantidade = notas.count()

# Cria um dataframe com as informações dos alunos:
df = pd.DataFrame(
    {
        'Aluno':    ['João', 'Maria', 'José', 'Pedro'],
        'Prova':    [10, 8, 7, 9],
        'Faltas':   [2, 3, 0, 1]
    })

# Localiza as notas do aluno:
aluno = df.loc[df['Aluno'] == 'João']

# Tipo de dados do dataframe:
tipo_dados = df.dtypes

# Retorna a prova com notas maiores que 7:
maiores_notas = df[df['Prova'] > 7]

# Lendo arquivos CSV
csv = pd.read_csv('base/AAPL.csv', sep=',')

# Exibe as 10 primeiras linhas do arquivo:
selecao = csv.head(10)

# Exibe os dados dos últimos 7 dias:
intervalo = csv.tail(7)

# Média dos 7 dias:
media_dias = csv.tail(7)[['Adj Close']].mean()

# Descrição do arquivo:
descricao = csv.describe()