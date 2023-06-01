from sys import maxsize

def floyd_Warshall(graph):
    matrix = []
    for i in range(len(graph)):
        line = []
        for j in range(len(graph)):
            if i == j:
                line.append(0)
            else:
                e = False
                for edge in graph[i].edges:
                    if edge['neighbor'].getNum() == j:
                        line.append(edge['weight'])
                        e = True
                        break
                if not e:
                    line.append(maxsize)
        matrix.append(line)

    for k in range(0, len(graph)):
        for i in range(0, len(graph)):
            for j in range(0, len(graph)):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    
    for line in matrix:
        print(line)


if __name__ == "__main__":
    pass