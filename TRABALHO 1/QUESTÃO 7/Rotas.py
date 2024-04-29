class Rotas:
    """
    Classe que representa um conjunto de rotas entre cidades.

    Args:
        origem (str): A cidade de origem.
        destino (str): A cidade de destino.

    Attributes:
        rotas (list): Uma lista de tuplas contendo as rotas disponíveis, cada uma representada por uma tupla no formato (origem, destino, custo).
        origem (str): A cidade de origem.
        destino (str): A cidade de destino.

    Methods:
        estadoInicial(): Retorna o estado inicial, que é a cidade de origem.
        testeObjetivo(estado): Verifica se o estado atual é o estado objetivo, ou seja, a cidade de destino.
        funcaoSucessora(estado): Retorna uma lista de ações possíveis a partir do estado atual.
        custo(estado, acao): Retorna o custo associado a uma determinada ação a partir do estado atual.
        validaEstado(estado): Verifica se um estado é válido, ou seja, se está presente nas rotas.
        heuristica(estado): Retorna o valor da heurística para um determinado estado.

    """

    def __init__(self, origem, destino):
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
        return self.origem
    
    def testeObjetivo(self, estado):
        return estado == self.destino
    
    def funcaoSucessora(self, estado):
        return [(destino, destino) for origem, destino, custo in self.rotas if origem == estado]
    
    def custo(self, estado, acao):
        return [custo for origem, destino, custo in self.rotas if origem == estado and destino == acao][0]
    
    def validaEstado(self, estado):
        return estado in [origem for origem, destino, custo in self.rotas] + [destino for origem, destino, custo in self.rotas]
    
    def heuristica(self, estado):
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