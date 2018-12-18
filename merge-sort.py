   ##############################################
     #ALUNA: HOZANA RAQUEL GOMES DE LIMA          #
     #MAT: 11414870                               #
     #DISCIPLINA: ANÁLISE E PROJETOS DE ALGORITMOS#
     #       EXERCICIO DE ORDENACAO               #
     ##############################################


import sortlib


################### MERGE SORT ###########################

def intercalacao(listaOriginal, metadeEsquerda, metadeDireita):
    e = 0
    d = 0
    for o in range(len(listaOriginal)):
        if (e >= len(metadeEsquerda)):
            listaOriginal[o] = metadeDireita[d]
            d += 1
        elif (d >= len(metadeDireita)):
            listaOriginal[o] = metadeEsquerda[e]
            e += 1
        elif (metadeEsquerda[e] < metadeDireita[d]):
            listaOriginal[o] = metadeEsquerda[e]
            e += 1
        else:
            listaOriginal[o] = metadeDireita[d]
            d += 1
    
################### OBSERVACAO ###########################
# A implementacao tem codigo mais simples e nao economico em memoria, 
# porque o algoritmo eh recursivo e cria 3 listas em cada recursao,
# que sao: o parametro  'lista' e as duas metades do parametro [como descrito no algoritmo].
# O ideal seria usar os indices ! 
def mergesort(lista):
    if(len(lista) > 1):
        indiceDoMeio   = len(lista)//2
        
        metadeEsquerda = lista[:indiceDoMeio]
        mergesort(metadeEsquerda)
        
        metadeDireita  = lista[indiceDoMeio:]
        mergesort(metadeDireita)
        
        intercalacao(lista, metadeEsquerda, metadeDireita)
  
def main():
	entrada = sortlib.le_instancia("instancias-num/num.100000.4.in")
	mergesort(entrada)
	print(entrada)
	sortlib.print_status(entrada)
main()
