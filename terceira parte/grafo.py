grafo = {
    "joel": ["dom", "fabio"], #não busca quando inverte os itens da lista
    "fabio": [],
    "dom":[],
}
print(f"\n{grafo}")

from collections import deque
"""tempo de execução O(vertices+arestas)"""
def pesquisa(nome):
  fila_de_pesquisa = deque()
  fila_de_pesquisa += grafo[nome]
  verificadas = []
  while fila_de_pesquisa:
    pessoa = fila_de_pesquisa.popleft()
    if pessoa in verificadas:
      fila_de_pesquisa += grafo[pessoa]
      verificadas.append(pessoa)
    elif pessoa_e_vendedor(pessoa):
      print(f"\n{pessoa} é o vendendor")
    else:
      fila_de_pesquisa+= grafo[pessoa]
      return True

def pessoa_e_vendedor(nome):
  return nome[-1] == 'm'

pesquisa("joel")