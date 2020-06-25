class LanguageStat:
	def __init__(self, name, year, count):
		self.name = name
		self.year = year
		self.count = count

	def __str__(self):
		return self.name + str(self.count)

class Node:
	def __init__(self, language_stat, left = None, right = None, parent = None, height = 1, bf = 0):
		self.val = language_stat
		self.left = left
		self.right = right
		self.parent = parent
		self.height = height
		self.bf = bf
		self._val = str(language_stat)