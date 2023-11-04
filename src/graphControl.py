from sys import maxsize
from src.Graph import Graph
from os import listdir
from src.utils import *

def NovoGrafo():
    G = Graph()
    addVertice(G, 'v1')
    
    return G

def Grafo(G):
    files = listdir('src/grafos')
    for index,file in enumerate(files):
        print(f'( {index} ) | {file}')
        
    num = int(input('\nEscolha um Grafo: '))
    
    with open(f'src/grafos/{files[num]}', 'r') as arquivo:
        
        linhas = arquivo.readlines()
        grafoData = []
        
        for linha in linhas:
            if linha != '\n':
                linha = linha.strip()
                linha = linha.replace('\n', '')
                linha = linha.split(' ')
                linha[2] = int(linha[2])
                grafoData.append(linha)
                
        G = Graph()
        
        grafoHeader = grafoData.pop(0)
        
        G.nome = grafoHeader[0]
        G.n = 0
        G.m = 0
        
        for e in grafoData:
            if not EVertice(G, e[0]):
                addVertice(G, e[0])
            if not EVertice(G, e[1]):
                addVertice(G, e[1])

            AddAresta(G, e[0], e[1], e[2])
        
    return G

def EVertice(G, v):
    return (v in G.vertices)

def AddAresta(G, vi, vj , w):
    if not( EVertice(G, vi) and EVertice(G, vj)):
        return
    
    vi = G.vertices[vi]
    vj = G.vertices[vj]
    vi.arestas.append({
        'peso': w,
        'vertice': vj
    })
    G.m += 1

def RemoveAresta(G, vi, vj , w):
    if not( EVertice(G, vi) and EVertice(G, vj) and ExisteAresta(G, vi, vj , w)):
        return
    
    vi = G.vertices[vi]
    for index,e in enumerate(vi.arestas):
        if e['peso'] == w and e['vertice'].nome == vj:
            vi.arestas.pop(index)
    G.m -= 1
    
def ExisteAresta(G, vi, vj , w):
    vi = G.vertices[vi]
    for e in vi.arestas:
        if e['peso'] == w and e['vertice'].nome == vj:
            return True
    return False

def MudaPeso(G, vi, vj , w, novoW):
    if not(ExisteAresta(G, vi, vj , w)):
        return
    
    vi = G.vertices[vi]
    for index, e in enumerate(vi.arestas):
        if e['peso'] == w and e['vertice'].nome == vj:
            vi.arestas[index]['peso'] = novoW

def ImprimeGrafo(G):
    print(f'\n  ___ Nome: {G.nome} n: {G.n} m: {G.m} ___  ')
    for key in G.vertices.keys():
        v = G.vertices[key]
        print(f'\n____________ vertice: { v.nome } ____________\n')
        for e in v.arestas:
            print(f'{v.nome} -----({e['peso']})-----> {e['vertice'].nome}')

def RemoveGrafo(G):
    for key in G.vertices.keys():
        del G.vertices[key]
    del G

def RecuperaPeso(G, vi, vj ):
    if not( EVertice(G, vi) and EVertice(G, vj)):
        return
    
    pesos = []
    vi = G.vertices[vi]
    
    for e in vi.arestas:
        pesos.append(e['peso'])
    return tuple(pesos)

def GrafoSimples(G):
    if Eciclo(G):
        return False
    for key in G.vertices.keys():
        arestas = Incidencia(G, key)
        for e in arestas:
            for i in arestas:
                if e['vertice'].nome == i['vertice'].nome and e != i:
                    return False
    return True

def EArvore(G):
    return Eciclo(G) and Conexo(G)

def EBipartido(G):
    keys = G.vertices.keys()
    visitados = dict(zip(keys, ['b']*G.n))
    keys = list(keys)
    vi = G.vertices[keys[0]]
    lista = [vi]
    visitados[vi.nome] = 'v'

    while len(lista) != 0:
        vi = lista[0]
        
        if visitados[vi.nome] == 'v':
            cor = 'a'
        else:
            cor = 'v'
        for e in vi.arestas:
            u = e['vertice']
            
            if visitados[u.nome] == 'b':
                lista.append(u)
                visitados[u.nome] = cor
            elif visitados[u.nome] == visitados[vi.nome]:
                return False
            
        lista.pop(0)
        
    return True

def Complemento(G):
    keys = G.vertices.keys()
    
    Gi = Graph()
    Gi.m = 0
    Gi.nome = G.nome + "'"
    
    for key in keys:
        addVertice(Gi,key)
        
    for key in keys:
        v = G.vertices[key]
        for e in v.arestas:
            for key2 in keys:
                if e['vertice'].nome == key2:
                    continue
                else:
                    AddAresta(Gi, key, key2, 1)
                    Gi.m += 1
    return Gi

def EAdj(G, vi, vj ):
    vi = G.vertices[vi]
    for e in vi.arestas:
        if e['vertice'].nome == vj:
            return True
    return False

def Adjacencia(G, v):
    if not(EVertice(G, v)):
        return
    
    vi = G.vertices[v]
    return vi.arestas

def Incidencia(G, vi):
    if not(EVertice(G, vi)):
        return
    
    arestas = []
    for key in G.vertices.keys():
        v = G.vertices[key]
        for e in v.arestas:
            if e['vertice'].nome == vi:
                arestas.append(e)
    return tuple(arestas)

def MatrizAdj(G):
    keys = G.vertices.keys()
    keys = list(keys)
    index = dict(zip(keys, range(G.n)))
    
    matrizAdj = []
    for key in G.vertices.keys():
        matrizAdj.append([0]*G.n-1)
        u = G.vertices[key]
        for e in u.arestas:
            i = index[e['vertice'].nome]
            matrizAdj[i].append(e['peso'])
    return matrizAdj

def ImprimeMatrizAdj(G):
    keys = G.vertices.keys()
    keys = list(keys)
    index = dict(zip(keys, range(G.n)))
    
    print(f'   ', end='')
    
    for i in keys:
        print(f'  {i}  ', end='')
        
    print('')
    matrizAdj = []
    
    for ind, key in enumerate(G.vertices.keys()):
        matrizAdj.append([0]*(G.n))
        u = G.vertices[key]
        for e in u.arestas:
            i = index[e['vertice'].nome]
            matrizAdj[ind][i] = e['peso']
            
    for i in range(G.n):
        print(f'{keys[i]}  ', end='')
        for j in range(G.n):
            print(f'  {matrizAdj[i][j]}  ', end='')
        print('')

def Conexo(G):
    keys = G.vertices.keys()
    visitados = dict(zip(keys, [False]*G.n))
    keys = list(keys)
    vi = G.vertices[keys[0]]
    lista = [vi]
    visitados[vi.nome] = True
    num = 1
    
    while len(lista) != 0:
        vi = lista[0]
        for e in vi.arestas:
            u = e['vertice']
            if not visitados[u.nome]:
                visitados[u.nome] = True
                num += 1
                lista.append(u)
                
        lista.pop(0)
        
    return num == G.n

def DSF(G, vi):
    vi = G.vertices[vi]
    keys = G.vertices.keys()
    visitados = dict(zip(keys, [False]*G.n))
    pilha = [vi]
    visitados[vi.nome] = True
    arvore = []
    while len(pilha) != 0:
        vi = pilha[-1]
        for e in vi.arestas:
            u = e['vertice']
            if not visitados[u.nome]:
                pilha.append(u)
                DSF_visitado(vi, u, visitados, arvore)
        pilha.pop()
    return tuple(arvore)

def BSF(G, vi):
    vi = G.vertices[vi]
    keys = G.vertices.keys()
    visitados = dict(zip(keys, [False]*G.n))
    lista = [vi]
    visitados[vi.nome] = True
    arvore = []
    while len(lista) != 0:
        vi = lista[0]
        for e in vi.arestas:
            u = e['vertice']
            if not visitados[u.nome]:
                visitados[u.nome] = True
                arvore.append((vi.nome, u.nome))
                lista.append(u)
                
        lista.pop(0)
    return tuple(arvore)

def CaminhoMinimo(G, vi, vj):
    vi = G.vertices[vi]
    vj = G.vertices[vj]
    keys = G.vertices.keys()
    custo = dict(zip(keys, [maxsize]*G.n))
    antecessores = dict(zip(keys, [0]*G.n))
    custo[vi.nome] = 0

    for i in range(0, G.n-1):
        for key in keys:
            v = G.vertices[key]
            
            for e in v.arestas:
                nome = e['vertice'].nome
                if custo[nome] > e['peso'] + custo[v.nome]:
                    custo[nome] = e['peso'] + custo[v.nome]
                    antecessores[nome] = v.nome
                    
        antecessor = vj.nome
        caminho = [vj.nome]

    while antecessor != vi.nome:
        antecessor = antecessores[antecessor]
        caminho.insert(0, antecessor)
            
    return tuple(caminho)

def CustoMinimo(G, v):
    vi = G.vertices[vi]

    keys = G.vertices.keys()
    custo = dict(zip(keys, [maxsize]*G.n))
    custo[vi.nome] = 0

    for i in range(0, G.n-1):
        for key in keys:
            v = G.vertices[key]
            
            for e in v.arestas:
                nome = e['vertice'].nome
                if custo[nome] > e['peso'] + custo[v.nome]:
                    custo[nome] = e['peso'] + custo[v.nome]
    return tuple(custo)

def CaminhosMinimos(G, v):
    v = G.vertices[v]

    keys = G.vertices.keys()
    custo = dict(zip(keys, [maxsize]*G.n))
    antecessores = dict(zip(keys, [0]*G.n))
    custo[v.nome] = 0

    for i in range(0, G.n-1):
        for key in keys:
            vi = G.vertices[key]
            
            for e in vi.arestas:
                nome = e['vertice'].nome
                if custo[nome] > e['peso'] + custo[vi.nome]:
                    custo[nome] = e['peso'] + custo[vi.nome]
                    antecessores[nome] = vi.nome
    caminhos = {}
    
    for key in keys:
        caminho = [key]
        antecessor = key
        while antecessor != v.nome:
            antecessor = antecessores[antecessor]
            caminho.insert(0, antecessor)
        
        caminhos[key] = caminho
    
    return caminhos

if '__main__' == __name__:
    pass