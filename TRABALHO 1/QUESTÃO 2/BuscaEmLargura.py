import networkx as nx
import matplotlib.pyplot as plt

class BuscaEmLargura:
    def __init__(self):
        self.fronteira = []
        self.visitados = []
        self.solucao = []
        self.grafo = nx.DiGraph()  # Adiciona um grafo para representar a árvore de busca

    def busca(self, problema):
        # Adiciona o estado inicial na fronteira
        estado_inicial = problema.estadoInicial()
        self.fronteira.append((estado_inicial, []))
        self.grafo.add_node(estado_inicial)  # Adiciona o estado inicial ao grafo

        while len(self.fronteira) > 0:
            # Remove o primeiro estado da fronteira
            estado, caminho = self.fronteira.pop(0)

            # Verifica se o estado é o objetivo
            if problema.testeObjetivo(estado):
                # Se for, adiciona o caminho até o estado na solução
                self.solucao = caminho + [(estado)]
                break

            # Adiciona o estado na lista de visitados
            self.visitados.append(estado)

            # Gera os filhos do estado
            filhos = problema.funcaoSucessora(estado)

            # Adiciona os filhos na fronteira
            for nome, estado_filho in filhos:
                if not estado_filho in self.visitados:
                    self.fronteira.append(((nome, estado_filho), caminho + [estado]))
                    self.grafo.add_edge(estado, estado_filho)  # Adiciona uma aresta ao grafo
                    
    def mostraGrafo(self):
        # Cria um novo grafo para a solução
        grafo_solucao = nx.DiGraph()

        # Adiciona os estados e as transições da solução ao grafo
        for i in range(len(self.solucao) - 1):
            estado_atual = self.solucao[i][1]
            estado_proximo = self.solucao[i + 1][1]
            grafo_solucao.add_edge(estado_atual, estado_proximo)

        # Desenha o grafo da solução
        nx.draw(grafo_solucao, with_labels=True, ax=plt.gca(), node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
        plt.savefig("grafo_solucao.png")
        plt.show()
        

    def mostraCaminho(self):
        # Mostra o caminho
        for nome, estado in self.solucao:
            print("Operação: " + nome + " Jarro 1: " + str(estado[0]) + " Jarro 2: " + str(estado[1]))
            
        self.mostraGrafo()

