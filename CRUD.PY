import sqlite3 as conector

conexao = conector.connect("fabrica543.db")
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS devs (id_dev INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome VARCHAR(60), area_atuacao varchar(200), telefone varchar(14))""")





conexao.commit()

def cadastrar():
    cursor.execute("""INSERT INTO devs (nome,area_atuacao,telefone) VALUES ('Joaozinho', 'Analista de dados', '6788888888')""")

    nomeDev = input(" Nome do Desenvolvedor \n")
    area = input("Digite  area de atuação do Desenvolvedor \n ")
    tel = input("Digite o numero de telefone do Desenvolvedor \n")
    cursor.execute("""INSERT INTO devs (nome,area_atuacao,telefone) VALUES (?,?,?)""", (nomeDev,area,tel))

    conexao.commit()

    print("cadastro realizado com sucesso!")

def listar():
    cursor.execute("""SELECT * FROM devs""")
    dado = cursor.fetchall()

    if not dado:
        print("nenhum dev cadastrado.")
        return
    print("\n LISTA DE DEVS")

    for desenvolvedores in dado:
        print(f"ID: {desenvolvedores[0]} | NOME: {desenvolvedores[1]}| Area de Atuação: {desenvolvedores[2]}| Telefone: {desenvolvedores[3]}")
def atualizar():
    listar()
    id_dev = int(input("\n DIGITE O ID DE DEV QUE DESEJA ATUALIZAR :"))
    nomeDev = input("Novo nome : ")
    atuacao = input("Nova area de atuação: ")
    tel = input('Novo telefone:')

    cursor.execute("""UPDATE devs SET nome = ?, area_atuacao = ?, telefone = ? WHERE id_dev = ?""", (nomeDev, atuacao, tel))

    conexao.commit()

    print("Dados atualizados com sucesso!")

def deletar():
    listar()
    id_dev = int(input("\n Digite o ID do usaurio que deseja deletar "))

    cursor.execute("""DELETE FROM devs WHERE id_dev =?""", (id_dev,))
    conexao.commit()

    print("\nUsuario deletado com sucesso!")

def menu():
    while True:
        print("\n==== MENU ====")
        print("1 - Cadastrar DEV")
        print("2 - lISTAR DEVS")
        print("3 - Atualizar DEV")
        print("4 - Deletar DEV")
        print("5 - Sair")

        op = int(input("Digite sua escolha :"))

        match op:
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                atualizar()
            case 4:
                deletar()
            case 5:
                print("Tchau.... O bar estar aberto....")
            case _:
                print("ERROR 404")

menu()

conexao.close()