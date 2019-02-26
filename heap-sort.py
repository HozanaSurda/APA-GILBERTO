
##############################################
#ALUNA: HOZANA RAQUEL GOMES DE LIMA          #
#MAT: 11414870                               #
#DISCIPLINA: ANÁLISE E PROJETOS DE ALGORITMOS#
#       EXERCICIO DE ORDENACAO               #
##############################################

import sortlib

def heapify(V, raiz, tam):
    m = raiz          # maior valor
    e = 2 * m + 1     # esquerda = 2*i + 1 
    d = 2 * m + 2     # direita  = 2*i + 2 
  
    #filho da esquerda maior que a raiz
    if e < tam and V[m] < V[e]: 
        m = e 

    #filho da direita maior que raiz
    if d < tam and V[m] < V[d]: 
        m = d 
  
    # se a raiz mudou entao recursao 
    if m != raiz: 
        V[raiz],V[m] = V[m],V[raiz] # swap
        heapify(V, m, tam) 
  
def heapSort(V):
    n = len(V)
    for i in range(n//2, -1, -1): 
        heapify(V, i, n) 
    #usa o heap para ordenar
    for i in range(n-1, 0, -1): 
        V[i], V[0] = V[0], V[i] # swap 
        heapify(V, 0, i)
        
def main():
	entrada = sortlib.le_instancia("instancias-num/num.1000.1.in")
	heapSort(entrada)
	print(entrada)
	sortlib.print_status(entrada)
main()
