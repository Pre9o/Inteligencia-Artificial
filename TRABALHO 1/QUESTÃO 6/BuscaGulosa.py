import networkx as nx
import matplotlib.pyplot as plt

class BuscaGulosa:
    def __init__(self):
        """
        Inicializa a classe BuscaGulosa.

        Atributos:
            solucao (list): O caminho da solução encontrado pela busca.
            fronteira (list): A fronteira de estados a serem explorados.
            visitados (list): Lista de estados já visitados durante a busca.
        """
        self.solucao = None
        self.fronteira = []
        self.visitados = []

    def buscar(self, problema):
        """
        Realiza a busca gulosa para encontrar a solução do problema.

        Args:
            problema: O problema a ser resolvido.

        Atribuições:
            Adiciona o estado inicial na fronteira.
            Enquanto a fronteira não estiver vazia:
                - Remove o estado da fronteira.
                - Verifica se o estado é o objetivo.
                - Adiciona o estado na lista de visitados.
                - Gera os filhos do estado.
                - Adiciona os filhos na fronteira.
                - Ordena a fronteira de acordo com a heurística.
        """
        estado_inicial = problema.estadoInicial()
        self.fronteira.append((estado_inicial, [(None, estado_inicial)]))
        
        while len(self.fronteira) > 0:
            estado, caminho = self.fronteira.pop(0)
            
            if problema.testeObjetivo(estado):
                self.solucao = caminho + [(None, estado)]
                break
            
            self.visitados.append(estado)
            filhos = problema.funcaoSucessora(estado)
            
            for nome, filho in filhos:
                if filho not in self.visitados:
                    self.fronteira.append((filho, caminho + [(nome, filho)]))
                    
            self.fronteira.sort(key=lambda x: problema.heuristica(x[0]))
            
    def mostraGrafo(self):
        """
        Desenha o grafo da solução.

        Cria um novo grafo para a solução e desenha as transições entre os estados.
        """
        grafo_solucao = nx.DiGraph()
        
        for i in range(len(self.solucao) - 1):
            estado_atual = self.solucao[i][1]
            estado_proximo = self.solucao[i + 1][1]
            grafo_solucao.add_edge(tuple(estado_atual), tuple(estado_proximo))
            
        nx.draw(grafo_solucao, with_labels=True, ax=plt.gca(), node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
        plt.savefig("grafo_solucao_gulosa.png")
        plt.show()
        
    def mostra_caminho(self):
        """
        Mostra o caminho da solução e informações sobre a busca.

        Exibe o caminho da solução, a lista de nodos abertos e fechados durante a busca, e desenha o grafo da solução.
        """
        for nome, estado in self.solucao:
            print("Operação: " + str(nome) + " Estado: " + str(estado))
            
        print(f"Lista de nodos abertos: {self.visitados}\n")
        print(f"Lista de nodos fechados: {self.fronteira}\n")
        
        self.mostraGrafo()
