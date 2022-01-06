import datetime
import mysql.connector
try:
    db_conection = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "",database = "cadastro")
    print('Conectado ao banco de dados!')
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("O banco de dados não existe!")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Nome do usuário ou senha incorretos")
    else:
        print(error)
else:
    db_conection.close()

#Criando o menu
print("=-"*20, "CADASTRO DE CLIENTES", "=-" * 20)
print("""Menu\n
Inserir[1]
Editar[2]
Excluir[3]
Sair[4]""")
opcao = int(input("Digite a opção: "))
while (True):
    if (opcao == 4):
        break
    if (opcao == 1):
        nome = input("Nome do cliente: ")
        cpf = str(input("CPF: "))
        endereco = input("Endereço: ").strip()
        numero_casa = input("Número: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        pais = (input("País: "))

#Inserindo os dados informados

        cnx = mysql.connector.connect(user = "root", database = "cadastro")
        conectar = cnx.cursor()
        adicionar = ("insert into pessoas"
        "(nome, cpf, endereco, numero_casa, cidade, estado, pais)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        dados_cliente = (nome, cpf, endereco, numero_casa, cidade, estado, pais )
        conectar.execute(adicionar, dados_cliente)
        cursor.close()












