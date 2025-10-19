import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT)

  print("--- Teste de Conexão e Append ---")
  print("Valor inicial:", conn.root.exposed_value())
  conn.root.exposed_append(20)
  conn.root.exposed_append(5)
  conn.root.exposed_append(10)
  print("Após appends (20, 5, 10):", conn.root.exposed_value())
  print("-" * 20)

  print("--- Teste de Search ---")
  print("Pesquisando '5':", conn.root.exposed_search(5))
  print("Pesquisando '99':", conn.root.exposed_search(99))
  print("-" * 20)

  print("--- Teste de Sort ---")
  conn.root.exposed_sort()
  print("Valor após ordenar:", conn.root.exposed_value())
  print("-" * 20)

  print("--- Teste de Remove ---")
  print("Removendo '10':", conn.root.exposed_remove(10))
  print("Valor após remover '10':", conn.root.exposed_value())
  print("Removendo '99':", conn.root.exposed_remove(99))
  print("Valor após tentar remover '99':", conn.root.exposed_value())
  print("-" * 20)

  print("--- Teste de Insert ---")
  print("Inserindo '99' na posição 0:", conn.root.exposed_insert(0, 99))
  print("Valor após inserir:", conn.root.exposed_value())
  print("-" * 20)