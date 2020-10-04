'''
Algoritmo para uma binary tree usando classes: from @LucidProgramming
'''

class Node(object):
	def __init__(self, valor):
		self.valor = valor
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def print_tree(self, travesal_type):
		if travesal_type == "preorder":
			return self.preoder_print(tree.root, "")
		elif travesal_type == "inorder":
			return self.inorder_print(tree.root, "")
		elif travesal_type == "postorder":
			return self.postorder_print(tree.root, "")
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


#           1
#       /      \
#     2         3
#    /  \      /  \
#  4     5    6    7
#                    \
#                     8


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree("preorder")[:-1])
print(tree.print_tree("inorder")[:-1])
print(tree.print_tree("postorder")[:-1])
