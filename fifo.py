import math

class FIFO:

    def fifo(self, inicio,requisicoes):
        setores_cilindro = 0
        posicao_atual = inicio

        menor = filter(lambda x:x < posicao_atual,requisicoes) #Retornando uma função
        menor.sort()
        menor.reverse()

        maior = filter(lambda x:x > posicao_atual,requisicoes)
        maior.sort()

        for requisicoes in maior:
            setores_cilindro += int(math.fabs(requisicoes - posicao_atual))
            posicao_atual = requisicoes

        for requisicoes in menor:
            setores_cilindro += int(math.fabs(requisicoes -posicao_atual))
            posicao_atual = requisicoes

        return setores_cilindro
    