import BuscaEmLargura, BuscaEmProfundidade, BuscaGulosa, Voos

def main():
    """
    Função principal que executa as diferentes buscas no problema de voos.

    Realiza as buscas em profundidade, largura e gulosa para encontrar o caminho entre uma origem e um destino.
    """
    # Cria um problema de voos com origem 'a' e destino 'h'
    voos = Voos.Voos('a', 'h')
    
    # Realiza a busca em profundidade
    busca_profundidade = BuscaEmProfundidade.BuscaEmProfundidade()
    busca_profundidade.busca(voos)
    busca_profundidade.mostraCaminho()
    
    # Realiza a busca em largura
    busca_largura = BuscaEmLargura.BuscaEmLargura()
    busca_largura.busca(voos)
    busca_largura.mostraCaminho()
    
    # Realiza a busca gulosa
    busca_gulosa = BuscaGulosa.BuscaGulosa()
    busca_gulosa.buscar(voos)
    busca_gulosa.mostra_caminho()

if __name__ == "__main__":
    main()
