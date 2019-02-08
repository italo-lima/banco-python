from db import Produto

class ProdutoRepo():

    def inserir_produto(self, produto, sessao):
        novo_produto = Produto(descricao = produto.descricao, valor = produto.valor)
        sessao.add(novo_produto)