# GraphAlgorithms

Implementações de algoritmos destinados a lidar com grafos ponderados.

## Leitura de Grafo a partir de um Arquivo de Texto:

*Durante a execução é possível escolher qual arquivo de texto o programa principal irá operar. O arquivo deve ser localizado em /GraphAlgorithms/src/grafos* e seguir o formato descrito abaixo:

1. A primeira linha contém três campos:
    - Uma string que indica o nome do grafo (por exemplo, G, H, G1, etc.).
    - O número de vértices (n) no grafo.
    - O número de arestas (m) no grafo.
    Os valores n e m devem ser separados por um espaço simples e lidos na ordem especificada.
2. A partir da terceira linha, as linhas seguintes consistem nas especificações das arestas direcionadas, uma por linha. Cada linha contém:
    - A descrição de uma aresta no formato (vi, vj), onde vi é o valor do vértice de origem e vj é o valor do vértice de destino.
    - Após um espaço em relação ao vértice vj, um terceiro campo indica o peso da aresta (vi, vj).

O peso de cada aresta pode ser um número real positivo ou negativo, ou mesmo infinito, indicado como o valor máximo representável pela linguagem de programação escolhida. Essa estrutura de entrada permite a definição precisa de grafos ponderados e é a base para a construção e manipulação do grafo no programa.

## Operações Básicas:

Este projeto implementa as seguintes operações básicas para manipulação de grafos ponderados:

- `NovoGrafo()`: Retorna um novo grafo vazio, contendo apenas um vértice.
- `Grafo(G)`: Retorna uma representação por listas de adjacências do grafo G.
- `EVertice(G, v)`: Verifica se o vértice v pertence ao conjunto de vértices V(G) do grafo G.
- `AddAresta(G, vi, vj, ω)`: Adiciona uma aresta ponderada em G entre os vértices vi e vj, com o peso ω. Essa operação verifica se vi e vj pertencem a V(G); caso contrário, a operação não é executada.
- `RemoveAresta(G, vi, vj, ω)`: Remove uma aresta ponderada em G entre os vértices vi e vj, com o peso ω. Essa operação verifica se vi e vj pertencem a V(G) e se a aresta existe; caso contrário, a operação não é executada.
- `ExisteAresta(G, vi, vj, ω)`: Verifica se existe uma aresta em G entre os vértices vi e vj, com o peso ω.
- `MudaPeso(G, vi, vj, ω, ω')`: Modifica o valor do peso de uma aresta em G entre os vértices vi e vj, de ω para ω'. Essa operação verifica se vi e vj pertencem a V(G) e se a aresta existe; caso contrário, a operação não é executada.
- `ImprimeGrafo(G)`: Imprime todos os vértices e arestas do grafo G.
- `RemoveGrafo(G)`: Libera todo o espaço utilizado pela representação de G.
- `RecuperaPeso(G, vi, vj)`: Devolve a lista de pesos de todas as arestas entre os vértices vi e vj em V(G). Essa operação verifica se vi e vj pertencem a V(G); caso contrário, a operação não é executada.
- `GrafoSimples(G)`: Retorna se o grafo G é um grafo simples (sem arestas paralelas ou laços) ou não.
- `EArvore(G)`: Retorna se o grafo G é uma árvore (um grafo conexo sem ciclos) ou não.
- `EBipartido(G)`: Retorna se o grafo G é bipartido (pode ser dividido em dois conjuntos disjuntos de vértices, onde todas as arestas ligam vértices de conjuntos diferentes) ou não.
- `Complemento(G)`: Retorna o grafo complementar G de G (todos os vértices que não estão em G, formam o conjunto de vértices em G complementar, e as arestas são adicionadas entre os vértices do complemento de G).
- `EAdj(G, vi, vj)`: Verifica se existe uma aresta entre os vértices vi e vj em E(G).
- `Adjacencia(G, v)`: Devolve a lista de adjacência do vértice v em G. Essa operação verifica se v pertence a V(G); caso contrário, a operação não é executada.
- `Incidencia(G, v)`: Devolve as arestas incidentes ao vértice v em G. Essa operação verifica se v pertence a V(G); caso contrário, a operação não é executada.
- `MatrizAdj(G)`: Constrói a matriz de adjacência de G, onde a posição a[i][j] corresponde ao peso da aresta entre os vértices vi e vj. Essa operação cria uma matriz n x n, onde n é o número de vértices de G.
- `ImprimeMatrizAdj(G)`: Imprime a matriz de adjacência de G.
- `Conexo(G)`: Retorna se G é um grafo conexo (todos os vértices estão conectados) ou não.

Essas operações fornecem as bases para manipular grafos ponderados neste projeto.

## Percursos:

Este projeto implementa dois algoritmos de percurso em grafos:

- `DFS(G, vi)`: Percorre os vértices do grafo G em profundidade, começando a busca no vértice vi ∈ V(G). Durante o percurso, é gerada uma árvore de busca que indica, para cada vértice vi ∈ V(G), o vértice a partir do qual vi foi alcançado pela primeira vez na busca. O resultado é um vetor que representa essa árvore de busca.
- `BFS(G, vi)`: Percorre os vértices do grafo G em largura, começando a busca no vértice vi ∈ V(G). Assim como no DFS, durante o percurso, é gerada uma árvore de busca que indica, para cada vértice vi ∈ V(G), o vértice a partir do qual vi foi alcançado pela primeira vez na busca. O resultado é um vetor que representa essa árvore de busca.

Esses algoritmos são úteis para explorar a estrutura do grafo e encontrar conexões entre os vértices. Eles são amplamente utilizados em diversos problemas e aplicações que envolvem grafos ponderados.

## Caminhos Mínimos:

Este projeto implementa três algoritmos relacionados à busca de caminhos mínimos em grafos ponderados:

- `CaminhoMinimo(G, vi, vj)`: Este algoritmo devolve um caminho mínimo, que é uma sequência de vértices, entre o vértice vi e o vértice vj no grafo G. O caminho mínimo é calculado com base nos pesos das arestas.
- `CustoMinimo(G, v)`: Este algoritmo calcula os custos dos caminhos mínimos a partir de um vértice v para todos os outros vértices no grafo G. Ele retorna uma estrutura de dados que associa cada vértice alcançável a partir de v com o custo mínimo para atingir esse vértice.
- `CaminhoMinimo(G, v)`: Este algoritmo calcula os caminhos mínimos entre um vértice v e todos os outros vértices do grafo G. Ele retorna uma estrutura de dados que associa cada vértice alcançável.

## Utilitário:

Este projeto implementa algumas funções utilitárias para a manipulação de grafos:

- `addVertice(G, v, i)`: Adiciona um novo vértice ao grafo G e incrementa o número de vértices n do grafo em  i.
- `Eciclo(G)`: Verifica se o grafo G contém um ciclo usando BSF.
- `salvarGrafo(G, nome):`: Salva o grafo G em um arquivo txt com o nome especificado no formato descrito no início.