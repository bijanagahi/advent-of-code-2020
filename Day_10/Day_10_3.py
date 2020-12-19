def main(lines):
    splits = 1
    count = 1
    for jolt in lines[1:]:
        splits = 0 # count the splits
        for i in range(1,4):
            if jolt+i in lines:
                splits+=1
        if splits > 1:
            print(f"Splitting at {jolt}")
            count += splits
    print(count)
if __name__ == '__main__':
    lines = open('./test.txt').read().splitlines()
    main(sorted([int(_) for _ in lines]))