#ANALISE E PROJETO DE ALGORITMOS#
#ALUNA: HOZANA RAQUEL GOMES DE LIMA#
#MAT: 11414870#
#ALGORITMO DE KRUSKAL#

class Grafo:

    def __init__(self,vertices):
        self.V = vertices 
        self.G = []
        self.PAI = [i for i in range(vertices)]
        #print(self.PAI)

    #adiciona aresta
    def add(self, x, y, w):
        self.G.append([x, y, w])

    def raiz(self, i):
        if self.PAI[i] == i:
            return i
        return self.raiz(self.PAI[i])

    def unir(self, x, y):
        xr = self.raiz(x)
        yr = self.raiz(y)
        self.PAI[xr] = yr

    def KruskalMST(self):
        self.G =  sorted(self.G, key = lambda item : item[2])
        
        MST =[] 
        for e in range(len(self.G)):
            x, y, w =  self.G[e]
            
            xr = self.raiz(x)
            yr = self.raiz(y)

            if xr != yr:
                MST.append([x, y, w])
                self.unir(x, y)          

        w_tot = 0
        #print ("\tArestas da MST:")
        for x, y, w  in MST:
            #print ("\t\t%d -- %d com peso %d" % (x, y, w))
            w_tot += w
        
        print('Custo da Arvore:', w_tot)
 

def calculaMST(instancia):
    print("Instancia Kruskal:", instancia)
    
    f = open(instancia, "r")
    
    V = int(f.readline())
    g = Grafo(V)
    for i in range(V-1):
        j = i + 1
        for w in [int(x) for x in f.readline().split()]:
            g.add(i, j, w)
            j += 1
       
    g.KruskalMST()
            
    
calculaMST("instancias-grafo/dij10.txt")
calculaMST("instancias-grafo/dij20.txt")
calculaMST("instancias-grafo/dij40.txt")
calculaMST("instancias-grafo/dij50.txt")