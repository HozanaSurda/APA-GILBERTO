
##############################################
#ALUNA: HOZANA RAQUEL GOMES DE LIMA          #
#MAT: 11414870                               #
#DISCIPLINA: ANÁLISE E PROJETOS DE ALGORITMOS#
#       EXERCICIO DE ORDENACAO               #
##############################################

import sortlib

def selectionSort(vetor):
    i = 0
    i_min = 0
    j = 0
    temp = 0
    for i in range(len(vetor)):
        i_min = i
        j = i + 1
        while j < len(vetor):
            if (vetor[j] < vetor[i_min]):
                i_min = j
            j += 1
        if (vetor[i] != vetor[i_min]):
            temp = vetor[i]
            vetor[i] = vetor[i_min]
            vetor[i_min] = temp
  
def main():
	entrada = sortlib.le_instancia("instancias-num/num.1000.1.in")
	selectionSort(entrada)
	print(entrada)
	sortlib.print_status(entrada)
main()
