
##############################################
#ALUNA: HOZANA RAQUEL GOMES DE LIMA          #
#MAT: 11414870                               #
#DISCIPLINA: ANÁLISE E PROJETOS DE ALGORITMOS#
#       EXERCICIO DE ORDENACAO               #
##############################################

import sortlib

def insertionSort(vetor):
    pivo = 0
    j = 0
    i = 1
    for i in range(len(vetor)):
        pivo = vetor[i]
        j = i - 1
        while ((j >= 0) & (vetor[j] > pivo)):
            vetor[j+1] = vetor[j]
            j = j - 1
        vetor[j+1] = pivo
        i = i + 1
    print (vetor)

def main():
    entrada = sortlib.le_instancia("instancias-num/num.1000.1.in")
    insertionSort(entrada)
    print(entrada)
    sortlib.print_status(entrada)
    
main()
