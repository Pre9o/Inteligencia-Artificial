class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def minimax(node, depth, maximizing_player):
    if depth == 0 or len(node.children) == 0:
        return node.value
    
    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        node.value = max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        node.value = min_eval
        return min_eval

# Construindo a árvore
root = Node(0)

root.children = [
    Node(0),
    Node(0)
]

for i, child in enumerate(root.children):
    child.children = [
        Node(0),
        Node(0)
    ]

    for j, grandchild in enumerate(child.children):
        grandchild.children = [
            Node(0),
            Node(0)
        ]

    for j, grandgrandchild in enumerate(grandchild.children):
        grandchild.value = [20, 33, -45, 31, 24, 25, -10, 20, 40, -25, 18, -42, 24, -19, 36, -41][i * 2 + j]

# Aplicando o algoritmo Minimax alternando os jogadores
def alternate_minimax(node, depth):
    if depth % 2 == 0:
        minimax(node, depth, False)  # Maximizando
    else:
        minimax(node, depth, True)   # Minimizando

# Aplicando o algoritmo Minimax alternando os jogadores
alternate_minimax(root, 5)

# Função para imprimir a árvore
def print_tree(node, depth=0):
    if node:
        print(" " * depth, node.value)
        for child in node.children:
            print_tree(child, depth + 2)

# Imprimindo a árvore preenchida
print("Árvore preenchida:")
print_tree(root)
