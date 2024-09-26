from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import Pessoa

# declaracao de constante em Python por padrão é feito em letra maiuscula
def RetornaSession():
  USUARIO = "root"
  SENHA = "root"
  HOST = "127.0.0.1"
  BANCO = "pythonando"
  PORTA = "3306"
  CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}"

  engine = create_engine(CONN, echo=True)
  Session = sessionmaker(bind=engine)
  return Session()


session = RetornaSession()



# inserindo no banco de dados
# x = Pessoa(nome='caio',
#            usuario='caioadauri',
#            senha='1234')

# session.add(x)
# session.commit()