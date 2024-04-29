class QuebraCabeca:
    def __init__(self, origem, objetivo, funcaoCusto):
        self.origem = origem
        self.objetivo = objetivo
        self.funcaoCusto = funcaoCusto

    def estadoInicial(self):
        return self.origem
    
    def testeObjetivo(self, estado):
        return estado == self.objetivo
    
    def funcaoSucessora(self, estado):
        # Encontra a posição do zero
        posicao_zero = estado.index(0)
        
        # Encontra as posições possíveis para mover o zero
        posicoes_possiveis = []
        if posicao_zero % 3 != 0:
            posicoes_possiveis.append(posicao_zero - 1)
        if posicao_zero % 3 != 2:
            posicoes_possiveis.append(posicao_zero + 1)
        if posicao_zero > 2:
            posicoes_possiveis.append(posicao_zero - 3)
        if posicao_zero < 6:
            posicoes_possiveis.append(posicao_zero + 3)
        
        # Gera os sucessores
        sucessores = []
        for posicao in posicoes_possiveis:
            sucessor = estado.copy()
            sucessor[posicao_zero], sucessor[posicao] = sucessor[posicao], sucessor[posicao_zero]
            sucessores.append((sucessor[posicao], sucessor))
        
        return sucessores
    
    def heuristica(self, estado):
        if self.funcaoCusto == 1:
            return 1
        
        if self.funcaoCusto == 2:
            return sum([1 if estado[i] != self.objetivo[i] else 0 for i in range(9)])
