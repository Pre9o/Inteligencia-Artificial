class BuscaEmLargura:
    """
    Implementação de um algoritmo de busca em largura.
    """

    def __init__(self):
        """
        Inicializa a classe de busca em largura.

        Fronteira é a lista de estados a serem explorados.
        Visitados é a lista de estados já visitados.
        Solução é a sequência de estados que leva à solução do problema.
        """
        self.fronteira = []  # Fronteira de busca
        self.visitados = []  # Estados já visitados
        self.solucao = []    # Sequência de estados da solução

    def busca(self, problema):
        """
        Realiza a busca em largura para encontrar a solução do problema.

        Args:
            problema: O problema a ser resolvido, contendo métodos como estadoInicial(),
                      testeObjetivo() e funcaoSucessora().
        """
        # Adiciona o estado inicial na fronteira
        self.fronteira.append((problema.estadoInicial(), []))
        
        while len(self.fronteira) > 0:
            # Remove o primeiro estado da fronteira
            estado, caminho = self.fronteira.pop(0)
            
            # Verifica se o estado é o objetivo
            if problema.testeObjetivo(estado):
                # Se for, adiciona o caminho até o estado na solução
                self.solucao = caminho + [estado]
                break
            
            # Adiciona o estado na lista de visitados
            self.visitados.append(estado)
            
            # Gera os filhos do estado
            filhos = problema.funcaoSucessora(estado)
            
            # Adiciona os filhos na fronteira
            for filho in filhos:
                if not filho in self.visitados:
                    self.fronteira.append((filho, caminho + [estado]))
    
    def mostraCaminho(self):
        """
        Mostra o caminho da solução encontrada.
        """
        # Mostra o caminho
        for estado in self.solucao:
            print("Missionarios: " + str(estado[0]) + " Canibais: " + str(estado[1]) + " Lado: " + str(estado[2]))
