import BuscaEmLargura, Jarros

def main():
    # Inicializa o problema
    problema = Jarros.Jarros(4, 3)
    # Inicializa a busca em largura
    busca = BuscaEmLargura.BuscaEmLargura()
    
    # Realiza a busca
    busca.busca(problema)
    
    # Mostra o caminho
    busca.mostraCaminho()
    
if __name__ == '__main__':
    main()