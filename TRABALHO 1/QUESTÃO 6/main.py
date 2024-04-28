import BuscaGulosa, Rotas

def main():
    problema = Rotas.Rotas('a', 'k')

    busca_gulosa = BuscaGulosa.BuscaGulosa()

    busca_gulosa.buscar(problema)
    
    busca_gulosa.mostra_caminho()

if __name__ == '__main__':
    main()