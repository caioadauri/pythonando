import pymysql.cursors

connection = pymysql.connect(
  host='127.0.0.1', 
  port=3306, 
  user='root', 
  password='root',
  database='pythonando',
  cursorclass = pymysql.cursors.DictCursor
  )

def CriarTabela(tabela):
  try:
    with connection.cursor() as cursor:
      cursor.execute(f'create table {tabela} (nome varchar(200))')
    print(f'Tabela {tabela} criada com sucesso!')
  except Exception as e:
    print(f'Erro ao criar tablea {tabela}: {e}')

def RemoverTabela(tabela):
  try:
    with connection.cursor() as cursor:
      cursor.execute('DROP table teste')
    print(f'Tabela removida com sucesso!')
  except Exception as e:
    print(f'Erro ao remover tabela {tabela}: {e}')

def InsereDados():
  try:
    with connection.cursor() as cursor:
      cursor.execute("INSERT INTO teste values ('Marcos')")
      connection.commit()
    print(f'Inserção de dados realizada com sucesso!')
  except Exception as e:
    print(f'Erro ao inserir dados {e}')

def RetornaDados():
  try:
    with connection.cursor() as cursor:
      cursor.execute("SELECT * FROM teste")
      retorno = cursor.fetchall()
    for i in retorno:
      print(i)
  except Exception as e:
    print(f'Erro ao retornar os dados {e}')

def AtualizaDados(atual, novo):
  try:
    with connection.cursor() as cursor:
      cursor.execute(f"UPDATE teste set nome = '{novo}' where nome = '{atual}'")
      connection.commit()
    print('Dado atualizado com sucesso!')
  except Exception as e:
    print(f'Erro ao atualizar o dado {e}')

def ExcluiDados(registro):
  try:
    with connection.cursor() as cursor:
      cursor.execute(f"DELETE FROM TESTE WHERE nome = '{registro}'")
      connection.commit()
    print('Dado deletado com sucesso!')
  except Exception as e:
    print(f'Erro ao excluir o dado: {e}')

RetornaDados()

connection.close()






