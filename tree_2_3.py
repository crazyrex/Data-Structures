
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
			return self.root.addContentsToList(out)
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
						return Node23(new,
							self.a,
							Node23(self.midSub, self.b, self.rightSub))
			else:
				if self.b == None:
					new = self.rightSub.insert(item)
					if new != None:
						self.b = new.a
						self.midSub = new.leftSub
						self.rightSub = new.rightSub
				else:
					if item < self.b:
						new = self.midSub.insert(item)
						return Node23(
							Node23(self.leftSub, self.a, new.leftSub),
							new.val,
							Node23(new.leftSub, self.b, self.rightSub))
					else:
						new = self.rightSub.insert(item)
						return Node23(
							Node23(self.leftSub, self.a, self.rightSub),
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
	
	def getString(self):
		subList = ["", ""]
		if self.leftSub != None:
			leftList = self.leftSub.getString()
			for i in range(0, len(leftList)):
				while i+2>=len(subList):
					subList.append("")
				subList[i+2] += leftList[i]
			afterBar = False
			for i in leftList[0]:
				if i == "|":
					afterBar = True
				if afterBar:
					subList[1]+="_"
				else:
					subList[1]+=" "
				subList[0]+=" "
		subList[1]+=str(self.a)
		subList[0]+="|"
		
		
		return subList
	
		"""
	def makeDiagram(self, grid, level):
		lowX=0
		hghX=0
		if self.leftSub != None:
			self.leftSub.makeDiagram(grid, level+2)
		if level+2<len(grid):
			lowX = len(grid[level+2])
				#grid[level] += " "*(len(grid[level+2])-len(grid[level])+1)
				#grid[level+1] += " "*(len(grid[level+2])-len(grid[level+1]))
			#while level+1>=len(grid):
			#	grid.append("")
			#grid[level] += "|"
			#grid[level+1] += str(self.a)
		if self.midSub != None:
			self.midSub.makeDiagram(grid, level+2)
		if level+2<len(grid):
			hghX = len(grid[level+2])
		if self.rightSub != None:
			self.rightSub.makeDiagram(grid, level+2)
		
		while level>=len(grid):
			grid.append("")
		
		if lowX > 0:
			grid[level]+=" "*(lowX-len(grid[level]))
			#grid[level]+=" "*lowX
			#grid[level]+=
		
		grid[level]+=str(self.a)
		
		if self.b != None:
				grid[level] += "--"
				grid[level] += str(self.b)
			
	
		if self.a != None:
			if level+2<len(grid):
				grid[level] += " "*(len(grid[level+2])-len(grid[level]))
				grid[level+1] += " "*(len(grid[level+2])-len(grid[level+1]))
			while level+1>=len(grid):
				grid.append("")
			grid[level] += "|"
			grid[level+1] += str(self.a)
		"""
	
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
			bStr = str(self.b)
		
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
		out[0] += " "*len(midGrid[0])
		
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
		
		out.append(self.a)
		
		if self.b != None:
			if self.midSub != None:
				self.midSub.addContentsToList(out)
			
			out.append(self.b)
		
		if self.rightSub != None:
			self.rightSub.addContentsToList(out)






