import datetime
import mysql.connector
try:
    db_connection = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "",database = "cadastro")
    print('Conectado ao banco de dados!')
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("O banco de dados não existe!")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Nome do usuário ou senha incorretos")
    else:
        print(error)
else:
    db_connection.close()

#Criando o menu
print("=-"*20, "CADASTRO DE CLIENTES", "=-" * 20)
print("""Menu\n
Inserir[1] 
Buscar por CPF:[2] 
Editar[3] 
Excluir[4] 
Sair[5]""")
while (True):
    opcao = str(input("Digite a opção: "))
    if (opcao not in "12345"):
        print("Opção inválida, tente novamente!")

    if (opcao == "5"):
        break
    if (opcao == "1"):
        insertnome = input("Nome do cliente: ")
        insertcpf = str(input("CPF: "))
        insertendereco = input("Endereço: ").strip()
        insertnumero_casa = input("Número: ")
        insertcidade = input("Cidade: ")
        insertestado = input("Estado: ")
        insertpais = (input("País: "))

#Inserindo os dados informados

        cnx = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "",database = "cadastro")
        conectar = cnx.cursor()
        adicionar = ("insert into pessoas"
        "(nome, cpf, endereco, numero_casa, cidade, estado, pais)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        dados_cliente = (insertnome, insertcpf, insertendereco, insertnumero_casa, insertcidade, insertestado, insertpais )
        conectar.execute(adicionar, dados_cliente)
        conectar.close()
        cnx.close()

#Criando a opção buscar
    if (opcao == "2"):
        cpf = str(input("Digite o CPF(somente números):"))
        cnx = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "",database = "cadastro")
        conectar = cnx.cursor()
        buscar = ("select nome, cpf, endereco, numero_casa, cidade, estado, pais from pessoas"
        "where cpf between ({}) and ({}); " .format(cpf,cpf))
        conectar.execute(buscar)
        for (nome, cpf, endereco, numero_casa, cidade, estado, pais) in conectar:
            print("""Nome: {} 
            CPF: {} 
            Endereço: {}, número: {} 
            Cidade: {} 
            Estado: {}  
            País: {}""" .format(nome, cpf, endereco, numero_casa, cidade, estado, pais))
        conectar.close()
        cnx.close()










