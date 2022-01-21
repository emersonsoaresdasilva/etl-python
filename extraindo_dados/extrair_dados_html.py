import pandas as pd

url = 'https://www.contextures.com/xlsampledata01.html'

tabela = pd.read_html(url)

print(tabela[0])