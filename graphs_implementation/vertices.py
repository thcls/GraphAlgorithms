
class Vertex:
    def __init__(self, name) -> None:
        self.name = str(name)
        self.cost = 0
        self.edges = []
        self.edgesin = []

    def addNeighbor(self, neighbor, weight):
        edge = {
            'neighbor': neighbor,
            'weight': weight
        }
        self.edges.append(edge)
        edge = {
            'neighbor': self,
            'weight': weight
        }
        neighbor.edgesin.append(edge)
    
    def intName(self):
        return int(self.name)
    
    def getNum(self):
        return ord(self.name)-65

if __name__ == "__main__":
    pass