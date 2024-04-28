import BuscaEmLargura, Fazendeiro

def main():
    # Inicializa o problema
    problema = Fazendeiro.Fazendeiro(['e', 'e', 'e', 'e'])
    # Inicializa a busca em largura
    busca = BuscaEmLargura.BuscaEmLargura()
    
    # Realiza a busca
    busca.busca(problema)
    
    # Mostra o caminho
    busca.mostraCaminho()
    
if __name__ == '__main__':
    main()