import BuscaGulosa, QuebraCabeca

def main():
    """ 
    Função principal do programa. Executa o algoritmo de busca gulosa para resolver o problema do quebra-cabeça de 8 peças.
    
    Cria uma instância do problema do quebra-cabeça com o estado inicial e o estado objetivo.
    Inicializa a busca gulosa e realiza a busca para encontrar a solução.
    Exibe o caminho da solução e informações sobre a busca.
    
    """
    problema = QuebraCabeca.QuebraCabeca([1, 3, 4,
                                          8, 2, 5,
                                          7, 6, 0],
                                         [1, 2, 3,
                                          8, 0, 4,
                                          7, 6, 5], 1)

    busca_gulosa = BuscaGulosa.BuscaGulosa()

    busca_gulosa.buscar(problema)
    
    busca_gulosa.mostra_caminho(problema)


    problema = QuebraCabeca.QuebraCabeca([1, 3, 4,
                                          8, 2, 5,
                                          7, 6, 0],
                                         [1, 2, 3,
                                          8, 0, 4,
                                          7, 6, 5], 2)
    
    busca_gulosa = BuscaGulosa.BuscaGulosa()

    busca_gulosa.buscar(problema)

    busca_gulosa.mostra_caminho(problema)

if __name__ == '__main__':
    main()