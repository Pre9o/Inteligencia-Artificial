class Voos:
    """
    Representa o problema dos voos, onde se busca encontrar um caminho entre uma origem e um destino.

    Attributes:
        voos (list): Lista de tuplas contendo informações sobre os voos disponíveis, cada tupla contém (origem, destino, custo).
        origem (str): Origem dos voos.
        destino (str): Destino dos voos.
    """

    def __init__(self, origem, destino):
        """
        Inicializa o problema dos voos com uma origem e um destino.

        Args:
            origem (str): Origem dos voos.
            destino (str): Destino dos voos.
        """
        self.voos = [
            ('a', 'b', 1),
            ('a', 'c', 9),
            ('a', 'd', 4),
            ('b', 'c', 7),
            ('b', 'e', 6),
            ('b', 'f', 1),
            ('c', 'f', 7),
            ('d', 'f', 4),
            ('d', 'g', 5),
            ('e', 'h', 9),
            ('f', 'h', 4),
            ('g', 'h', 1)    
        ]
        self.origem = origem
        self.destino = destino

    def estadoInicial(self):
        """
        Retorna o estado inicial do problema.

        Returns:
            str: Estado inicial do problema.
        """
        return self.origem

    def testeObjetivo(self, estado):
        """
        Verifica se um estado é o estado objetivo.

        Args:
            estado (str): Estado a ser verificado.

        Returns:
            bool: True se o estado é o estado objetivo, False caso contrário.
        """
        return estado == self.destino

    def funcaoSucessora(self, estado):
        """
        Retorna os estados sucessores de um estado dado.

        Args:
            estado (str): Estado atual.

        Returns:
            list: Lista de tuplas contendo os estados sucessores no formato (ação, estado).
        """
        return [(destino, destino) for origem, destino, custo in self.voos if origem == estado]

    def custo(self, estado, acao):
        """
        Retorna o custo de realizar uma ação em um estado.

        Args:
            estado (str): Estado atual.
            acao (str): Ação a ser realizada.

        Returns:
            int: Custo da ação.
        """
        return [custo for origem, destino, custo in self.voos if origem == estado and destino == acao][0]

    def validaEstado(self, estado):
        """
        Verifica se um estado é válido.

        Args:
            estado (str): Estado a ser verificado.

        Returns:
            bool: True se o estado é válido, False caso contrário.
        """
        return estado in [origem for origem, destino, custo in self.voos] + [destino for origem, destino, custo in self.voos]

    def heuristica(self, estado):
        """
        Retorna uma heurística para o estado dado.

        Args:
            estado (str): Estado atual.

        Returns:
            int: Valor da heurística para o estado.
        """
        voos_a_partir_do_estado = [custo for origem, destino, custo in self.voos if origem == estado]
        if voos_a_partir_do_estado:
            return min(voos_a_partir_do_estado)
        else:
            return float('inf')  # Se não há voos a partir do estado, retorna infinito
