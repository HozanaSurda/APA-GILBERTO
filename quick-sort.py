   ##############################################
     #ALUNA: HOZANA RAQUEL GOMES DE LIMA          #
     #MAT: 11414870                               #
     #DISCIPLINA: ANÁLISE E PROJETOS DE ALGORITMOS#
     #       EXERCICIO DE ORDENACAO               #
     ##############################################


import sortlib
import random

################### QUICK SORT ###########################
# A implementacao tem codigo mais simples e nao economico em memoria.
# O ideal seria usar os indices para tornar a conquista O(1). 

def quicksortaux(lista):
    pivo = lista[0]
    
    parteesquerda = []
    partedireita  = []
    parteigual    = []
    
    for i in range(len(lista)):
        if(lista[i] < pivo):
            parteesquerda.append(lista[i])
        elif(lista[i] > pivo):
            partedireita.append(lista[i])
        else:
            parteigual.append(lista[i])
        
    if(len(parteesquerda) > 1):
        parteesquerda = quicksortaux(parteesquerda)
    
    if(len(partedireita) > 1):
        partedireita = quicksortaux(partedireita)
        
    return parteesquerda + parteigual + partedireita # Conquista - O(n)

def quicksort(lista):
    random.shuffle(lista) #garante que nao cai no pior caso do quick [probabilidade 1/n! de acontecer]
    listaordenada = quicksortaux(lista)
    print(len(listaordenada), len(lista))
    for i in range(len(listaordenada)):
        lista[i] = listaordenada[i]

  
def main():
	entrada = sortlib.le_instancia("instancias-num/num.100000.4.in")
	quicksort(entrada)
	print(entrada)
	sortlib.print_status(entrada)
main()
