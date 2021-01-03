import re
from Day_19_classes import Node, Rulebook

def main(rules,messages):
	rulebook = Rulebook(*parseRules(rules))
	
	# print(rulebook.getRule('4'))	
	master = rulebook.getRule('0')

	print(len([m for m in messages if m in master]))
	

	# for rule,definition in rules.items():
	# 	print("working on rule:", rule)
	# 	if not rule in tree:
	# 		ruleNode = Node(rule)
	# 		tree[rule] = ruleNode
	# 	else:
	# 		ruleNode = tree[rule]
	# 	nodes = definition.split(' ')
	# 	for node in nodes:
	# 		if node == '|':
	# 			continue
	# 		# check if this node already exists in the tree
	# 		if node in tree:
	# 			node = tree[node]
	# 		else:
	# 			# convert it to a node
	# 			name = node
	# 			node = Node(node)
	# 			tree[name] = node
	# 		ruleNode.addChild(node)



def parseRules(rules):
	ruleMapper = {}
	for rule in rules:
		name = re.match(r'[0-9]+', rule)[0]
		definition = re.search(r':.*', rule)[0][2:]
		print(f"line: [{rule}] || Name: {name} | Def: {definition}")
		if '"a"' in definition:
			definition = 'a'
			aIdx = name
		if '"b"' in definition:
			definition = 'b'
			bIdx = name
		ruleMapper[name] = definition
	print(ruleMapper)
	return ruleMapper, aIdx, bIdx

# def expandRule(rule, ruleMapper):
# 	if not re.search(r'[0-9]', ruleMapper[rule]):
# 		print(f'Hit bottom for rule [{rule}], value={ruleMapper[rule]}')
# 		return ruleMapper[rule]
# 	else:
# 		newDef = []
# 		branch = ''
# 		parts = ruleMapper[rule].split(' ')
# 		for part in parts:
# 			print("checking:", part)
# 			if part == '|':
# 				newDef.append(branch)
# 			else:
# 				branch += expandRule(part, ruleMapper)
# 		ruleMapper[rule] = newDef
# 		print(f'RULE [{rule}] NOW HAS DEF [{newDef}]')
# 		return newDef



if __name__ == '__main__':
	lines = open('./input.txt').read().splitlines()
	rules = []
	messages = []
	swap = False
	for line in lines:
		if len(line) < 2:
			swap = True
			continue
		if not swap:
			rules.append(line)
		else:
			messages.append(line)
	main(rules, messages)