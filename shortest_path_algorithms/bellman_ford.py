from sys import maxsize
from untils import printweight

def bellman_Ford(graph, sourse):
    for vertex in graph:
        vertex.cost = maxsize
        
    sourse.cost = 0
    
    printInteration(graph)
    for i in range(0, len(graph)-1):
        for vertex in graph:
            for edge in vertex.edgesin:
                if vertex.cost > edge['weight'] + edge['neighbor'].cost:
                    vertex.cost = edge['weight'] + edge['neighbor'].cost
                    
        printInteration(graph)
    printweight(graph)
        
def printInteration(graph):
    for i in graph:
        if i.cost > maxsize-10000:
            print('', end='∞, ')
        else:
            print(i.cost, end=', ')
    print('',end='\n')
        
if __name__ == "__main__":
    pass