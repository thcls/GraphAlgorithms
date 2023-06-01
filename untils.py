def printGraph(graph):
    print('__________________________________')
    for vertice in graph:
        message = 'Name: ' + vertice.name + ' Neighbors: '
        for edge in vertice.edges:
            message += edge['neighbor'].name + ', '
        print(message,end='\n')
    print('__________________________________')
        
def printweight(graph):
    print('----'*len(graph))
    for vertice in graph:
        print(vertice.name,end='   ')
    print('',end='\n')
    for vertice in graph:
        print(vertice.cost,end='   ')
        #vertice.printInfo()
    print('',end='\n')
    print('----'*len(graph))