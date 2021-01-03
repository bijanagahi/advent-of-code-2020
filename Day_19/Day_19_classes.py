class Rulebook(object):
	def __init__(self, rules, aIdx, bIdx):
		self.rules = rules
		self.aIdx = aIdx
		self.bIdx = bIdx
		self.completed = {aIdx:[rules[aIdx]],bIdx:[rules[bIdx]]}

	def getRule(self, name):
		print(f'Getting rule for [{name}]')
		if name in self.completed:
			return self.completed[name]
		else:
			print("Not found, need to complete it first")
			return self.completeRule(name)

	def completeRule(self, name):
		# print(f"Completing rule [{name}]")
		rule = []
		fragment1 = None
		fragment2 = None
		parts = self.rules[name].split(' ')
		for part in parts:
			if part == '|':
				rule.extend(self.mergeFragments(fragment1, fragment2))
				fragment1 = None
				fragment2 = None
			else:
				if not fragment1:
					# print("assigning fragment1")
					fragment1 = self.getRule(part)
				elif not fragment2:
					# print("assigning fragment2")
					fragment2 = self.getRule(part)
				else:
					raise ValueError
		rule.extend(self.mergeFragments(fragment1, fragment2))
		# print(f"Final completed rule for [{name}]: {rule}")
		self.completed[name] = rule
		return rule

	def mergeFragments(self, fragment1, fragment2):
		# print(f"Merging {fragment1} and {fragment2}")
		subrule = []
		if not fragment2:
			return fragment1
		for a in fragment1:
			for b in fragment2:
				subrule.append(a+b)
		return subrule

				
	
	def __str__(self):
		return "Completed rules: "+str(self.completed)


class Node(object):

	def __init__(self, name):
		self.name = name
		self.leftChildren = []
		self.rightChildren = []
		self.value = []

	def addChild(self,child):
		if len(self.leftChildren) == 2:
			print(f"[{self.name}]: Adding {child.name} to right children")
			self.rightChildren.append(child)
		else:
			print(f"[{self.name}]: Adding {child.name} to left children")
			self.leftChildren.append(child)

	def setValue(self,value):
		self.values.extend(value)

	def __str__(self):
		return f'node [{self.name}] value: {self.value}'