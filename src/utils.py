from src.Graph import Vertice

def addVertice(G, v):
    u = Vertice(v)
    G.vertices[v] = u
    G.n += 1

def DSF_visitado(v, u, visitados, arvore):
    visitados[u.nome] = True
    arvore.append((v.nome, u.nome))
    for e in u.arestas:
        
        vi = e['vertice']
        if not visitados[vi.nome]:
            DSF_visitado(u, vi, visitados, arvore)
            
def Eciclo(G):
    keys = G.vertices.keys()
    visitados = dict(zip(keys, [False]*G.n))
    keys = list(keys)
    vi = G.vertices[keys[0]]
    lista = [vi]
    visitados[vi.nome] = True
    
    while len(lista) != 0:
        vi = lista[0]
        for e in vi.arestas:
            u = e['vertice']
            if not visitados[u.nome]:
                visitados[u.nome] = True
                lista.append(u)
            else:
                return True
                
        lista.pop(0)
        
    return False

def salvarGrafo(G, nome):
    with open(f'src/grafos/{nome}.txt', 'w') as f:
        f.write(f"{nome} {G.n} {G.m}\n")
        f.write('\n')
        for key in G.vertices.keys():
            v = G.vertices[key]
            for e in v.arestas:
                f.write(f"{v.nome} {e['vertice'].nome} {e['peso']}\n")