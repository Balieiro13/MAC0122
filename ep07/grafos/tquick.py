from quickfind import QuickFind

obj=QuickFind(5) #Total number of nodes in graph
obj.union(0,1) #Create connection between 0 and 1
obj.union(2,3) #Create connection between 2 and 3
obj.union(3,4) #Create connection between 3 and 4
print(obj.isjoin(0,1)) #Check connection between 0 and 1
print(obj.isjoin(1,2)) #Check Connection between 1 and 2
print(obj.isjoin(2,4))