from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# declaracao de constante em Python por padrão é feito em letra maiuscula
USUARIO = "root"
SENHA = "root"
HOST = "127.0.0.1"
BANCO = "pythonando"
PORTA = "3306"

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
  __tablename__ = 'Pessoa'
  id = Column(Integer, primary_key=True)
  nome = Column(String(100))
  usuario = Column(String(50))
  senha = Column(String(30))

Base.metadata.create_all(engine)