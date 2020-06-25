from utilities import *
	
class Languages:
	def __init__(self):
		self.data_by_year = {}

	def build_trees_from_file(self, file_object):
		file_object.readline()
		for line in file_object:
			line = line.strip().split(',')
			year = int(line[0])
			name = line[1]
			if line[2].isdigit() == True:
				count = int(line[2])
			
				language_entry = LanguageStat(name, year, count)
				node = Node (language_entry)
			
				if language_entry.year not in self.data_by_year.keys():
					tree = BalancingTree (node)
					self.data_by_year[language_entry.year] = tree
			
				else:
					tree = self.data_by_year[language_entry.year]
					tree.balanced_insert(node)
					self.data_by_year[language_entry.year] = tree
		
		return self.data_by_year
				
				
	def query_by_name(self, language_name):
		d = {}
		for i in self.data_by_year.keys():
			tree = self.data_by_year[i]
			current = tree.root
			while current != None:
				if language_name == current.val.name:
					d[i] = current.val.count
					break
				elif language_name < current.val.name:
					current = current.left
				elif language_name > current.val.name:
					current = current.right					
		return d
		
	def query_by_count(self, threshold = 0):
		self.number = threshold
		d = {}
		for i in self.data_by_year.keys():
			tree = self.data_by_year[i]
			current = tree.root
			l = []
			self.preorder (current, threshold, l)
			if l != []:
				d[i] = l
		return d
	
	
	def preorder (self, node, threshold, l):
		if node.val.count > threshold:
			l.append (node.val.name)
		if node.left:
			self.preorder(node.left, threshold, l)
		if node.right:
			self.preorder(node.right, threshold, l)



class BalancingTree:
	def __init__(self, root_node):
		self.root = root_node
	
	def balanced_insert(self, node, curr = None):
		curr = curr if curr else self.root
		self.insert(node, curr)
		self.balance_tree(node)


	def insert(self, node, curr = None):
		curr = curr if curr else self.root
		# insert at correct location in BST
		if node._val < curr._val:
			if curr.left is not None:
				self.insert(node, curr.left)
			else:
				node.parent = curr
				curr.left = node
		else:
			if curr.right is not None:
				self.insert(node, curr.right)
			else:
				node.parent = curr
				curr.right = node
		return


	def balance_tree(self, node):
		self.postorder(self.root)
		
		state = True
		temp = node
		while temp != None and state:
			temp_bf = self.find_balance_factor(temp)
			if abs(temp_bf) >1:
				state = False
			else:
				temp = temp.parent
				
		
		if temp_bf == 2 and state == False:
			temp_right_bf = self.find_balance_factor(temp.right)
			if temp_right_bf == 1:
				self.left_rotate(temp)
			elif temp_right_bf == -1:
				self.right_rotate(temp.right)
				self.left_rotate(temp)
				
		
		if temp_bf == -2 and state == False:
			temp_left_bf = self.find_balance_factor(temp.left)
			if temp_left_bf == -1:
				self.right_rotate(temp)
			elif temp_left_bf == 1:
				self.left_rotate(temp.left)
				self.right_rotate(temp)
		self.postorder(self.root)
		
				
	def postorder (self,node):
		if node.left:
			self.postorder (node.left)
		if node.right:
			self.postorder (node.right)			
		self.update_height(node)
		self.find_balance_factor(node)
		


	def update_height(self, node):
		node.height = 1 + max(self.height(node.left), self.height(node.right))


	def height(self, node):
		return node.height if node else -1


	def left_rotate(self, z):
		y = z.right
		y.parent = z.parent
		if y.parent is None:
			self.root = y
		else:
			if y.parent.left is z:
				y.parent.left = y
			elif y.parent.right is z:
				y.parent.right = y
		z.right = y.left
		if z.right is not None:
			z.right.parent = z
		y.left = z
		z.parent = y
		self.update_height(z)
		self.update_height(y)


	def right_rotate(self, z):
		y = z.left
		y.parent = z.parent
		if y.parent is None:
			self.root = y
		else:
			if y.parent.left is z:
				y.parent.left = y
			elif y.parent.right is z:
				y.parent.right = y
		z.left = y.right
		if z.left is not None:
			z.left.parent = z
		y.right = z
		z.parent = y
		self.update_height(z)
		self.update_height(y)		
				
		
		
	def find_balance_factor(self, node):
		bf = self.height(node.right) - self.height(node.left)
		node.bf = bf
		return bf


	def is_balanced(self):
		self.postorder(self.root)
		state = self.is_balanced_preorder(self.root)
		if state == False:
			return False
		else:
			return True
	
	def is_balanced_preorder (self, node):
		if self.find_balance_factor(node) < -1 or self.find_balance_factor(node) > 1:
			return False	
		if node.left:
			self.is_balanced_preorder (node.left)
		if node.right:
			self.is_balanced_preorder (node.right)	
	
	
	
	
	def printout (self):
		self.preorder(self.root)
				
	def preorder (self,node):
		print (self.find_balance_factor(node))
		if node.left:
			self.preorder (node.left)
		if node.right:
			self.preorder (node.right)			



