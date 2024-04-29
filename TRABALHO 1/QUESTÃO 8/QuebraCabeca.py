class QuebraCabeca:
    """
    Classe que representa um quebra-cabeça.

    Args:
        origem (list): O estado inicial do quebra-cabeça.
        objetivo (list): O estado objetivo que se deseja alcançar.
        funcaoCusto (int): O tipo de função de custo a ser utilizada.

    Attributes:
        origem (list): O estado inicial do quebra-cabeça.
        objetivo (list): O estado objetivo que se deseja alcançar.
        funcaoCusto (int): O tipo de função de custo a ser utilizada.

    Methods:
        estadoInicial(): Retorna o estado inicial do quebra-cabeça.
        testeObjetivo(estado): Verifica se o estado atual é o estado objetivo.
        funcaoSucessora(estado): Gera os estados sucessores a partir do estado atual.
        heuristica(estado): Calcula a heurística do estado atual.

    """

    def __init__(self, origem, objetivo, funcaoCusto):
        self.origem = origem
        self.objetivo = objetivo
        self.funcaoCusto = funcaoCusto

    def estadoInicial(self):
        """
        Retorna o estado inicial do quebra-cabeça.

        Returns:
            list: O estado inicial do quebra-cabeça.

        """
        return self.origem
    
    def testeObjetivo(self, estado):
        """
        Verifica se o estado atual é o estado objetivo.

        Args:
            estado (list): O estado atual do quebra-cabeça.

        Returns:
            bool: True se o estado atual é o estado objetivo, False caso contrário.

        """
        return estado == self.objetivo
    
    def funcaoSucessora(self, estado):
        """
        Gera os estados sucessores a partir do estado atual.

        Args:
            estado (list): O estado atual do quebra-cabeça.

        Returns:
            list: Uma lista de tuplas contendo os estados sucessores e a ação que levou a cada estado.

        """
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
        """
        Calcula a heurística do estado atual.

        Args:
            estado (list): O estado atual do quebra-cabeça.

        Returns:
            int: O valor da heurística calculada.

        """
        if self.funcaoCusto == 1:
            return 1
        
        if self.funcaoCusto == 2:
            return sum([1 if estado[i] != self.objetivo[i] else 0 for i in range(9)])
