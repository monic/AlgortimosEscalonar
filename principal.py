import sys
from fifo import *
from ssf import *
from  elevador import *
import copy

def main():
    ultimo = int(sys.stdin.readline()) #Leitura do ultimo número
    inicio = int(sys.stdin.readline()) #Leitura do inicio
    requisicoes = map(int,sys.stdin.readline())

    # Instanciando os objetos da classe
    fifo = FIFO()
    leitura_fifo = fifo.fifo(inicio,requisicoes)

    #Instanciando o algortimo SSF
    ssf = SSF()
    leitura_ssf = ssf.ssf(inicio, copy.deepcopy(requisicoes))

    #Instanciando o algortimo do elevador
    elevador = Elevador()
    leitura_elevador = elevador.elevador(ultimo,inicio,requisicoes)

    #Saida dos valores
    saida = 'FIFO {0}\nSSF {1}\nElevador{2}'

    #Apresenta a saída dos valores
    print(saida.format(leitura_fifo,leitura_ssf,leitura_elevador))

if __name__ == "__main__":
    main()

