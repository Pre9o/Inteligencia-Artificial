import networkx as nx
import matplotlib.pyplot as plt

class aStar:
    def __init__(self):
        """
        Inicializa a busca A*.

        Atributos:
            solucao (list): Representa o caminho da solução.
            fronteira (list): Representa os estados na fronteira de busca.
            visitados (list): Representa os estados já visitados durante a busca.
        """
        self.solucao = None
        self.fronteira = []
        self.visitados = []

    def buscar(self, problema):
        """
        Realiza a busca A* para encontrar a solução do problema.

        :param problema: O problema a ser resolvido.
        :type problema: Problema
        """
        # Adiciona o estado inicial na fronteira
        estado_inicial = problema.estadoInicial()
        self.fronteira.append((estado_inicial, [(None, estado_inicial)], 0))
        
        while len(self.fronteira) > 0:
            # Remove o estado da fronteira
            estado, caminho, custo = self.fronteira.pop(0)
            
            # Verifica se o estado é o objetivo
            if problema.testeObjetivo(estado):
                # Se for, adiciona o caminho até o estado na solução
                self.solucao = caminho + [(None, estado)]
                break
            
            # Adiciona o estado na lista de visitados
            self.visitados.append(estado)
            
            # Gera os filhos do estado
            filhos = problema.funcaoSucessora(estado)
            
            # Adiciona os filhos na fronteira
            for nome, filho in filhos:
                if filho not in self.visitados:
                    self.fronteira.append((filho, caminho + [(nome, filho)], custo + problema.custo(estado, filho)))
                    
            # Ordena a fronteira de acordo com a heurística
            self.fronteira.sort(key=lambda x: problema.heuristica(x[0]) + x[2])

    def mostraGrafo(self):
        """
        Desenha e exibe o grafo da solução.
        """
        # Cria um novo grafo para a solução
        grafo_solucao = nx.DiGraph()
        
        # Adiciona os estados e as transições da solução ao grafo
        for i in range(len(self.solucao) - 1):
            estado_atual = self.solucao[i][1]
            estado_proximo = self.solucao[i + 1][1]
            grafo_solucao.add_edge(tuple(estado_atual), tuple(estado_proximo))
            
        # Desenha o grafo da solução
        nx.draw(grafo_solucao, with_labels=True, ax=plt.gca(), node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
        plt.savefig("grafo_solucao_astar.png")
        plt.show()

    def mostra_caminho(self):
        """
        Exibe o caminho da solução e outras informações relevantes.
        """
        # Mostra o caminho
        for nome, estado in self.solucao:
            print("Operação: " + str(nome) + " Estado: " + str(estado))
            
        print(f"Lista de nodos abertos: {self.visitados}\n")
        print(f"Lista de nodos fechados: {self.fronteira}\n")

        self.mostraGrafo()
