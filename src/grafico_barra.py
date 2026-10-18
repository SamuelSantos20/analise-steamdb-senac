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
	SELECT YEAR(data_lancamento), COUNT(*)
	FROM jogos
	GROUP BY YEAR(data_lancamento)
	ORDER BY YEAR(data_lancamento);
''')

resultados = cursor.fetchall()

anos = [linha[0] for linha in resultados]
quantidades = [linha[1] for linha in resultados]

plt.bar(anos, quantidades)
plt.xlabel('ANO DE LANÇAMENTO')
plt.ylabel('JOGOS LANÇADOS')
plt.title('N. DE LANÇAMENTOS POR ANO')
plt.show()
