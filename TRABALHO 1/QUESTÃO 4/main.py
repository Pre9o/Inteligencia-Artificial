import BuscaEmLargura, BuscaEmProfundidade, Voos

def main():
    # Inicializa o problema
    problema = Voos.Voos('a', 'j')
    # Inicializa a busca em largura
    busca = BuscaEmLargura.BuscaEmLargura()
    
    # Realiza a busca
    busca.busca(problema)
    
    # Mostra o caminho
    busca.mostraCaminho()
    
    # Inicializa a busca em profundidade
    busca = BuscaEmProfundidade.BuscaEmProfundidade()
    
    # Realiza a busca
    busca.busca(problema)
    
    # Mostra o caminho
    busca.mostraCaminho()
    
if __name__ == '__main__':
    main()