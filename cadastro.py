import sqlite3 as conector

conexao = conector.connect("fabrica543.db")
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS devs (id_dev INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome VARCHAR(60), area_atuacao varchar(200), telefone varchar(14))""")

cursor.execute("""INSERT INTO devs (nome,area_atuacao,telefone) VALUES ('Joaozinho', 'Analista de dados', '6788888888')""")

nomeDev = input(" Nome do Desenvolvedor \n")
area = input("Digite  area de atuação do Desenvolvedor \n ")
tel = input("Digite o numero de telefone do Desenvolvedor \n")
cursor.execute("""INSERT INTO devs (nome,area_atuacao,telefone) VALUES (?,?,?)""", (nomeDev,area,tel))

cursor.execute("""SELECT * FROM devs""")
dado = cursor.fetchall()
for desenvolvedores in dado:
    print(desenvolvedores)









conexao.commit()