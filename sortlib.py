
##############################################
#ALUNA: HOZANA RAQUEL GOMES DE LIMA          #
#MAT: 11414870                               #
#DISCIPLINA: ANÁLISE E PROJETOS DE ALGORITMOS#
#       EXERCICIO DE ORDENACAO               #
##############################################

def le_instancia(instancia):
    print("Instancia", instancia)
    f = open(instancia, "r")
    N = int(f.readline())
    vetor = []
    for i in range(N):
        vetor.append(int(f.readline()))
    return vetor

def ordenado(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))

def print_status(vetor):
    if ordenado(vetor):
        print("Vetor foi ordenado com sucesso")
    else:
        print("O vetor nao foi ordenado. Houve algum erro.")
