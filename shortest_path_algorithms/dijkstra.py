from sys import maxsize
from untils import printweight

def dijkstra(graph, sourse):
    prev = []
    
    for vertex in graph:
        vertex.cost = maxsize
        prev.append(vertex)
    
    sourse.cost = 0
    
    while len(prev):
        
        index = 0
        for i in range(0,len(prev)):
            if prev[index].cost > prev[i].cost:
                index = i
        vertex = prev.pop(index)
        
        for edge in vertex.edges:
            if vertex.cost + edge['weight'] < edge['neighbor'].cost:
                edge['neighbor'].cost = vertex.cost + edge['weight']
    
    printweight(graph)

def dijkstraHeap(graph, sourse):
    prev = []
    
    sourse.cost = 0
    for vertex in graph:
        prev.append(vertex)
    
    while len(prev):
        index = 0
        for i in range(0,len(prev)):
            if prev[index].cost > prev[i].cost:
                index = i
        vertex = prev.pop(index)
        
        for edge in vertex.edges:
            if vertex.cost + edge['weight'] < edge['neighbor'].cost:
                edge['neighbor'].cost = vertex.cost + edge['weight']

if __name__ == "__main__":
    pass