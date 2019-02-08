import sys
sys.path.insert(0, "..")
from repositorios import cliente_repositorio, produto_repositorio
from db import Pedido
from fabricas import fabrica_conexao
from sqlalchemy.orm import joinedload

class PedidoRepo():

    def inserir_pedido(self, id, sessao, produtos):
        repositorio_cliente = cliente_repositorio.ClienteRepo()
        cliente = repositorio_cliente.listar_cliente(id, sessao)
        novo_pedido = Pedido(cliente=cliente)
        for i in produtos:
            produto = produto_repositorio.ProdutoRepo().listar_produto_id(i, sessao)
            novo_pedido.produtos.append(produto)
        sessao.add(novo_pedido)

    def listar_pedidos(self, sessao):
        pedidos = sessao.query(Pedido).options(joinedload(Pedido.produtos)).all()
        return pedidos


