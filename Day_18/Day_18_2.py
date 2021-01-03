# Special thank you to wikipedia for this one
# https://en.wikipedia.org/wiki/Operator-precedence_parser#Pseudocode

import re

class t():
	def __init__(self, line):
		self.line = re.split('([\+\*])', line)

	def peek(self):
		if len(self.line) > 0:
			return self.line[0]
		else:
			return None
	def __len__(self):
		return len(self.line)

	def __iter__(self):
		return self
	def __next__(self):
		if len(self.line) == 0:
			return None
		token = self.line[0]
		self.line = self.line[1:]
		return token

def main(lines):
	total = 0
	pattern = r'\([0-9\+\*\s]*?\)'
	for line in lines:
		while len(matches := re.findall(pattern, line)) > 0:
			for match in matches:
				inside = match[1:-1]
				tokens = t(inside)
				result = parse(int(next(tokens)), 0, tokens)
				line = line.replace(match, str(result))
		tokens = t(line)
		result = parse(int(next(tokens)), 0, tokens)
		total+=result
	print("TOTAL:",total)

def parse(lhs, min_precedence, tokens):
	lookahead = tokens.peek()
	if not lookahead:
		return lhs
	while precedence(lookahead) >= min_precedence:
		if len(tokens) == 0:
			return lhs
		op = lookahead
		next(tokens) # advance after peeking
		rhs = int(next(tokens))
		lookahead = tokens.peek()
		if lookahead:
			while precedence(lookahead) > precedence(op):
				rhs = parse(rhs, precedence(lookahead), tokens)
				lookahead = tokens.peek()
				if not lookahead:
					break
		lhs = evaluate(lhs, op, rhs)
	return lhs

def precedence(op):
	return 1 if op == '*' else 2

def evaluate(lhs, op, rhs):
	if op == '*':
		return lhs*rhs
	else:
		return lhs+rhs

if __name__ == '__main__':
    lines = open('./input.txt').read().replace(' ','').splitlines()
    main(lines)