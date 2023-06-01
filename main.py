from os import listdir
from json import load

from graphs_implementation.vertices import Vertex
from untils import *

from shortest_path_algorithms.bellman_ford import bellman_Ford
from shortest_path_algorithms.dijkstra import dijkstra
from shortest_path_algorithms.floyd_warshall import floyd_Warshall

def selectGraph():
    files = listdir('graphs/')
    cont = 1
    for i in files:
        print('Num {}: {}'.format(str(cont),i),end=' | \n')
        cont += 1
    
    num = int(input('\nSelect graph: '))
    return files[num-1]
        
def getGraph():
    with open('graphs/{}'.format(selectGraph())) as jsonFile:
        graph = load(jsonFile)
        
    vertices = []
    
    for name in graph.keys():
        vertices.append(Vertex(name))
    
    for vertice in vertices:
        for key in graph[vertice.name].keys():
            vertice.addNeighbor(vertices[ord(key)-65], graph[vertice.name][key])
    
    return vertices

def getGraphSiple():
    with open('graphs/{}'.format(choose_input())) as jsonFile:
        graph = load(jsonFile)
    
    return graph

graph = getGraph()
printGraph(graph)
floyd_Warshall(graph)