import math

class SSF:

    def ssf(self,inicio,requisicoes):
        setores_cilindro = 0
        posicao_atual = inicio

        for requisicoes in range(len(requisicoes)):
            inc = self.__menor_distacia(posicao_atual, requisicoes)
            setores_cilindro +=int(math.fabs(requisicoes[inc] - posicao_atual))
            posicao_atual = requisicoes[inc]
            requisicoes.pop(inc) #remove a utltima requisição
        return setores_cilindro

    def __menor_distancia(self, posicao_atual,requisicoes):
        menor = int(math.fabs(posicao_atual -max(requisicoes))) +1
        valor_menor = -1

        for valor,requisicoes in enumerate(requisicoes):
            tamanho = int(math.fabs(requisicoes - posicao_atual))
            if tamanho < menor:
                menor = tamanho

        return valor_menor #Retorna o indice com menor requisição
    
