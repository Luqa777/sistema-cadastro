from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Integer, Column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:admin@localhost:3306/login', echo=False)

Session = sessionmaker(bind=engine)
session = Session()


class Base(DeclarativeBase):
    pass


class Pessoa(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    senha = Column(String(255), nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha



Base.metadata.create_all(engine)
