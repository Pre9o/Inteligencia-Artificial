class MissionariosCanibais():
    """
    Implementação do problema dos Missionários e Canibais.
    """

    def __init__(self, missionarios, canibais, lado, tamanho_barco):
        """
        Inicializa o problema dos Missionários e Canibais.

        Args:
            missionarios: O número inicial de missionários.
            canibais: O número inicial de canibais.
            lado: O lado onde está o barco (0 para esquerda, 1 para direita).
            tamanho_barco: O tamanho máximo do barco.
        """
        self.missionarios = missionarios      # Número de missionários
        self.canibais = canibais              # Número de canibais
        self.lado = lado                      # Lado do rio onde está o barco
        self.objetivo = (0, 0, 0)             # Estado objetivo
        self.tamanho_barco = tamanho_barco    # Tamanho máximo do barco
        
    def estadoInicial(self):
        """
        Retorna o estado inicial do problema.

        Returns:
            O estado inicial do problema.
        """
        return (self.missionarios, self.canibais, self.lado)
    
    def testeObjetivo(self, estado):
        """
        Verifica se o estado é o estado objetivo.

        Args:
            estado: O estado a ser verificado.

        Returns:
            True se o estado for o objetivo, False caso contrário.
        """
        return estado == self.objetivo
    
    def funcaoSucessora(self, estado):
        """
        Gera os sucessores do estado dado.

        Args:
            estado: O estado atual.

        Returns:
            Uma lista de estados sucessores válidos.
        """
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
        """
        Valida se o estado é válido.

        Args:
            estado: O estado a ser validado.

        Returns:
            True se o estado for válido, False caso contrário.
        """
        # Verifica se o estado é válido
        if estado[0] < 0 or estado[1] < 0 or estado[0] > self.missionarios or estado[1] > self.canibais:
            return False
        
        if estado[0] != 0 and estado[0] < estado[1]:
            return False
        
        if self.missionarios - estado[0] != 0 and self.missionarios - estado[0] < self.canibais - estado[1]:
            return False
        
        return True 
