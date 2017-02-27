
class Node:
	def __init__(self, val):
		self.edges = []
		self.val = val

class Edge:
	def __init__(self, a, b, val):
		self.a = a
		self.b = b
		self.val = val

class Graph:
		
	def __init__(self):
		self.nodes = []
		self.edges = []
	
	def addNode(self, val):
		self.nodes.append(Node(val))

