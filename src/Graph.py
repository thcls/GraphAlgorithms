class Graph:
    def __init__(self) -> None:
        self.nome  = ''
        self.n = 0
        self.m = 0
        self.vertices = {} # 'vi': vi

class Vertice:
    def __init__(self, nome) -> None:
        self.nome  = nome
        self.arestas = [] # {'peso': w,'vertice': vi}