import re

def main(lines):
	total = 0
	pattern = r'\([0-9\+\*\s]*?\)'
	for line in lines:
		while len(matches := re.findall(pattern, line)) > 0:
			for match in matches:
				inside = match[1:-1]
				result = evaluate(*split(inside))
				line = line.replace(match, str(result))
		total+=evaluate(*split(line))
	print("TOTAL:",total)


def evaluate(runningTotal, line):
	print(f"evaluating: {runningTotal}  {line}")
	operator1 = runningTotal
	operator2 = int(re.match(r'[0-9]+',line[1:])[0])
	operand = line[0]
	if operand == '+':
		operator1 += operator2
	if operand == '*':
		operator1 *= operator2
	if '+' in line[1:] or '*' in line[1:]:
		return evaluate(operator1, str(operator2).join(line.split(str(operator2))[1:]))
	else:
		return operator1

def split(line):
	pre = re.match(r'[0-9]+',line)[0]
	post = pre.join(line.split(pre)[1:])
	return int(pre),post


if __name__ == '__main__':
    lines = open('./input.txt').read().replace(' ','').splitlines()
    main(lines)