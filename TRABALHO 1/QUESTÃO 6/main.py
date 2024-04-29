import BuscaGulosa, Rotas

def main():
    """
    Função principal para resolver o problema de busca de rotas utilizando o algoritmo de Busca Gulosa.

    Cria uma instância do problema de rotas com origem 'a' e destino 'k'.
    Inicializa a busca gulosa e realiza a busca para encontrar a solução.
    Exibe o caminho da solução e informações sobre a busca.

    """
    problema = Rotas.Rotas('a', 'k')

    busca_gulosa = BuscaGulosa.BuscaGulosa()

    busca_gulosa.buscar(problema)
    
    busca_gulosa.mostra_caminho()

if __name__ == '__main__':
    main()
