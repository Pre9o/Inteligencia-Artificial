import networkx as nx
import matplotlib.pyplot as plt

class BuscaEmLargura:
    def __init__(self):
        self.fronteira = []
        self.visitados = []
        self.solucao = []

    def busca(self, problema):
        # Adiciona o estado inicial na fronteira
        estado_inicial = problema.estadoInicial()
        self.fronteira.append((estado_inicial, []))  # Adiciona o estado inicial e uma lista vazia como caminho
        
        while len(self.fronteira) > 0:
            # Remove o primeiro estado da fronteira
            
            estado, caminho = self.fronteira.pop(0)

            # Verifica se o estado é o objetivo
            if problema.testeObjetivo(estado):
                # Se for, adiciona o caminho até o estado na solução
                self.solucao = caminho + [(None, estado)]  # Adiciona o estado objetivo à solução
                break

            # Adiciona o estado na lista de visitados
            self.visitados.append(estado)

            # Gera os filhos do estado
            filhos = problema.funcaoSucessora(estado)

            for nome, filho in filhos:
                # Adiciona o filho na fronteira
                if filho not in self.visitados:
                    self.fronteira.append((filho, caminho + [(nome, filho)]))


    def mostraGrafo(self):
        # Cria um novo grafo para a solução
        grafo_solucao = nx.DiGraph()

        # Adiciona os estados e as transições da solução ao grafo
        for i in range(len(self.solucao) - 1):
            estado_atual = self.solucao[i][1]
            estado_proximo = self.solucao[i + 1][1]
            grafo_solucao.add_edge(tuple(estado_atual), tuple(estado_proximo))

        # Desenha o grafo da solução
        nx.draw(grafo_solucao, with_labels=True, ax=plt.gca(), node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
        plt.savefig("grafo_solucao.png")
        plt.show()
        

    def mostraCaminho(self):
        # Mostra o caminho
        for nome, estado in self.solucao:
            print("Operação: " + str(nome) + " Estado: " + str(estado))
            
        print(f"Lista de nodos abertos: {self.visitados}\n")
        print(f"Lista de nodos fechados: {self.fronteira}\n")
            
        self.mostraGrafo()

