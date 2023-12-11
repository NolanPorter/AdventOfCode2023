def part1() -> int:
    val = 0
    input_data = open('input.txt').read().splitlines()
    for line in input_data:
        arr = line.split(": ")
        arr_hands = arr[1].split("; ")
        valid_game = True
        for hand in arr_hands:
            dice = hand.split(", ")
            for type in dice:
                piece = type.split(" ")
                number = int(piece[0])
                color = piece[1]
                if not check(color, number):
                    valid_game = False
        if valid_game:
            val += int(arr[0].split(" ")[1])

    return val

def check(color, number) -> bool:
    if color == "green" and number > 13:
        return False
    elif color == "blue" and number > 14:
        return False
    elif color == "red" and number > 12:
        return False
    return True

def part2() -> int:
    val = 0
    input_data = open('input.txt').read().splitlines()
    green = 0
    red = 0
    blue = 0
    for line in input_data:
        arr = line.split(": ")
        arr_hands = arr[1].split("; ")
        for hand in arr_hands:
            dice = hand.split(", ")
            for type in dice:
                piece = type.split(" ")
                number = int(piece[0])
                color = piece[1]
                if color == "green" and number > green:
                    green = number
                elif color == "blue" and number > blue:
                    blue = number
                elif color == "red" and number > red:
                    red = number

        val += red*blue*green
        red = 0
        green = 0
        blue = 0
        
    return val


print(part1())
print(part2())