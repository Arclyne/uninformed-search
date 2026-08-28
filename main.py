from collections import deque

class Mapa:
    def __init__(self, ciudades):
        self.ciudades = ciudades

        self.indices = {}

        for posicion in range(len(ciudades)):
            ciudad = ciudades[posicion]
            self.indices[ciudad] = posicion

        cantidad = len(ciudades)
        self.matriz = []

        for fila in range(cantidad):
            nueva_fila = [0] * cantidad
            self.matriz.append(nueva_fila)

    def conectar(self, ciudad1, ciudad2):
        fila = self.indices[ciudad1]
        columna = self.indices[ciudad2]

        self.matriz[fila][columna] = 1
        self.matriz[columna][fila] = 1

    def obtener_vecinos(self, ciudad):
        vecinos = []
        fila = self.indices[ciudad]

        for columna in range(len(self.ciudades)):
            if self.matriz[fila][columna] == 1:
                vecinos.append(self.ciudades[columna])

        return vecinos

    def mover(self, ciudad_actual, destino):
        fila = self.indices[ciudad_actual]
        columna = self.indices[destino]

        if self.matriz[fila][columna] == 1:
            return destino

        return None

    def mostrar_mapa(self):
        for ciudad in self.ciudades:
            vecinos = self.obtener_vecinos(ciudad)
            print(ciudad, "->", vecinos)


ciudades = [
    "Arad",
    "Zerind",
    "Oradea",
    "Sibiu",
    "Timisoara",
    "Lugoj",
    "Mehadia",
    "Drobeta",
    "Craiova",
    "Rimnicu Vilcea",
    "Fagaras",
    "Pitesti",
    "Bucharest",
    "Giurgiu",
    "Urziceni",
    "Hirsova",
    "Eforie",
    "Vaslui",
    "Iasi",
    "Neamt"
]

mapa = Mapa(ciudades)

mapa.conectar("Arad", "Zerind")
mapa.conectar("Arad", "Sibiu")
mapa.conectar("Arad", "Timisoara")

mapa.conectar("Zerind", "Oradea")
mapa.conectar("Oradea", "Sibiu")

mapa.conectar("Timisoara", "Lugoj")
mapa.conectar("Lugoj", "Mehadia")
mapa.conectar("Mehadia", "Drobeta")
mapa.conectar("Drobeta", "Craiova")

mapa.conectar("Sibiu", "Fagaras")
mapa.conectar("Sibiu", "Rimnicu Vilcea")

mapa.conectar("Rimnicu Vilcea", "Craiova")
mapa.conectar("Rimnicu Vilcea", "Pitesti")

mapa.conectar("Craiova", "Pitesti")

mapa.conectar("Fagaras", "Bucharest")
mapa.conectar("Pitesti", "Bucharest")

mapa.conectar("Bucharest", "Giurgiu")
mapa.conectar("Bucharest", "Urziceni")

mapa.conectar("Urziceni", "Hirsova")
mapa.conectar("Hirsova", "Eforie")

mapa.conectar("Urziceni", "Vaslui")
mapa.conectar("Vaslui", "Iasi")
mapa.conectar("Iasi", "Neamt")

def reconstruir_camino(parents, start, goal):
    camino = deque()
    actual = goal

    while actual != start:
        camino.appendleft(actual)
        actual = parents[actual]

    camino.appendleft(start)
    return camino


def bfs(mapa, start, goal):
    if start == goal:
        return deque([start])

    visited = {start}
    parents = {}
    cola = deque([start])

    while cola:
        actual = cola.popleft()

        for vecino in mapa.obtener_vecinos(actual):
            if vecino not in visited:
                visited.add(vecino)
                parents[vecino] = actual

                if vecino == goal:
                    return reconstruir_camino(parents, start, goal)

                cola.append(vecino)

    return None


def dfs(mapa, start, goal):
    if start == goal:
        return deque([start])

    visited = {start}
    parents = {}

    def buscar(actual):
        for vecino in mapa.obtener_vecinos(actual):
            if vecino not in visited:
                visited.add(vecino)
                parents[vecino] = actual

                if vecino == goal:
                    return True

                if buscar(vecino):
                    return True

        return False

    if buscar(start):
        return reconstruir_camino(parents, start, goal)

    return None


def main():
    ciudad_actual = "Arad"
    target_city = "Bucharest"

    print("Ciudad inicial:", ciudad_actual)
    print("Ciudad destino:", target_city)

    camino_bfs = bfs(mapa, ciudad_actual, target_city)
    print("\nBFS (búsqueda en amplitud):")
    if camino_bfs is not None:
        print("Camino encontrado:", list(camino_bfs))
    else:
        print("No existe un camino hacia", target_city)

    camino_dfs = dfs(mapa, ciudad_actual, target_city)
    print("\nDFS (búsqueda en profundidad):")
    if camino_dfs is not None:
        print("Camino encontrado:", list(camino_dfs))
    else:
        print("No existe un camino hacia", target_city)


if __name__ == "__main__":
    main()