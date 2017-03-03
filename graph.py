
class Node:
	def __init__(self, val):
		self.edges = []
		self.val = val
	
	def getStr(self):
		out = str(self.val)
		
		if len(self.edges) > 0:
			out += ": "
		
		for i in range(0, len(self.edges)):
			if i != 0:
				out += ", "
			out += str(i.val)
		
		out += "\n"
		return out

class Graph:
		
	def __init__(self):
		self.nodes = []
	
	def addNode(self, node):
		self.nodes.append(node)
	
	def nodesToString(self):
		out = ""
		for i in self.nodes:
			out += i.getStr()
		return out
