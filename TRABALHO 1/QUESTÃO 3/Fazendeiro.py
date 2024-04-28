class Fazendeiro:
    def __init__(self, estado):
        # Estado é uma lista da forma ['e', 'e', 'e', 'e'], onde cada elemento representa a posição do fazendeiro, lobo, ovelha e repolho, respectivamente
        self.estado = estado
        self.tamanho_barco = 1
        self.objetivo = ['d', 'd', 'd', 'd']
        self.lado = 'e'

    def estadoInicial(self):
        return ('Início', 'e', 'e', 'e', 'e')

    def testeObjetivo(self, estado):
        # O objetivo é ter todos na margem direita
        return estado == self.objetivo

    def funcaoSucessora(self, estado):
        sucessores = []
        
        if estado[0] == 'e':
            # Se o fazendeiro está na margem esquerda
            for i in range(self.tamanho_barco + 1):
                for j in range(self.tamanho_barco + 1):
                    for k in range(self.tamanho_barco + 1):
                        for l in range(self.tamanho_barco + 1):
                            if i + j + k + l <= self.tamanho_barco and i + j + k + l > 0:
                                # Gera os sucessores
                                sucessor = [estado[0], estado[1], estado[2], estado[3]]
                                sucessor[0] = 'd'
                                if i > 0:
                                    sucessor[1] = 'd'
                                if j > 0:
                                    sucessor[2] = 'd'
                                if k > 0:
                                    sucessor[3] = 'd'
                                if self.validaEstado(sucessor):
                                    nome = 'Levar ' + str(i) + ' lobo(s), ' + str(j) + ' ovelha(s) e ' + str(k) + ' repolho(s) para a margem direita.'
                                    sucessores.append((nome, sucessor))
        else:
            # Se o fazendeiro está na margem direita
            for i in range(self.tamanho_barco + 1):
                for j in range(self.tamanho_barco + 1):
                    for k in range(self.tamanho_barco + 1):
                        for l in range(self.tamanho_barco + 1):
                            if i + j + k + l <= self.tamanho_barco and i + j + k + l > 0:
                                # Gera os sucessores
                                sucessor = [estado[0], estado[1], estado[2], estado[3]]
                                sucessor[0] = 'e'
                                if i > 0:
                                    sucessor[1] = 'e'
                                if j > 0:
                                    sucessor[2] = 'e'
                                if k > 0:
                                    sucessor[3] = 'e'
                                if self.validaEstado(sucessor):
                                    nome = 'Levar ' + str(i) + ' lobo(s), ' + str(j) + ' ovelha(s) e ' + str(k) + ' repolho(s) para a margem esquerda.'
                                    sucessores.append((nome, sucessor))
        return sucessores

    def validaEstado(self, estado):
        # O lobo não pode ficar sozinho com a ovelha, e a ovelha não pode ficar sozinha com o repolho
        if (estado[1] == estado[2] and estado[0] != estado[1]) or (estado[2] == estado[3] and estado[0] != estado[2]):
            return False
        
        
        return True