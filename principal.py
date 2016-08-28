import sys
from fcfs import *
from sstf import *
from elevador import *
import copy


def main():
    arquivo = open("entrada.txt")
    conteudo = []
    #Realiza a leitura das linhas do arquivo
    for line in arquivo:
        conteudo.append(int(line))
    # Leitura do ultimo número
    ultimo = int (conteudo[0])
    # Leitura do inicio
    inicio = int(conteudo [1])
    #Leitura das requisições de acesso
    requisicoes = conteudo[2:]

    # Instanciando os objetos da classe
    fcfs = FCFS()
    leitura_fcfs = fcfs.fcfs(inicio,requisicoes)

    #Instanciando o algortimo SSF
    sstf = SSTF()
    leitura_sstf = sstf.sstf(inicio, copy.deepcopy(requisicoes))

    #Instanciando o algortimo do elevador
    elevador = Elevador()
    leitura_elevador = elevador.elevador(ultimo,inicio,requisicoes)

    # Exibe a saida
    print("-------------------------------------")
    print("|        Resultados obtidos         |")
    print("-------------------------------------")
    print("|   FCFS  |", leitura_fcfs, " setores percorridos|")
    print("-------------------------------------")
    print("|   SSTF  |", leitura_sstf, " setores percorridos|")
    print("-------------------------------------")
    print("| Elevador|", leitura_elevador, " setores percorridos|")
    print("-------------------------------------")


if __name__ == "__main__":
    main()

