
class Tree23:
	def __init__(self):
		self.root = None
	
	def insert(self, item):
		if self.root == None:
			self.root = Node23(item)
		else:
			self.root.insert(item)
	
	def searchFor(self, item):
		if self.root == None:
			return False
		else:
			return self.root.searchFor(item)

class Node23:
	def __init__(self, val):
		self.a = val
		self.b = None
		self.leftSub = None
		self.midSub = None
		self.rightSub = None
	
	def insert(self, item):
		
		pass
	
	def searchFor(self, item):
		if self.a == item:
			return True
		elif item < self.a:
			if self.leftSub == None:
				return False
			else:
				return self.leftSub.searchFor(Item)
		elif self.b == None:
			if self.rightSub == None:
				return False
			else:
				return self.rightSub.searchFor(item)
		elif self.b == item:
			return True
		elif item < self.b:
			if self.midSub == None:
				return False
			else:
				return self.midSub.searchFor(item)
		else:
			if self.rightSub == None:
				return False
			else:
				return self.rightSub.searchFor(item)
		






