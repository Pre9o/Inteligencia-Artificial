class Nodo:
    """
    Classe que representa um nó em uma árvore.

    Atributos:
    - valor: O valor armazenado no nó.
    - filhos: Uma lista de nós filhos.
    """

    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

def minimax(Nodo, profundidade, maximizando_jogador):
    """
    Implementa o algoritmo Minimax para encontrar a melhor jogada em um jogo de dois jogadores.

    Parâmetros:
    - Nodo: O nó atual do jogo.
    - profundidade: A profundidade atual da busca.
    - maximizando_jogador: Um valor booleano indicando se é a vez do jogador maximizador.

    Retorna:
    - O valor da jogada ótima para o jogador atual.

    """
    if profundidade == 0 or len(Nodo.filhos) == 0:
        return Nodo.valor
    
    if maximizando_jogador:
        max_eval = float('-inf')
        for filho in Nodo.filhos:
            eval = minimax(filho, profundidade - 1, False)
            max_eval = max(max_eval, eval)
        Nodo.valor = max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for filho in Nodo.filhos:
            eval = minimax(filho, profundidade - 1, True)
            min_eval = min(min_eval, eval)
        Nodo.valor = min_eval
        return min_eval
    
def poda_alpha_beta(Nodo, profundidade, alpha, beta, maximizando_jogador, lado):
    """
    Realiza a poda alfa-beta em uma árvore de jogo.

    Args:
        Nodo (objeto): O nó atual da árvore.
        profundidade (int): A profundidade atual na árvore.
        alpha (float): O valor do alpha.
        beta (float): O valor do beta.
        maximizando_jogador (bool): Indica se é o turno do jogador maximizador.
        lado (str): O lado da árvore a ser percorrido ('esquerda' ou 'direita').

    Returns:
        float: O valor do nó após a poda alfa-beta.
    """
    if profundidade == 0 or len(Nodo.filhos) == 0:
        return Nodo.valor
    
    filhos = Nodo.filhos if lado == 'esquerda' else Nodo.filhos[::-1]
    
    if maximizando_jogador:
        max_eval = float('-inf')
        for filho in filhos:
            eval = poda_alpha_beta(filho, profundidade - 1, alpha, beta, False, lado)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                print("Poda alfa-beta na profundidade", profundidade)
                break
        Nodo.valor = max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for filho in filhos:
            eval = poda_alpha_beta(filho, profundidade - 1, alpha, beta, True, lado)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                print("Poda alfa-beta na profundidade", profundidade)
                break
        Nodo.valor = min_eval
        return min_eval
    
def arvore_preenchida():
    """
    Constrói e retorna uma árvore preenchida com valores específicos.

    A árvore é construída com base em um padrão de filhos e netos, onde cada nó
    contém um valor específico. Os valores são definidos a partir de uma lista
    predefinida.

    Returns:
        Nodo: A raiz da árvore preenchida.
    """
    # Construindo a árvore
    raiz = Nodo(0)

    raiz.filhos = [
        Nodo(0),
        Nodo(0)
    ]

    contador = 0

    for i, filho in enumerate(raiz.filhos):
        filho.filhos = [
            Nodo(0),
            Nodo(0)
        ]

        for j, neto in enumerate(filho.filhos):
            neto.filhos = [
                Nodo(0),
                Nodo(0)
            ]

            for k, bisneto in enumerate(neto.filhos):
                bisneto.filhos = [
                    Nodo(0),
                    Nodo(0)
                ]

                for l, tataraneto in enumerate(bisneto.filhos):
                    tataraneto.valor = [20, 33, -45, 31, 24, 25, -10, 20, 40, -25, 18, -42, 24, -19, 36, -41][contador]
                    contador += 1

    return raiz

# Aplicando o algoritmo Minimax alternando os jogadores
def alternar_minimax(Nodo, profundidade):
    """
    Alterna entre maximização e minimização do algoritmo minimax.

    Parâmetros:
    - Nodo: O nó atual do jogo.
    - profundidade: A profundidade atual na árvore de busca.

    Retorna:
    Nenhum valor de retorno.
    """
    if profundidade % 2 == 0:
        minimax(Nodo, profundidade, False)  # Maximizando
    else:
        minimax(Nodo, profundidade, True)   # Minimizando

# Função para imprimir a árvore
def print_arvore(Nodo, profundidade=0):
    """
    Imprime a árvore representada pelo nó fornecido.

    Args:
        Nodo: O nó raiz da árvore.
        profundidade (opcional): A profundidade atual na árvore (padrão é 0).

    Returns:
        None
    """
    if Nodo:
        print(" " * profundidade, Nodo.valor)
        for filho in Nodo.filhos:
            print_arvore(filho, profundidade + 2)

raiz = arvore_preenchida()

# Aplicando o algoritmo Minimax alternando os jogadores
alternar_minimax(raiz, 5)

# Imprimindo a árvore preenchida
print("Árvore preenchida MiniMax:")
print_arvore(raiz)

raiz = arvore_preenchida()

poda_alpha_beta(raiz, 5, float('-inf'), float('inf'), True, 'esquerda')

# Imprimindo a árvore preenchida
print("Árvore preenchida Poda AlphaBeta esquerda:")
print_arvore(raiz)

raiz = arvore_preenchida()

poda_alpha_beta(raiz, 5, float('-inf'), float('inf'), True, 'direita')

# Imprimindo a árvore preenchida
print("Árvore preenchida Poda AlphaBeta direita:")
print_arvore(raiz)