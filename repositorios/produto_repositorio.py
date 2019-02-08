from db import Produto

class ProdutoRepo():

    def inserir_produto(self, produto, sessao):
        novo_produto = Produto(descricao = produto.descricao, valor = produto.valor)
        sessao.add(novo_produto)

    def listar_produto_id(self, id, sessao):
        produto = sessao.query(Produto).filter(Produto.id == id).first()
        return produto