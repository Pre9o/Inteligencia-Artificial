import BuscaEmLargura, MissionariosCanibais

def main():
    # Inicializa o problema
    problema = MissionariosCanibais.MissionariosCanibais(3, 3, 1, 2)
    # Inicializa a busca em largura
    busca = BuscaEmLargura.BuscaEmLargura()
    
    # Realiza a busca
    busca.busca(problema)
    
    # Mostra o caminho
    busca.mostraCaminho()
    
if __name__ == '__main__':
    main()