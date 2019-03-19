#CENTRO DE INFORMATICA#
#ANALISE E PROJETO DE ALGORITMOS#
#ALUNA: HOZANA RAQUEL GOMES DE LIMA - 11414870#
#DIJKSTRA#

from collections import defaultdict
import heapq

INF = 999999999

class Grafo:

    def __init__(self, vertices):
        self.V     = vertices 
        self.G     = defaultdict(list)
        self.chave = defaultdict(int)
        self.pai   = defaultdict(int)

    #adiciona aresta
    def add(self, x, y, w):
        self.G[x].append( (y,w) )
        self.G[y].append( (x,w) )
        

    def DIJKSTRA(self, s):
        nafila = defaultdict(int)
        for i in range(self.V):
            self.chave[i] = INF
            self.pai[i]   = INF
            nafila[i]     = True 
        self.chave[s] = 0
        
        heap = []
        heapq.heappush(heap, (0, s))
        while heap:
            _,u = heapq.heappop(heap)
            nafila[u] = False
            for v,w in self.G[u]:
                if(nafila[v] == True and w + self.chave[u] < self.chave[v]):
                    self.pai[v]   = u
                    self.chave[v] = w + self.chave[u]
                    heapq.heappush(heap, (w, v))
                   
        for i in range(self.V-1):
            print("V[",i+1,"] tem peso:", self.chave[i+1], "vindo pelo vertice:", self.pai[i+1])
            
        print('Custo do caminho:', self.chave[self.V-1])
def calculaMenorCaminho(instancia):
    print("Instancia", instancia)
    
    f = open(instancia, "r")
    
    V = int(f.readline())
    g = Grafo(V)
    for i in range(V-1):
        j = i + 1
        for w in [int(x) for x in f.readline().split()]:
            g.add(i, j, w)
            j += 1
       
    g.DIJKSTRA(0)
            
    
calculaMenorCaminho("instancias-grafo/dij10.txt")
#alculaMenorCaminho("instancias-grafo/dij20.txt")
#alculaMenorCaminho("instancias-grafo/dij40.txt")
#alculaMenorCaminho("instancias-grafo/dij50.txt")