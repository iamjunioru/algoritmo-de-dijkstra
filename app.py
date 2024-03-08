def dijkstra(grafo, origem, destino):
  distancias = {vertice: float('inf') for vertice in grafo}
  distancias[origem] = 0

  visitados = set()

  # loop
  while True:
    vertice_atual = min((vertice for vertice in grafo if vertice not in visitados), key=lambda vertice: distancias[vertice])

    if vertice_atual == destino:
      return _reconstruir_caminho(origem, destino, distancias)
    if all(vertice in visitados for vertice in grafo):
      return None

    # marcar como visitado
    visitados.add(vertice_atual)

    for adjacente, peso in grafo[vertice_atual].items():
      nova_distancia = distancias[vertice_atual] + peso
      if nova_distancia < distancias[adjacente]:
        distancias[adjacente] = nova_distancia

def _reconstruir_caminho(origem, destino, distancias):
  caminho = []
  vertice_atual = destino

  while vertice_atual != origem:
    caminho.append(vertice_atual)
    for adjacente, peso in grafo[vertice_atual].items():
      if distancias[vertice_atual] == distancias[adjacente] + peso:
        vertice_atual = adjacente
        break

  caminho.append(origem)
  caminho.reverse()

  return caminho

# ex
grafo = {
  "A": {"B": 4, "C": 2},
  "B": {"A": 4, "C": 1, "D": 5},
  "C": {"A": 2, "B": 1, "D": 3, "E": 6},
  "D": {"B": 5, "C": 3, "E": 4},
  "E": {"C": 6, "D": 4},
}

origem = "A"
destino = "E"

caminho = dijkstra(grafo, origem, destino)

if caminho is None:
  print(f"não existe caminho de {origem} para {destino}.")
else:
  print(f"o caminho minimo de {origem} para {destino} é {caminho}.")
