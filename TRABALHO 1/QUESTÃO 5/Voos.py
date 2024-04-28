class Voos:
    def __init__(self, origem, destino):
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
        return self.origem
    
    def testeObjetivo(self, estado):
        return estado == self.destino
    
    def funcaoSucessora(self, estado):
        return [(destino, destino) for origem, destino, custo in self.voos if origem == estado]
    
    def custo(self, estado, acao):
        return [custo for origem, destino, custo in self.voos if origem == estado and destino == acao][0]
    
    def validaEstado(self, estado):
        return estado in [origem for origem, destino, custo in self.voos] + [destino for origem, destino, custo in self.voos]
    
    def heuristica(self, estado):
        voos_a_partir_do_estado = [custo for origem, destino, custo in self.voos if origem == estado]
        if voos_a_partir_do_estado:
            return min(voos_a_partir_do_estado)
        else:
            return float('inf')  # Se não há voos a partir do estado, retorna infinito