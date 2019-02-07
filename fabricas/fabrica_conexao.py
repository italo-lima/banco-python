import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ConexaoDB():

    def conectar(self):
        user = "root"
        passwd = "0806italo"
        db = "treinaweb_miniprojeto"
        host = "localhost"
        port = 3306

        engine = create_engine(f'mysql://{user}:{passwd}@{host}:{port}/{db}')
        return engine

    def criar_sessao(self):
        conexao = self.conectar()
        Session = sessionmaker()
        Session.configure(bind=conexao)
        session = Session()

        return session