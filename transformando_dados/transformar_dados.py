import pandas as pd

compras = pd.read_excel('base/compras_loja_a.xlsx')

# Retorna as colunas do arquivo
print(compras.columns)

# Retorna a contagem das linhas para cada coluna
print(compras.groupby(['Data', 'Região', 'Representante', 'Item']).count()['Unidade'])

# Remove valores duplicados
print(compras.drop_duplicates())

# Verifica valores ausentes
print(compras.info())
print(compras.isnull().any())

# Informa o número da linha com valores ausentes
print(compras[compras.isnull().any(axis=1)])

# Exclui linhas com valores ausentes
print(compras.drop(45))

# Altera valores da coluna
compras.loc[33, 'Item'] = 'Celular'

# Exibe 10 primeiras linhas
print(compras.head(10))

# Substitui formato da data para o padrão ISO
compras.Data = compras.Data.str.replace('-', '/')
compras.Data = compras.Data.str.replace('//', '/')

# Formata o valor da coluna, substituindo caracteres especiais
preco_ajustado = []
for preco in compras['Preço Unidade']:
    preco_ajustado.append(float(str(preco).replace(';', '.')))
compras['Preço Unidade'] = preco_ajustado

# Exibe os dados do arquivo
print(compras)