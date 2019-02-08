from repositorios import cliente_repositorio, pedido_repositorio, produto_repositorio
from entidades import cliente, produto
from fabricas import fabrica_conexao

opc_menu = 1

while opc_menu != 0:
    print("{:-^30}".format("Menu"))
    print("1. Cliente")
    print("2. Produtos")
    print("3. Pedido")
    print("0. Sair")
    print("{:-^30}".format(""))
    opc_menu = int(input("Digite a opção desejada: "))

    if opc_menu == 1:
        print("{:-^30}".format("Menu"))
        print("1. Inserir Cliente")
        print("2. Editar Cliente")
        print("3. Remover Cliente")
        print("4. Listar todos os Clientes")
        print("5. Listar Cliente por ID")
        print("6. Listar Cliente(s) por nome")
        print("7. Listar Clientes ordenados")
        print("0. Voltar")
        print("{:-^30}".format(""))
        opc_cliente = int(input("Digite a opção desejada: "))

        if(opc_cliente == 1):
            fabrica = fabrica_conexao.ConexaoDB()
            sessao = fabrica.criar_sessao()
            try:
                nome_cliente = input("Digite o nome do cliente: ")
                idade_cliente = int(input("Digite a idade do cliente: "))
                novo_cliente = cliente.Cliente(nome_cliente, idade_cliente)
                repositorio = cliente_repositorio.ClienteRepo().inserir(novo_cliente, sessao)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif(opc_cliente == 2):
            fabrica = fabrica_conexao.ConexaoDB()
            sessao = fabrica.criar_sessao()
            try:
                id_cliente = int(input("Digite o id do cliente: "))
                nome_cliente = input("Digite o nome do cliente: ")
                idade_cliente = int(input("Digite a idade do cliente: "))
                novo_cliente = cliente.Cliente(nome_cliente, idade_cliente)
                repositorio = cliente_repositorio.ClienteRepo().alterar(novo_cliente, id_cliente, sessao)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif opc_cliente == 3:
            fabrica = fabrica_conexao.ConexaoDB()
            sessao = fabrica.criar_sessao()
            try:
                id_cliente = int(input("Digite o ID do cliente a ser removido"))
                repositorio = cliente_repositorio.ClienteRepo().excluir(id_cliente, sessao)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif opc_cliente == 4:
            fabrica = fabrica_conexao.ConexaoDB()
            sessao = fabrica.criar_sessao()
            try:
                clientes = cliente_repositorio.ClienteRepo().listar(sessao)
                for i in clientes:
                    print(i)
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif opc_cliente == 5:
            fabrica = fabrica_conexao.ConexaoDB()
            sessao = fabrica.criar_sessao()
            try:
                id_cliente = int(input("Digite o ID do cliente: "))
                cliente = cliente_repositorio.ClienteRepo().listar_cliente(id_cliente, sessao)
                print(cliente)
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif opc_cliente == 6:
            fabrica = fabrica_conexao.ConexaoDB()
            sessao = fabrica.criar_sessao()
            try:
                nome_cliente = input("Digite o nome desejado: ")
                clientes = cliente_repositorio.ClienteRepo().listar_cliente_nome(nome_cliente, sessao)
                for i in clientes:
                    print(i)
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif opc_cliente == 7:
            fabrica = fabrica_conexao.ConexaoDB()
            sessao = fabrica.criar_sessao()
            try:
                nome_cliente = input("Digite o nome desejado")
                clientes = cliente_repositorio.ClienteRepo().listar_cliente_nomes_ordenados(nome_cliente, sessao)

                for i in clientes:
                    print(i)
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        else:
            continue

    elif opc_menu == 2:
        print("{:-^30}".format("Menu"))
        print("1. Inserir Produto")
        print("2. Buscar produto ID")
        print("0. Voltar")
        print("{:-^30}".format(""))
        opc_produto = int(input("Digite a opção desejada: "))

        if opc_produto == 1:
            fabrica = fabrica_conexao.ConexaoDB()
            sessao = fabrica.criar_sessao()
            try:
                descricao_produto = input("Digite a descrição do produto: ")
                valor_produto = float(input("Digite o valor do produto: "))
                novo_produto = produto.Produto(descricao_produto, valor_produto)
                repositorio = produto_repositorio.ProdutoRepo().inserir_produto(novo_produto, sessao)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif opc_produto == 2:
            fabrica = fabrica_conexao.ConexaoDB()
            sessao = fabrica.criar_sessao()
            try:
                produto_id = int(input("Digite o id do produto"))
                novo_produto = produto_repositorio.ProdutoRepo().listar_produto_id(produto_id, sessao)
                print(novo_produto)
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()


        elif opc_produto == 0:
            continue
        else:
            print("Valor inválido!")

    elif opc_menu == 3:
        print("{:-^30}".format("Menu"))
        print("1. Inserir Pedido")
        print("2. Listar pedidos")
        print("0. Voltar")
        print("{:-^30}".format(""))
        opc_pedido = int(input("Digite a opção desejada: "))

        if opc_pedido == 1:
            fabrica = fabrica_conexao.ConexaoDB()
            sessao = fabrica.criar_sessao()
            try:
                lista_produtos = []
                while True:
                    print("1. inserir Produto")
                    print("0. Voltar")
                    opc_pedido_produto = int(input("Digite a opção desejada: "))

                    if opc_pedido_produto == 1:
                        id_produto = int(input("Digite o id deste produto: "))
                        lista_produtos.append(id_produto)
                    elif opc_pedido_produto == 0:
                        break
                id_cliente = int(input("Digite o id do cliente a ser relacionado com pedido"))
                repositorio_pedido = pedido_repositorio.PedidoRepo().inserir_pedido(id_cliente, sessao, lista_produtos)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif opc_pedido == 2:
            fabrica = fabrica_conexao.ConexaoDB()
            sessao = fabrica.criar_sessao()
            try:
                repositorio_pedido = pedido_repositorio.PedidoRepo().listar_pedidos(sessao)
                for i in repositorio_pedido:
                    print(i, i.produtos)
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()
        elif opc_pedido == 0:
            continue
        else:
            print("Opção Inválidade")


    else:
        print("Opção incorreta!!")