import aStar, Rotas

def main():
    problema = Rotas.Rotas('a', 'k')

    astar = aStar.aStar()

    astar.buscar(problema)
    
    astar.mostra_caminho()

if __name__ == '__main__':
    main()