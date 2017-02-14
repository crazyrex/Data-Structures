
class Tree23:
	def __init__(self):
		self.root = None

	def insert(self, item):
		if self.root == None:
			self.root = Node23(item)
		else:
			new = self.root.insert(item)
			if new != None:
				self.root = new

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

	def __init__(self, leftIn, val, rightIn):
		self.a = val
		self.b = None
		self.leftSub = leftIn
		self.midSub = None
		self.rightSub = rightIn

	def insert(self, item):
		if self.leftSub == None: # if this node is a leaf
			if self.b == None:
				if item < self.a:
					self.b = self.a
					self.a = item
				else:
					self.b = item
			else:
				if item < self.a:
					return Node23(Node23(item), self.a, Node23(self.b))
				elif item < self.b:
					return Node23(Node23(self.a), item, Node23(self.b))
				else:
					return Node23(Node23(self.a), self.b, Node23(item))
		else: # If this node is not a leaf
			if item < self.a:
				new = self.leftSub.insert(item)
				if new != None:
					if self.b == None:
						self.b = self.a
						self.a = new.val
						self.leftSub = new.leftSub
						self.midSub = new.rightSub
					else:
						return Node23(new, self.a, Node23(self.midSub, self.b, self.rightSub))
			else:
				if self.b == None:
					new = self.rightSub.insert(item)
					if new != None:
						self.b = new.val
						self.midSub = new.leftSub
						self.rightSub = new.rightSub
				else:
					if item < self.b:
						new = self.midSub.insert(item)
						return Node23(
							Node23(self.leftSub, self.a, new.leftSub),
							new.val,
							Node23(new.leftSub, self.b, self.rightSub)
						)
					else:
						new = self.rightSub.insert(item)
						return Node23(Node23(self.leftSub, self.a, self.rightSub), self.b, new)


	def searchFor(self, item):
		if self.a == item or self.b == item:
			return True
		elif item < self.a:
			if self.leftSub == None:
				return False
			else:
				return self.leftSub.searchFor(Item)
		elif self.b == None or item > self.b:
			if self.rightSub == None:
				return False
			else:
				return self.rightSub.searchFor(item)
		else:
			if self.midSub == None:
				return False
			else:
				return self.midSub.searchFor(item)
