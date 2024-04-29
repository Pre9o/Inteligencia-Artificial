class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

def minimax(Nodo, profundidade, maximizando_jogador):
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

# Construindo a árvore
root = Nodo(0)

root.filhos = [
    Nodo(0),
    Nodo(0)
]

contador = 0

for i, filho in enumerate(root.filhos):
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

# Aplicando o algoritmo Minimax alternando os jogadores
def alternar_minimax(Nodo, profundidade):
    if profundidade % 2 == 0:
        minimax(Nodo, profundidade, False)  # Maximizando
    else:
        minimax(Nodo, profundidade, True)   # Minimizando

# Aplicando o algoritmo Minimax alternando os jogadores
alternar_minimax(root, 5)

# Função para imprimir a árvore
def print_arvore(Nodo, profundidade=0):
    if Nodo:
        print(" " * profundidade, Nodo.valor)
        for filho in Nodo.filhos:
            print_arvore(filho, profundidade + 2)

# Imprimindo a árvore preenchida
print("Árvore preenchida:")
print_arvore(root)
