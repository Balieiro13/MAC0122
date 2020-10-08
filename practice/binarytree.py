'''
Algoritmo para uma binary tree usando classes: from @LucidProgramming
'''

class Node(object):
    def __init__(self, valor=None):
        self.valor = valor
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, travesal_type):
        if travesal_type == "preorder":
            return self.preoder_print(self.root, "")
        elif travesal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif travesal_type == "postorder":
            return self.postorder_print(self.root, "")
        else:
            print("N tem esse travesal ai n")

    def preoder_print(self, start, traversal):
        if start:
            traversal += (str(start.valor) + '-')
            traversal = self.preoder_print(start.left, traversal)
            traversal = self.preoder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.valor) + '-')
            traversal = self.inorder_print(start.right, traversal)
            return traversal

        def postorder_print(self, start, traversal):
            if start:
                traversal = self.inorder_print(start.left, traversal)
                traversal = self.inorder_print(start.right, traversal)
                traversal += (str(start.valor) + '-')
            return traversal

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert (self, data, noodles):
        if data < noodles.valor:
            if noodles.left is None:
                noodles.left = Node(data)
            else:
                self._insert(data, noodles.left)
        elif data > noodles.valor:
            if noodles.right is None:
                noodles.right = Node(data)
            else:
                self._insert(data, noodles.right)
        else:
            print("esse valor já existe na árvore")

def procura(self, data):
    if self.root:
        achou = self._procura(data, self.root)
        if achou:
            return True
        return False
    else:
        return None

def _procura(self, data, noodles):
    if data < noodles.valor:
        if noodles.left is None:
            return False
        else:
            return self._procura(data, noodles.left)
    elif data > noodles.valor:
        if noodles.right is None:
            return False
        else:
            return self._procura(data, noodles.right)
    return True