from percolation import Percolation

teste = Percolation((3,4))
teste.open(0,0)
teste.open(2,2)
teste.open(1,1)
teste.open(1,2)
teste.open(0,1)
teste.open(2,3)
teste.open(1,1)
print(teste.graph.id)
print(teste.get_grid())

