import BuscaEmLargura
import Fazendeiro

def main():
    """
    Função principal que resolve o problema do Fazendeiro, Lobo, Ovelha e Repolho utilizando busca em largura.
    """
    # Inicializa o problema do Fazendeiro com o estado inicial ['e', 'e', 'e', 'e']
    problema = Fazendeiro.Fazendeiro(['e', 'e', 'e', 'e'])
    
    # Inicializa a busca em largura
    busca = BuscaEmLargura.BuscaEmLargura()
    
    # Realiza a busca em largura para encontrar a solução do problema
    busca.busca(problema)
    
    # Mostra o caminho da solução encontrada
    busca.mostraCaminho()
    
if __name__ == '__main__':
    main()
