class Node:
    def __init__(self, palitos_restantes, is_max_turn):
        self.palitos_restantes = palitos_restantes
        self.is_max_turn = is_max_turn
        self.value = 0
        self.children = []

        if palitos_restantes > 0:
            for i in range(1, min(4, palitos_restantes + 1)):
                self.children.append(Node(palitos_restantes - i, not is_max_turn))

def minimax(node, depth, alpha, beta, usar_poda, direction):
    if depth == 0 or len(node.children) == 0:
        return 1 if node.is_max_turn else -1

    children = node.children if direction == 'left' else reversed(node.children)

    if node.is_max_turn:
        max_eval = float('-inf')
        for child in children:
            eval = minimax(child, depth - 1, alpha, beta, usar_poda, direction)
            max_eval = max(max_eval, eval)
            if usar_poda:
                alpha = max(alpha, eval)
                if beta <= alpha:
                    print("Poda alfa-beta na profundidade", depth)
                    break
        node.value = max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for child in children:
            eval = minimax(child, depth - 1, alpha, beta, usar_poda, direction)
            min_eval = min(min_eval, eval)
            if usar_poda:
                beta = min(beta, eval)
                if beta <= alpha:
                    print("Poda alfa-beta na profundidade", depth)
                    break
        node.value = min_eval
        return min_eval
    
def print_arvore(Nodo, profundidade=0):
    if Nodo:
        print("      " * profundidade, "Palitos restantes:", Nodo.palitos_restantes, "Valor:", Nodo.value)
        for filho in Nodo.children:
            print_arvore(filho, profundidade + 2)

root = Node(5, True)
minimax(root, 5, float('-inf'), float('inf'), False, 'left')

print("O valor do jogo é:", root.value)
print_arvore(root)

root = Node(5, True)
minimax(root, 5, float('-inf'), float('inf'), True, 'left')

print("O valor do jogo com a poda executada a partir da esquerda é:", root.value)
print_arvore(root)

root = Node(5, True)
minimax(root, 5, float('-inf'), float('inf'), True, 'right')

print("O valor do jogo com a poda executada a partir da direita é:", root.value)
print_arvore(root)