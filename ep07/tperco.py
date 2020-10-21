from percolation import Percolation

teste = Percolation(4)
teste.data[3,3] = 2
teste.open(0,0)
teste.open(2,3)
teste.open(3,3)
teste.open(3,2)
print(teste.no_open())
print(teste.get_grid())