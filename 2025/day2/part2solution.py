def solution():
    with open("input.txt", "r") as f:
        ranges = f.read().strip().split(",")
        count = 0
        for num_range in ranges:
            first_num, second_num = num_range.split("-")
            for num in range(int(first_num), int(second_num) + 1):
                if isInvalid(str(num)):
                    count += int(num)
        return count


def isInvalid(s):
    n = len(s)
    if n < 2:
        return False
    for block_len in range(1, n // 2 + 1):
        if n % block_len != 0:
            continue
        first_block = s[:block_len]
        if first_block * (n // block_len) == s:
            return True
    return False
    


print(solution())