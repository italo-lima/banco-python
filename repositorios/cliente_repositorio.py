import sys
sys.path.insert(0, "..")
from fabricas import fabrica_conexao
from db import Cliente

class ClienteRepo():

    def listar(self, sessao):
        clientes = sessao.query(Cliente).all()
        return clientes

    def listar_cliente(self, id, sessao):
        cliente = sessao.query(Cliente).filter(Cliente.id == id).first()
        return cliente

    def listar_cliente_nome(self, nome, sessao):
        clientes = sessao.query(Cliente).filter(Cliente.nome == nome).all()
        return clientes

    def listar_cliente_nomes_ordenados(self, nome, sessao):
        clientes = sessao.query(Cliente).filter(Cliente.nome == nome).order_by(Cliente.idade).all()
        #em ordem descrecente
        #clientes = sessao.query(Cliente).filter(Cliente.nome == nome).order_by(Cliente.idade.desc()).all()
        return clientes

    def inserir(self,cliente,sessao):
        novo_cliente = Cliente(nome=cliente.nome, idade=cliente.idade)
        sessao.add(novo_cliente)

    def alterar(self,cliente, id, sessao):
        sessao.query(Cliente).filter(Cliente.id == id).update({'nome': cliente.nome, 'idade': cliente.idade})

    def excluir(self, id, sessao):
        cliente = self.listar_cliente(id, sessao)
        sessao.delete(cliente)

