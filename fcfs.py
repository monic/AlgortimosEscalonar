import math

class FCFS:

    def execute(self, inicio,requisicoes):
        # Inicializa o contador de cilindros percorridos com zero
        setores_cilindro = 0
        # Configura a posicao inicial do braco do disco
        posicao_atual = inicio

        # Percorre os cilindros
        for requisicao in requisicoes:
            setores_cilindro += int(math.fabs(requisicao - posicao_atual))
            posicao_atual = requisicao

        # Retorna o numero de cilindros percorridos
        return setores_cilindro
    