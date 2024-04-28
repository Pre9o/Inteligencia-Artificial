class Voos:
    def __init__(self, origem, destino):
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
        return self.origem
    
    def testeObjetivo(self, estado):
        return estado == self.destino
    
    def funcaoSucessora(self, estado):
        return [(voo, destino) for voo, origem, destino in self.voos if origem == estado]
    
    def validaEstado(self, estado):
        return estado in [origem for voo, origem, destino in self.voos] + [destino for voo, origem, destino in self.voos]