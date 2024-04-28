import MinMax, ArvoreDeBusca

def main():
    arvore = ArvoreDeBusca.ArvoreDeBusca([20, 33, -45, 31, 24, 25,-10, 20, 40, -25, 18, -42, 24, -19, 36, -41])

    minmax = MinMax.MinMax(arvore.retornaFolhas())

    minmax.mostraSolucao()

if __name__ == "__main__":
    main()
   