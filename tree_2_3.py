
class Tree23:
	def __init__(self):
		self.root = None

	def insert(self, item):
		if self.root == None:
			self.root = Node23(None, item, None)
		else:
			new = self.root.insert(item)
			if new != None:
				self.root = new

	def searchFor(self, item):
		if self.root == None:
			return False
		else:
			return self.root.searchFor(item)
	
	def getString(self):
		if self.root == None:
			return "[empty]"
		else:
			grid = self.root.makeDiagram()
			return "\n".join(grid)+"\n"
	
	def getList(self):
		if self.root == None:
			return []
		else:
			out = []
			self.root.addContentsToList(out)
			return out

class Node23:
	
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
					return Node23(
						Node23(None, item, None),
						self.a,
						Node23(None, self.b, None))
				elif item < self.b:
					return Node23(
						Node23(None, self.a, None),
						item,
						Node23(None, self.b, None))
				else:
					return Node23(
						Node23(None, self.a, None),
						self.b,
						Node23(None, item, None))
		else: # if this node has children
			if item < self.a: # if we want to insert the item into the left subtree
				new = self.leftSub.insert(item)
				if new != None: # if the operation ejected a node
					if self.b == None: # if we don't have a 'b' node and can just move 'a' over
						self.b = self.a
						self.a = new.a
						self.leftSub = new.leftSub
						self.midSub = new.rightSub
					else: # if we have a 'b', we must eject a new node headed by 'a'
						return Node23(new,
							self.a,
							Node23(self.midSub, self.b, self.rightSub))
			else: # if item is to the right of 'a'
				if self.b == None: # if 'b' is none we can just insert item to the right subtree
					new = self.rightSub.insert(item)
					if new != None: # we don't have to eject anything because we have room
						self.b = new.a
						self.midSub = new.leftSub
						self.rightSub = new.rightSub
				else: # b has a value so we have a choice between mid and right
					if item < self.b: # we insert the node in the middle
						new = self.midSub.insert(item)
						if new != None:
							return Node23(
								Node23(self.leftSub, self.a, new.leftSub),
								new.a,
								Node23(new.rightSub, self.b, self.rightSub))
					else:
						new = self.rightSub.insert(item)
						if new != None:
							return Node23(
								Node23(self.leftSub, self.a, self.midSub),
								self.b,
								new)


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
	
	def makeDiagram(self):
		leftGrid = [""]
		midGrid = [""]
		rightGrid = [""]
		aStr = ""
		bStr = ""
		
		if self.leftSub:
			leftGrid = self.leftSub.makeDiagram()
		if self.midSub:
			midGrid = self.midSub.makeDiagram()
		if self.rightSub:
			rightGrid = self.rightSub.makeDiagram()
		if self.a != None:
			aStr = str(self.a)
		if self.b != None:
			bStr = "="+str(self.b)
		
		out = [""]
		
		for i in range(0, len(leftGrid)):
			while len(out)<=i+1:
				out.append(" "*len(out[0]))
			out[i+1] += leftGrid[i]
		
		out[0] += " "*len(leftGrid[0])
		
		out[0]+=aStr
		for i in range(0, len(out)):
			out[i]+=" "*(len(out[0])-len(out[i]))
		
		for i in range(0, len(midGrid)):
			while len(out)<=i+1:
				out.append("#"*len(out[0]))
			out[i+1] += midGrid[i]
		out[0] += "="*len(midGrid[0])
		
		out[0]+=bStr
		for i in range(0, len(out)):
			out[i]+=" "*(len(out[0])-len(out[i]))
		
		for i in range(0, len(rightGrid)):
			while len(out)<=i+1:
				out.append(" "*len(out[0]))
			out[i+1] += rightGrid[i]
		
		out[0] += " "*len(rightGrid[0])
		
		return out
	
	def addContentsToList(self, out):
		if self.leftSub != None:
			self.leftSub.addContentsToList(out)
		
		if self.a != None:
			out.append(self.a)
		
		if self.midSub != None:
				self.midSub.addContentsToList(out)
		
		if self.b != None:
			out.append(self.b)
		
		if self.rightSub != None:
			self.rightSub.addContentsToList(out)






