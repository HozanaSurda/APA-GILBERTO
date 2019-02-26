
##############################################
#ALUNA: HOZANA RAQUEL GOMES DE LIMA          #
#MAT: 11414870                               #
#DISCIPLINA: ANÁLISE E PROJETOS DE ALGORITMOS#
#       EXERCICIO DE ORDENACAO               #
##############################################

import sortlib

#Usado para adaptar arrays com valores negativos (soma valor a todas as posicoes de V)
def countAux(V, valor):
        i = 0
        while i < len(V):
            V[i] += valor
            i += 1
        
def countSort(V):
    #ajeita vetores com valores negativos
    menor_elemento = min(V)
    if menor_elemento < 0:
        countAux(V, -menor_elemento)
        
    #encontra maior elemento
    maior_elemento = max(V) + 1
    
    #C eh uma lista de zeros para contagem (tamanho de maior elemento)
    C = [0] * maior_elemento
    
    #contagem
    i = 0
    for el in V:
        C[el] += 1
    
    #faz a soma das contagens
    i = 1
    while i < len(C):           
        C[i] = C[i] + C[i-1]
        i   += 1
    
        #copia V para B
    B = V[:]
    
    #ordena
    i = 0
    while i < len(B):
        C[B[i]] -= 1
        pos      = C[B[i]]
        V[pos]   = B[i]
        i       += 1

        #ajeita vetores com valores negativos
    if menor_elemento < 0:
        countAux(V, menor_elemento)
        

  
def main():
    entrada = sortlib.le_instancia("instancias-num/num.1000.1.in")
    countSort(entrada)
    print(entrada)
    sortlib.print_status(entrada)
        
main()
