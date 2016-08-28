#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class SSTF:
    """Algoritmo de escalonamento Shortest Seek Time First (SSTF)"""

    def execute(self, cilindro_inicial, requisicoes):
        """
        Executa o algoritmo. Recebe como parametros o cilindro inicial onde
        esta o braco e as requisicoes de acesso subsequentes
        """
        # Inicializa o contador de cilindros percorridos com zero
        cilindros_percorridos = 0

        # Configura a posicao inicial do braco do disco
        posicao_atual = cilindro_inicial

        for requisicao in range(len(requisicoes)):
            # Obtem o indice da proxima requisicao a ser atendida
            i = self.__menor_distancia(posicao_atual, requisicoes)
            cilindros_percorridos += int(math.fabs(requisicoes[i] - posicao_atual))
            posicao_atual = requisicoes[i]
            # Remove a ultima requisicao atendida da lista de requisicoes
            requisicoes.pop(i)

        # Retorna o numero de cilindros percorridos
        return cilindros_percorridos


    def __menor_distancia(self, posicao_atual, requisicoes):
        """
        Metodo privado da classe que retorna o indice da proxima requisicao
        a ser atendida, ou seja, a requisicao com menor deslocamento do braco
        """

        # Configura a menor distancia como a maior entre as restantes mais 1
        menor = int(math.fabs(posicao_atual - max(requisicoes))) + 1
        indice_menor = -1

        # Busca a requisicao com menor deslocamento do braco
        for indice, requisicao in enumerate(requisicoes):
            distancia = int(math.fabs(requisicao - posicao_atual))
            if distancia < menor:
                menor = distancia
                indice_menor = indice

        # Retorna o indice da requisicao com menor deslocamento do braco
        return indice_menor