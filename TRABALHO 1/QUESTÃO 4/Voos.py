class Voos:
    """
    Implementação de um problema de busca em grafo representando voos entre cidades.
    """

    def __init__(self, origem, destino):
        """
        Inicializa o problema de voos com uma lista de voos disponíveis, origem e destino.

        Args:
            origem: A cidade de origem.
            destino: A cidade de destino.
        """
        self.voos = [
            (1, 'a', 'b'),
            (2, 'a', 'b'),
            (3, 'a', 'd'),
            (4, 'b', 'e'),
            (5, 'b', 'f'),
            (6, 'c', 'g'),
            (7, 'c', 'h'),
            (8, 'c', 'i'),
            (9, 'd', 'j'),
            (10, 'e', 'k'),
            (11, 'e', 'l'),
            (12, 'g', 'm'),
            (13, 'j', 'n'),
            (14, 'j', 'o'),
            (15, 'k', 'f'),
            (16, 'l', 'h'),
            (17, 'm', 'd'),
            (18, 'o', 'a'),
            (19, 'n', 'b')
        ]
        
        self.origem = origem
        self.destino = destino
        
    def estadoInicial(self):
        """
        Retorna a cidade de origem como estado inicial.

        Returns:
            str: A cidade de origem.
        """
        return self.origem
    
    def testeObjetivo(self, estado):
        """
        Verifica se o estado é o destino.

        Args:
            estado: O estado a ser verificado.

        Returns:
            bool: True se o estado é o destino, False caso contrário.
        """
        return estado == self.destino
    
    def funcaoSucessora(self, estado):
        """
        Retorna uma lista de possíveis estados sucessores para o estado atual.

        Args:
            estado: O estado atual.

        Returns:
            list: Uma lista de tuplas (voo, destino).
        """
        return [(voo, destino) for voo, origem, destino in self.voos if origem == estado]
    
    def validaEstado(self, estado):
        """
        Verifica se o estado é válido, ou seja, se é uma cidade de origem ou destino de algum voo.

        Args:
            estado: O estado a ser verificado.

        Returns:
            bool: True se o estado é válido, False caso contrário.
        """
        return estado in [origem for voo, origem, destino in self.voos] + [destino for voo, origem, destino in self.voos]
