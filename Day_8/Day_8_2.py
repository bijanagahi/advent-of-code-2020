def main(instructions):
    superPC = findNextSwapLocation(instructions, 0)
    lastRun = False
    instructions[superPC] = swap(instructions[superPC])
    lastRun = runCode(instructions)
    while True:
        if lastRun:
            print("Done!")
            break
        if superPC >= len(instructions)-1:
            print("Exhausted all possible combinations :(")
            break
        # Don't forget to swap back
        instructions[superPC] = swap(instructions[superPC])
        superPC+=1
        # Find location of next instruction to swap
        superPC = findNextSwapLocation(instructions, superPC) 
        # Swap it
        instructions[superPC] = swap(instructions[superPC])
        # Now try again
        lastRun = runCode(instructions)

def findNextSwapLocation(instructions, superPC):
    while True:
        if instructions[superPC][0] == 'acc':
            superPC += 1
        else:
            return superPC

def swap(instruction):
    ins, arg = instruction
    return ('jmp', arg) if ins =='nop' else ('nop',arg)

'''
Attempt to run the instructions provided.
If there is an infinite loop or if there is an attempt to jump to an invalid location,
return False.
If the PC reaches the last line of the instructions, return the value of the acc.
'''
def runCode(instructions):
    # print("\n\nRunning code with instruction set:")
    # print("**************")
    # for line, (ins, arg) in enumerate(instructions):
    #     print(f"{line}|{ins}|{arg}|")
    # print("**************")
    visited = set()
    acc = 0
    pc = 0
    while True:
        if pc in visited:
            return False
        if pc >= len(instructions):
            print(f"PC [{pc}] is past length. Acc is at {acc}")
            return True
        if pc < 0:
            return False
        visited.add(pc)
        ins,arg = instructions[pc]
        if ins == "nop":
            pc += 1
            continue
        if ins == "acc":
            pc += 1
            acc += arg
        if ins == "jmp":
            if pc+arg < 0:
                print(f"Bad jump at {ins}|{arg}")
            pc += arg

if __name__ == "__main__":
    instructions = open("./input.txt").read().splitlines()
    # Normalize the input into a touple of (instruction, argument)
    for i,ins in enumerate(instructions):
        instructions[i] = (ins[0:3], int(ins[5:]) if ins[4] == '+' else int(ins[5:])*-1)
    print(f"Loaded {len(instructions)} instructions.")
    main(instructions)