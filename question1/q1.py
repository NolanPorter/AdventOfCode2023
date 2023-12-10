def part1() -> int:
    val = 0
    with open('input.txt') as f:
        for line in f.readlines():
            arr = [x for x in line if x.isnumeric()]
            num = int(''.join([arr[0], arr[-1]]))
            val += num
    return val

def part2() -> int:
    words = {
        "one": 1, 
        "two": 2, 
        "three": 3, 
        "four": 4, 
        "five": 5, 
        "six": 6, 
        "seven": 7, 
        "eight": 8, 
        "nine": 9
    }
    val = 0
    with open('input.txt') as f:
        for line in f.readlines():
            arr = []
            builder = ""
            scanning = 0
            scanned = 0
            for c in line:
                builder += c
                if c.isnumeric():
                    arr.append(int(c))
                else:
                    for word in words:
                        if word in builder[scanned:]:
                            arr.append(words[word])
                            scanned = scanning
                scanning += 1
            num = arr[0]*10 + arr[-1]
            val += num
        
    return val


print(part1())
print(part2())