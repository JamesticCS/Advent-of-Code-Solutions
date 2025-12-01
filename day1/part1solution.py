def solution():
    count = 0
    with open("input.txt", "r") as f:
        num = 50
        for line in f:
            line = line.strip()   # remove \n
            direction_char = line[0]
            direction = -1 if direction_char == "L" else 1
            distance = int(line[1:])
            num = (num + direction * distance) % 100
            if num == 0:
                count += 1

    return count

print(solution())