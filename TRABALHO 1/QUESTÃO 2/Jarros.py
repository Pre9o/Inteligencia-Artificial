class Jarros:
    """
    Implementação do problema dos Jarros.
    """

    def __init__(self, j1, j2):
        """
        Inicializa o problema dos Jarros.

        Args:
            j1: Capacidade do jarro 1.
            j2: Capacidade do jarro 2.
        """
        self.j1 = j1                      # Capacidade do jarro 1
        self.j2 = j2                      # Capacidade do jarro 2
        self.objetivo = (2, 0)            # Estado objetivo
        self.operacoes = [                # Lista de operações possíveis
            ("enche1", self.encher_j1, lambda estado: estado[0] < 4),
            ("enche2", self.encher_j2, lambda estado: estado[1] < 3),
            ("esvazia1", self.esvaziar_j1, lambda estado: estado[0] > 0),
            ("esvazia2", self.esvaziar_j2, lambda estado: estado[1] > 0),
            ("despeja1em2", self.passar_j1_j2, lambda estado: estado[0] > 0 and estado[1] < 3),
            ("despeja2em1", self.passar_j2_j1, lambda estado: estado[1] > 0 and estado[0] < 4)
        ]

    def encher_j1(self, estado):
        """
        Enche o jarro 1 até a capacidade máxima.

        Args:
            estado: O estado atual.

        Returns:
            O novo estado após encher o jarro 1.
        """
        return (4, estado[1])
        
    def encher_j2(self, estado):
        """
        Enche o jarro 2 até a capacidade máxima.

        Args:
            estado: O estado atual.

        Returns:
            O novo estado após encher o jarro 2.
        """
        return (estado[0], 3)

    def esvaziar_j1(self, estado):
        """
        Esvazia o jarro 1.

        Args:
            estado: O estado atual.

        Returns:
            O novo estado após esvaziar o jarro 1.
        """
        return (0, estado[1])

    def esvaziar_j2(self, estado):
        """
        Esvazia o jarro 2.

        Args:
            estado: O estado atual.

        Returns:
            O novo estado após esvaziar o jarro 2.
        """
        return (estado[0], 0)

    def passar_j1_j2(self, estado):
        """
        Transfere o conteúdo do jarro 1 para o jarro 2.

        Args:
            estado: O estado atual.

        Returns:
            O novo estado após transferir o conteúdo do jarro 1 para o jarro 2.
        """
        if estado[0] + estado[1] <= 3:
            return (0, estado[0] + estado[1])
        else:
            return (estado[0] - (3 - estado[1]), 3)

    def passar_j2_j1(self, estado):
        """
        Transfere o conteúdo do jarro 2 para o jarro 1.

        Args:
            estado: O estado atual.

        Returns:
            O novo estado após transferir o conteúdo do jarro 2 para o jarro 1.
        """
        if estado[0] + estado[1] <= 4:
            return (estado[0] + estado[1], 0)
        else:
            return (4, estado[1] - (4 - estado[0]))

    def estadoInicial(self):
        """
        Retorna o estado inicial do problema.

        Returns:
            O estado inicial do problema.
        """
        return ('inicio', (0, 0))
    
    def testeObjetivo(self, estado):
        """
        Verifica se o estado é o estado objetivo.

        Args:
            estado: O estado a ser verificado.

        Returns:
            True se o estado for o objetivo, False caso contrário.
        """
        _, estado_int = estado
        return estado_int == self.objetivo
    
    def funcaoSucessora(self, estado):
        """
        Gera os sucessores do estado dado.

        Args:
            estado: O estado atual.

        Returns:
            Uma lista de estados sucessores válidos.
        """
        sucessores = []
        _, estado_int = estado 

        for nome, operacao, condicao in self.operacoes:
            if condicao(estado_int): 
                sucessor = operacao(estado_int)  
                if self.validaEstado(sucessor):
                    sucessores.append((nome, sucessor))
                    
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
        if estado[0] < 0 or estado[1] < 0 or estado[0] > 4 or estado[1] > 3:
            return False

        return True
