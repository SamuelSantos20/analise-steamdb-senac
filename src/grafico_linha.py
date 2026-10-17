import polars as pl
import mysql.connector
import matplotlib.pyplot as plt

conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'steamdb'
)

cursor = conexao.cursor()





cursor.execute('''
	SELECT
		YEAR(data_lancamento) AS ano,
		preco
	FROM jogos
''')

dados = cursor.fetchall()

df = pl.DataFrame(
	dados,
	schema = cursor.column_names,
	orient = 'row'
)

medianas = (
	df
	.group_by("ano")
	.agg(
		pl.col("preco").median().alias('mediana_preco')
	)
	.sort('ano')
)

plt.figure(figsize = (10, 5))

plt.plot(
	medianas['ano'].to_list(),
	medianas['mediana_preco'].to_list(),
	marker = 'o'
)

plt.xlabel("ANO")
plt.ylabel("MEDIANA DE PREÇO")
plt.title("MEDIANA DE PREÇO POR ANO")
plt.grid(True)
plt.tight_layout()
plt.show()

cursor.close()
conexao.close()