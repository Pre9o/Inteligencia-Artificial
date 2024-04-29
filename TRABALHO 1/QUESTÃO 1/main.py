import BuscaEmLargura
import MissionariosCanibais

def main():
    """
    Função principal que executa a busca em largura para o problema dos Missionários e Canibais.
    """
    # Inicializa o problema dos Missionários e Canibais com 3 missionários, 3 canibais, 1 barco e tamanho do barco 2
    problema = MissionariosCanibais.MissionariosCanibais(3, 3, 1, 2)
    
    # Inicializa a busca em largura
    busca = BuscaEmLargura.BuscaEmLargura()
    
    # Realiza a busca em largura para encontrar a solução do problema
    busca.busca(problema)
    
    # Mostra o caminho da solução encontrada
    busca.mostraCaminho()
    
if __name__ == '__main__':
    main()
