import BuscaEmLargura
import Jarros

def main():
    """
    Função principal que resolve o problema dos jarros utilizando busca em largura.
    """
    # Inicializa o problema dos Jarros com um jarro de capacidade 4 e outro de capacidade 3.
    problema = Jarros.Jarros(4, 3)
    
    # Inicializa a busca em largura
    busca = BuscaEmLargura.BuscaEmLargura()
    
    # Realiza a busca em largura para encontrar a solução do problema
    busca.busca(problema)
    
    # Mostra o caminho da solução encontrada
    busca.mostraCaminho()
    
if __name__ == '__main__':
    main()
