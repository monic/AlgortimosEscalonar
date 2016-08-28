#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Elevador:
    """
    Algoritmo de escalonamento Elevador. O braco se movimenta inicialmente
    em direcao ao cilindro mais externo do disco.
    """

    def execute(self, ultimo_cilindro, cilindro_inicial, requisicoes):
        """
        Executa o algoritmo. Recebe como parametros o ultimo cilindro, o
        cilindro inicial onde esta o braco e as requisicoes de acesso
        subsequentes
        """
        # Inicializa o contador de cilindros percorridos com zero
        cilindros_percorridos = 0

        # Configura a posicao inicial do braco do disco
        posicao_atual = cilindro_inicial

        # Obtem as requisicoes que estao abaixo do cilindro inicial
        menores = filter(lambda x: x < posicao_atual, requisicoes)
        # Coloca as requisicoes em ordem decrescente para a descida do elevador


        # Obtem as requisicoes que estao acima do cilindro inicial
        maiores = filter(lambda x: x > posicao_atual, requisicoes)
        # Coloca as requisicoes em ordem crescente para a subida do elevador


        # Atende primeiro as requisicoes acima do cilindro inicial
        for requisicao in maiores:
            cilindros_percorridos += int(math.fabs(requisicao - posicao_atual))
            posicao_atual = requisicao

        # Em seguida atende as requisicoes abaixo do cilindro inicial
        for requisicao in menores:
            cilindros_percorridos += int(math.fabs(requisicao - posicao_atual))
            posicao_atual = requisicao


        # Retorna o numero de cilindros percorridos
        return cilindros_percorridos