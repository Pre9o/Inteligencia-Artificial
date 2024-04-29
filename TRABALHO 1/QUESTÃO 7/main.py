import aStar, Rotas

def main():
    """
    Função principal do programa. Executa o algoritmo A* para encontrar o menor caminho entre dois pontos de uma matriz de adjacência.
    
    Cria uma instância do problema de rotas com origem 'a' e destino 'k'.
    Inicializa a busca A* e realiza a busca para encontrar a solução.
    Exibe o caminho da solução e informações sobre a busca.

    """

    problema = Rotas.Rotas('a', 'k')

    astar = aStar.aStar()

    astar.buscar(problema)
    
    astar.mostra_caminho()

if __name__ == '__main__':
    main()