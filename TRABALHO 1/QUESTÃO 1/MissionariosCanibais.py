class MissionariosCanibais():
    def __init__(self, missionarios, canibais, lado, tamanho_barco):
        self.missionarios = missionarios
        self.canibais = canibais
        self.lado = lado
        self.objetivo = (0, 0, 0)
        self.tamanho_barco = tamanho_barco
        
    def estadoInicial(self):
        return (self.missionarios, self.canibais, self.lado)
    
    def testeObjetivo(self, estado):
        return estado == self.objetivo
    
    def funcaoSucessora(self, estado):
        sucessores = []
        
        if estado[2] == 1:
            # Se o barco está no lado direito
            for i in range(self.tamanho_barco + 1):
                for j in range(self.tamanho_barco + 1):
                    if i + j <= self.tamanho_barco and i + j > 0:
                        # Gera os sucessores
                        sucessor = (estado[0] - i, estado[1] - j, 0)
                        if self.validaEstado(sucessor):
                            sucessores.append(sucessor)
        else:
            # Se o barco está no lado esquerdo
            for i in range(self.tamanho_barco + 1):
                for j in range(self.tamanho_barco + 1):
                    if i + j <= self.tamanho_barco and i + j > 0:
                        # Gera os sucessores
                        sucessor = (estado[0] + i, estado[1] + j, 1)
                        if self.validaEstado(sucessor):
                            sucessores.append(sucessor)
        
        return sucessores
    
    
    def validaEstado(self, estado):
        # Verifica se o estado é válido
        if estado[0] < 0 or estado[1] < 0 or estado[0] > self.missionarios or estado[1] > self.canibais:
            return False
        
        if estado[0] != 0 and estado[0] < estado[1]:
            return False
        
        if self.missionarios - estado[0] != 0 and self.missionarios - estado[0] < self.canibais - estado[1]:
            return False
        
        return True 
        