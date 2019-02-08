from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from fabricas import fabrica_conexao

fabrica = fabrica_conexao.ConexaoDB()
engine = fabrica.conectar()

Base = declarative_base()

produto_pedido = Table('produto_pedido', Base.metadata,
                       Column('produto_id', Integer, ForeignKey('produto.id')),
                       Column('pedido_id', Integer, ForeignKey('pedido.id')))

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False)
    idade = Column(Integer, nullable=False)

    pedidos = relationship("Pedido", back_populates="cliente")

    def __repr__(self):
        return f"Cliente {self.id} {(self.nome,self.idade)}"

class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True)

    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    cliente = relationship("Cliente", back_populates="pedidos") #Relacionamento entre a tabela pedido e cliente

    produtos = relationship("Produto", secondary="produto_pedido", back_populates="pedido")

    def __repr__(self):
        return f"Pedido de número {self.id}"

class Produto(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(40), nullable=False)
    valor = Column(Float, nullable=False)

    pedido = relationship("Pedido", secondary="produto_pedido", back_populates="produtos")

Base.metadata.create_all(engine)