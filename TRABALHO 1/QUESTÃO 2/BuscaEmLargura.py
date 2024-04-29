import networkx as nx
import matplotlib.pyplot as plt

class BuscaEmLargura:
    """
    Implementação de um algoritmo de busca em largura com visualização do grafo de solução.
    """

    def __init__(self):
        """
        Inicializa a classe de busca em largura.

        Fronteira é a lista de estados a serem explorados.
        Visitados é a lista de estados já visitados.
        Solução é a sequência de estados que leva à solução do problema.
        """
        self.fronteira = []    # Fronteira de busca
        self.visitados = []    # Estados já visitados
        self.solucao = []      # Sequência de estados da solução

    def busca(self, problema):
        """
        Realiza a busca em largura para encontrar a solução do problema.

        Args:
            problema: O problema a ser resolvido, contendo métodos como estadoInicial(),
                      testeObjetivo() e funcaoSucessora().
        """
        # Adiciona o estado inicial na fronteira
        estado_inicial = problema.estadoInicial()
        self.fronteira.append((estado_inicial, []))

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

    def mostraGrafo(self):
        """
        Mostra visualmente o grafo de solução utilizando a biblioteca NetworkX e Matplotlib.
        """
        # Cria um novo grafo para a solução
        grafo_solucao = nx.DiGraph()

        # Adiciona os estados e as transições da solução ao grafo
        for i in range(len(self.solucao) - 1):
            estado_atual = self.solucao[i][1]
            estado_proximo = self.solucao[i + 1][1]
            grafo_solucao.add_edge(estado_atual, estado_proximo)

        # Desenha o grafo da solução
        nx.draw(grafo_solucao, with_labels=True, ax=plt.gca(), node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
        plt.savefig("grafo_solucao.png")  # Salva o grafo como uma imagem
        plt.show()  # Exibe o grafo

    def mostraCaminho(self):
        """
        Mostra o caminho da solução encontrada, exibindo as operações realizadas em cada estado.
        """
        # Mostra o caminho
        for nome, estado in self.solucao:
            print("Operação: " + nome + " Jarro 1: " + str(estado[0]) + " Jarro 2: " + str(estado[1]))
            
        # Mostra a lista de nodos abertos e fechados durante a busca
        print(f"Lista de nodos abertos: {self.visitados}\n")
        print(f"Lista de nodos fechados: {self.fronteira}\n")
            
        self.mostraGrafo()  # Chama a função para exibir o grafo de solução
