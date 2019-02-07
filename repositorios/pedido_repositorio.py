import sys
sys.path.insert(0, "..")
from repositorios import cliente_repositorio
from db import Pedido
from fabricas import fabrica_conexao

class PedidoRepo():

    def inserir_pedido(self, id, sessao):
        repositorio_cliente = cliente_repositorio.ClienteRepo()
        cliente = repositorio_cliente.listar_cliente(id, sessao)
        novo_pedido = Pedido(cliente=cliente)
        sessao.add(novo_pedido)


