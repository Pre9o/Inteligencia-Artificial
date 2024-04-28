import BuscaGulosa, QuebraCabeca

def main():
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