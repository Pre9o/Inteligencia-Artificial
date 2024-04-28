import BuscaEmLargura, BuscaEmProfundidade, BuscaGulosa, Voos

def main():
    voos = Voos.Voos('a', 'h')
    
    busca_profundidade = BuscaEmProfundidade.BuscaEmProfundidade()
    busca_profundidade.busca(voos)
    busca_profundidade.mostraCaminho()
    
    busca_largura = BuscaEmLargura.BuscaEmLargura()
    busca_largura.busca(voos)
    busca_largura.mostraCaminho()
    
    busca_gulosa = BuscaGulosa.BuscaGulosa()
    busca_gulosa.buscar(voos)
    busca_gulosa.mostra_caminho()
    
if __name__ == "__main__":
    main()