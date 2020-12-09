instructions = open("./input.txt").read().splitlines()
# Normalize the input into a touple of (instruction, argument)
for i,ins in enumerate(instructions):
    instructions[i] = (ins[0:3], int(ins[5:]) if ins[4] == '+' else int(ins[5:])*-1)
print("Instruction set length:",len(instructions))
visited = set()
acc = 0
pc = 0
while True:
    if pc in visited:
        print(f"Acc is at: {acc}, pc is: {pc}")
        break
    visited.add(pc)
    ins,arg = instructions[pc]
    if ins == "nop":
        pc += 1
        continue
    if ins == "acc":
        pc += 1
        acc += arg
    if ins == "jmp":
        pc += arg