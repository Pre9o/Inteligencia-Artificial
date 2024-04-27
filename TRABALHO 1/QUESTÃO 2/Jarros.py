class Jarros:
    def __init__(self, j1, j2):
        self.j1 = j1
        self.j2 = j2
        self.objetivo = (2, 0)
        self.operacoes = [
            ("enche1", self.encher_j1, lambda estado: estado[0] < 3),
            ("enche2", self.encher_j2, lambda estado: estado[1] < 4),
            ("esvazia1", self.esvaziar_j1, lambda estado: estado[0] > 0),
            ("esvazia2", self.esvaziar_j2, lambda estado: estado[1] > 0),
            ("despeja1em2", self.passar_j1_j2, lambda estado: estado[0] > 0 and estado[0] <= 4),
            ("despeja2em1", self.passar_j2_j1, lambda estado: estado[1] > 0 and estado[1] <= 3)
        ]

    def encher_j1(self, estado):
        return (4, estado[1])
        
    def encher_j2(self, estado):
        return (estado[0], 3)

    def esvaziar_j1(self, estado):
        return (0, estado[1])

    def esvaziar_j2(self, estado):
        return (estado[0], 0)

    def passar_j1_j2(self, estado):
        if estado[0] + estado[1] <= 3:
            return (0, estado[0] + estado[1])
        else:
            return (estado[0] - (3 - estado[1]), 3)

    def passar_j2_j1(self, estado):
        if estado[0] + estado[1] <= 4:
            return (estado[0] + estado[1], 0)
        else:
            return (4, estado[1] - (4 - estado[0]))


    def estadoInicial(self):
        return ('inicio', (0, 0))
    
    def testeObjetivo(self, estado):
        _, estado_int = estado
        return estado_int == self.objetivo
    
    def funcaoSucessora(self, estado):
        sucessores = []
        _, estado_int = estado 

        for nome, operacao, condicao in self.operacoes:
            if condicao(estado_int): 
                sucessor = operacao(estado_int)  
                if self.validaEstado(sucessor):
                    sucessores.append((nome, sucessor))
                    

        return sucessores
    
    def validaEstado(self, estado):
        # Verifica se o estado é válido
        if estado[0] < 0 or estado[1] < 0 or estado[0] > 4 or estado[1] > 3:
            return False

        return True
            