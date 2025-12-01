def solution():
    count = 0
    with open("input.txt", "r") as f:
        num = 50
        for line in f:
            line = line.strip()
            direction_char = line[0]
            direction = -1 if direction_char == "L" else 1
            distance = int(line[1:])

            start = num

            full_turns = distance // 100
            partial = distance % 100
            count += full_turns

            if direction == 1:  # R
                if start + partial >= 100:
                    count += 1
            else:  # L
                if start != 0 and partial >= start:
                    count += 1

            num = (start + direction * distance) % 100

    return count

print(solution())