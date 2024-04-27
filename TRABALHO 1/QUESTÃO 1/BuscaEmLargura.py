class BuscaEmLargura:
    def __init__(self):
        self.fronteira = []
        self.visitados = []
        self.solucao = []
    
    def busca(self, problema):
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
        # Mostra o caminho
        for estado in self.solucao:
            # print(estado)
            print("Missionarios: " + str(estado[0]) + " Canibais: " + str(estado[1]) + " Lado: " + str(estado[2]))