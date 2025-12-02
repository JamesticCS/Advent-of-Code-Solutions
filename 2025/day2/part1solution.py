def solution():
    with open("input.txt", "r") as f:
        ranges = f.read().strip().split(",")
        count = 0
        for num_range in ranges:
            first_num, second_num = num_range.split("-")
            for num in range(int(first_num), int(second_num) + 1):
                if len(str(num)) % 2 == 0 and isInvalid(str(num)):
                    count += int(num)
        return count


def isInvalid(s):
    half = len(s) // 2
    first_half = s[:half]
    second_half = s[half:]
    return first_half == second_half


print(solution())
