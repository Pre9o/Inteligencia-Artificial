import BuscaEmLargura, BuscaEmProfundidade, Voos

def main():
    """
    Função principal que executa a busca em largura e a busca em profundidade para o problema dos voos.
    """
    
    # Inicializa o problema dos voos com origem em 'a' e destino em 'j'
    problema = Voos.Voos('a', 'j')
    
    # Inicializa a busca em largura
    busca_largura = BuscaEmLargura.BuscaEmLargura()
    
    # Realiza a busca em largura
    busca_largura.busca(problema)
    
    # Mostra o caminho encontrado pela busca em largura
    busca_largura.mostraCaminho()
    
    # Inicializa a busca em profundidade
    busca_profundidade = BuscaEmProfundidade.BuscaEmProfundidade()
    
    # Realiza a busca em profundidade
    busca_profundidade.busca(problema)
    
    # Mostra o caminho encontrado pela busca em profundidade
    busca_profundidade.mostraCaminho()
    
if __name__ == '__main__':
    main()
