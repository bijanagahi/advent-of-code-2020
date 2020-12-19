def main(lines):
    differences = [0,0,0,0]
    current = 0
    for jolt in lines:
        differences[jolt-current]+=1
        current = jolt
    differences[3]+=1 # account for the 'build-in' adapter that always has a diff of 3 
    print(differences[1]*differences[3])

if __name__ == '__main__':
    lines = open('./input1.txt').read().splitlines()
    main(sorted([int(_) for _ in lines]))