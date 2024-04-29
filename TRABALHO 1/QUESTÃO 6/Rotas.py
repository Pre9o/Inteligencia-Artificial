class Rotas:
    def __init__(self, origem, destino):
        """
        Inicializa o problema de rotas com a origem e destino especificados.

        :param origem: O ponto de origem das rotas.
        :type origem: str
        :param destino: O ponto de destino das rotas.
        :type destino: str
        """
        self.rotas = [
            ('a', 'b', 7),
            ('a', 'c', 9),
            ('a', 'd', 3),
            ('b', 'i', 4),
            ('b', 'f', 3),
            ('c', 'j', 5),
            ('d', 'e', 1),
            ('f', 'g', 2),
            ('g', 'h', 3),
            ('i', 'k', 5),
            ('j', 'l', 6),
            ('l', 'k', 4)
        ]

        self.origem = origem
        self.destino = destino

    def estadoInicial(self):
        """
        Retorna o estado inicial do problema.

        :return: O ponto de origem das rotas.
        :rtype: str
        """
        return self.origem
    
    def testeObjetivo(self, estado):
        """
        Verifica se o estado atual é o objetivo do problema.

        :param estado: O estado atual.
        :type estado: str
        :return: True se o estado é o objetivo, False caso contrário.
        :rtype: bool
        """
        return estado == self.destino
    
    def funcaoSucessora(self, estado):
        """
        Retorna os possíveis estados sucessores do estado atual.

        :param estado: O estado atual.
        :type estado: str
        :return: Uma lista de tuplas contendo os estados sucessores e as ações correspondentes.
        :rtype: list[(str, str)]
        """
        return [(destino, destino) for origem, destino, custo in self.rotas if origem == estado]
    
    def custo(self, estado, acao):
        """
        Retorna o custo de uma determinada ação a partir de um estado.

        :param estado: O estado atual.
        :type estado: str
        :param acao: A ação a ser realizada a partir do estado atual.
        :type acao: str
        :return: O custo da ação a partir do estado atual.
        :rtype: int
        """
        return [custo for origem, destino, custo in self.rotas if origem == estado and destino == acao][0]
    
    def validaEstado(self, estado):
        """
        Verifica se um estado é válido, ou seja, se ele está presente nas rotas.

        :param estado: O estado a ser verificado.
        :type estado: str
        :return: True se o estado é válido, False caso contrário.
        :rtype: bool
        """
        return estado in [origem for origem, destino, custo in self.rotas] + [destino for origem, destino, custo in self.rotas]
    
    def heuristica(self, estado):
        """
        Retorna a heurística associada a um determinado estado.

        :param estado: O estado atual.
        :type estado: str
        :return: O valor da heurística para o estado atual.
        :rtype: int
        """
        funcao_heuristica = [
            ('a', 15),
            ('b', 7),
            ('c', 6),
            ('d', 14),
            ('e', 15),
            ('f', 7),
            ('g', 8),
            ('h', 5),
            ('i', 5),
            ('j', 3),
            ('k', 0),
            ('l', 4)
        ]

        return [custo for cidade, custo in funcao_heuristica if cidade == estado][0]
