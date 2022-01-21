import pandas as pd

from sqlalchemy import create_engine

compras = pd.read_excel('base/compras_ajustado.xlsx')

engine = create_engine('sqlite:///base/compras.db')

compras.to_sql('compras', con=engine)

engine.execute('SELECT * FROM compras').fetchall()

print(pd.read_sql_query('SELECT * FROM compras', engine))