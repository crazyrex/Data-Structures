
class Node:
	def __init__(self, val):
		self.edges = []
		self.val = val

class Graph:
		
	def __init__(self):
		self.nodes = []
	
	def addNode(self, node):
		self.nodes.append(node)
	
	def nodesToString(self):
		out = ""
		for i in self.nodes:
			out += str(i.val) + "\n"
		return out
