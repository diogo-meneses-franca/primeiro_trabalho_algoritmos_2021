import mysql.connector
from mysql.connector import errorcode

try:
    db_connection = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "cadastro")
    print('Conectado ao banco de dados!')
    cursor = db_connection.cursor()                  # CRIAÇÃO DO CURSOR LOGO NO INÍCIO PARA NÃO HAVER DUPLICAÇÕES

                                                                     #Criando o menu
    if(db_connection.is_connected):
        menu = True                       # VARIÁVEL CONTADORA PARA O LAÇO while DO MENU

        while(menu == True):
            print("=-"*20, "CADASTRO DE CLIENTES", "=-" * 20)
            print("""Menu\n
            Inserir[1]
            Consultar[2]
            Editar[3]
            Excluir[4]
            Sair[5]""")
            opcao = int(input(f"\nDigite a opção: "))

            contadora_opcao1 = True               # VARIÁVEL CONTADORA REFERENTE A Inserir[1]
            while (contadora_opcao1 == True):

                if(opcao not in (1, 2, 3, 4, 5)):
                    print(f"\n{'='*20}> OPÇÃO INVÁLIDA, TENTE NOVAMENTE <{'='*20}\n")
                    break

                if (opcao == 5):
                    print(f"\n{'*'*15} Conexão com o Banco de Dados encerrada {'*'*15}")
                    menu = False
                    cursor.close()
                    db_connection.close
                    break                         # QUEBRA O LOOP DO menu

                if (opcao == 1):
                    print(f"\n{'>'*40} CREATE {'<'*40}\n")
                    nome = input("Nome do cliente: ")
                    cpf = str(input("CPF: "))
                    endereco = input("Endereço: ").strip()
                    numero_casa = input("Número: ")
                    cidade = input("Cidade: ")
                    estado = input("Estado: ")
                    pais = (input("País: "))
                                                                        # Inserindo os dados informados
                    adicionar = ("insert into pessoas"
                    "(nome, cpf, endereco, numero_casa, cidade, estado, pais)"
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)")              # SCRIPT EM SQL
                    dados_cliente = (nome, cpf, endereco, numero_casa, cidade, estado, pais )
                    cursor.execute(adicionar, dados_cliente)
                    db_connection.commit()                 # PROPRIEDADE QUE GRAVARÁ OS VALORES EXECUTADOS NO DB
                    print(f"\n{'*'*15} Adicionado {cursor.rowcount} cadastro(s) ao Banco de Dados {'*'*15}\n")         # ESTA PROPRIEDADE RETORNARÁ O Nº DE LINHAS QUE FORAM ADICIONADAS AO DB

                    outro = input("| REALIZAR OUTRO CADASTRO? [S/N] | : ").upper()                   

                    if(outro == 'S'):
                        contadora_opcao1 = True
                    else:
                        contadora_opcao1 = False

                if (opcao == 2):
                    contadora_opcao2 = True               # VARIÁVEL CONTADORA REFERENTE A Consultar[2]
                    while(contadora_opcao2 == True):
                        print(f"\n{'>'*40} READ {'<'*40}\n")
                        cpf = int(input("\nDigite o CPF(somente números): "))
                        buscar = ("SELECT nome, cpf, endereco, numero_casa, cidade, estado, pais FROM pessoas WHERE cpf='%d';" %(cpf))              # SCRIPT EM SQL
                        cursor.execute(buscar)

                        for (nome, cpf, endereco, numero_casa, cidade, estado, pais) in cursor:
                            print(f"Nome: {nome}")
                            print(f"CPF: {cpf}")
                            print(f"Endereço: {endereco}, número: {numero_casa}") 
                            print(f"Cidade: {cidade}") 
                            print(f"Estado: {estado}")  
                            print(f"País: {pais}")
                            
                            outro = input(f"\n| REALIZAR OUTRA CONSULTA? [S/N] | : ")
                            outro = outro.upper()

                            if(outro == 'S'):
                                contadora_opcao2 = True
                            else:
                                contadora_opcao2 = False
                    break                         # QUEBRA O LOOP DO Consultar[2]
                        
                if(opcao == 3):
                    contadora_opcao3 = True               # VARIÁVEL CONTADORA REFERENTE A Editar[3]
                    print(f"\n{'>'*40} UPDATE {'<'*40}\n")
                    consulta = ("SELECT id, nome, cpf, endereco, numero_casa, cidade, estado, pais FROM pessoas;")              # SCRIPT EM SQL
                    cursor.execute(consulta)
                    
                    while(contadora_opcao3 == True):
                        for (id, nome, cpf, endereco, numero_casa, cidade, estado, pais) in cursor:
                            print(f"{'-'*160}\n| ID: {id} | NOME: {nome} | CPF: {cpf} | ENDEREÇO: {endereco} | Nº: {numero_casa} | CIDADE: {cidade} | ESTADO: {estado} | PAÍS: {pais} | \n{'-'*160}")
                        id_update = input("Digite o ID do cadastro que deseja alterar: ")
                        coluna = int(input(f"\n{'='*30} UPDATE {'='*30}\n\nNOME [1] \nCPF[2] \nENDEREÇO [3] \n\nDigite a opção desejada: "))
                        
                        def outra_alteracao():                           # FUNÇÃO RESPOSÁVEL POR PERGUNTAR POR OUTRA ALTERAÇÃO
                            global contadora_opcao3
                            novamente = input("| REALIZAR OUTRA ALTERAÇÃO? [S/N] | : ")
                            novamente = novamente.lower()
                            novamente = input("| REALIZAR OUTRA ALTERAÇÃO? [S/N] | : ").lower()
                            if(novamente == 's'):
                                contadora_opcao3 = True
                            else:
                                contadora_opcao3 = False
                            return contadora_opcao3

                        if(coluna == 1):
                            nome_update = input("\nNOME: ")
                            update = ("UPDATE pessoas SET nome=(%s) WHERE id=(%s)")              # SCRIPT EM SQL
                            dados_update = (nome_update, id_update)
                            cursor.execute(update, dados_update)
                            db_connection.commit()
                            print(f"\n{'*'*15} Alteração realizada com sucesso! {'*'*15}\n")

                            outra_alteracao()

                        elif(coluna == 2):
                            cpf_update = input("\nCPF: ")
                            update = ("UPDATE pessoas SET cpf=(%s) WHERE id=(%s)")              # SCRIPT EM SQL
                            dados_update = (cpf_update, id_update)
                            cursor.execute(update, dados_update)
                            db_connection.commit()
                            print(f"\n{'*'*15} Alteração realizada com sucesso! {'*'*15}\n")

                            outra_alteracao()

                        elif(coluna == 3):
                            endereco_update = input("\nENDEREÇO: ")
                            numero_update = input("\nNº: ")
                            cidade_update = input("\nCIDADE: ")
                            estado_update = input("\nESTADO: ")
                            pais_update = input("\nPAIS: ")
                            update = ("UPDATE pessoas SET endereco=(%s), numero_casa=(%s), cidade=(%s), estado=(%s), pais=(%s) WHERE id=(%s)")              # SCRIPT EM SQL
                            dados_update = (endereco_update, numero_update, cidade_update, estado_update, pais_update, id_update)
                            cursor.execute(update, dados_update)
                            db_connection.commit()
                            print(f"\n{'*'*15} Alteração realizada com sucesso! {'*'*15}\n")

                            outra_alteracao()
                    break                         # QUEBRA O LOOP DO Editar[3]

                if (opcao == 4):
                    contadora_opcao4 = True
                    print(f"\n{'>'*40} DELETE {'<'*40}\n")

                    while(contadora_opcao4 == True):
                        cpf = int(input("Digite o CPF(somente números): "))  
                        deletar = ("delete from pessoas where cpf='%d';" %(cpf))
                        print(f"\n{'*'*15} Dados deletados com sucesso! {'*'*15}\n")
                        cursor.execute(deletar)
                        db_connection.commit()
                        outro = input(f"| REALIZAR OUTRA EXCLUSÃO? [S/N] | : ")
                        outro = outro.upper()

                        if(outro == 'S'):
                            contadora_opcao4 = True
                        else:
                            contadora_opcao4 = False
                    break                         # QUEBRA O LOOP DO Excluir[4]

except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("O banco de dados não existe!")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Nome do usuário ou senha incorretos")
    else:
        print(error)
        db_connection.close()               # CONEXÃO É INTERROMPIDA EM CASO DE ERRO