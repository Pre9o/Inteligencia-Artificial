class Nodo:
    def __init__(self, palitos_restantes, maximizando_jogador):
        self.palitos_restantes = palitos_restantes
        self.maximizando_jogador = maximizando_jogador
        self.valor = 0
        self.filhos = []

        if palitos_restantes > 0:
            for i in range(1, min(4, palitos_restantes + 1)):
                self.filhos.append(Nodo(palitos_restantes - i, not maximizando_jogador))

def minimax(Nodo, profundidade, alpha, beta, usar_poda, direcao):
    if profundidade == 0 or len(Nodo.filhos) == 0:
        return 1 if Nodo.maximizando_jogador else -1

    filhos = Nodo.filhos if direcao == 'left' else reversed(Nodo.filhos)

    if Nodo.maximizando_jogador:
        max_eval = float('-inf')
        for filho in filhos:
            eval = minimax(filho, profundidade - 1, alpha, beta, usar_poda, direcao)
            max_eval = max(max_eval, eval)
            if usar_poda:
                alpha = max(alpha, eval)
                if beta <= alpha:
                    print("Poda alfa-beta na profundidade", profundidade)
                    break
        Nodo.valor = max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for filho in filhos:
            eval = minimax(filho, profundidade - 1, alpha, beta, usar_poda, direcao)
            min_eval = min(min_eval, eval)
            if usar_poda:
                beta = min(beta, eval)
                if beta <= alpha:
                    print("Poda alfa-beta na profundidade", profundidade)
                    break
        Nodo.valor = min_eval
        return min_eval
    
def print_arvore(Nodo, profundidade=0):
    if Nodo:
        print("      " * profundidade, "Palitos restantes:", Nodo.palitos_restantes, "Valor:", Nodo.valor)
        for filho in Nodo.filhos:
            print_arvore(filho, profundidade + 2)

raiz = Nodo(5, True)
minimax(raiz, 5, float('-inf'), float('inf'), False, 'left')

print("O valor do jogo é:", raiz.valor)
print_arvore(raiz)

raiz = Nodo(5, True)
minimax(raiz, 5, float('-inf'), float('inf'), True, 'left')

print("O valor do jogo com a poda executada a partir da esquerda é:", raiz.valor)
print_arvore(raiz)

raiz = Nodo(5, True)
minimax(raiz, 5, float('-inf'), float('inf'), True, 'right')

print("O valor do jogo com a poda executada a partir da direita é:", raiz.valor)
print_arvore(raiz)