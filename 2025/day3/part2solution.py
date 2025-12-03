def solution():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            stack = []
            line = line.strip()
            nums = [int(ch) for ch in line]
            toRemove = len(nums) - 12
            for num in nums:
                while toRemove > 0 and stack and stack[-1] < num:
                    stack.pop()
                    toRemove -= 1
                stack.append(num)
            if len(stack) > 12:
                stack = stack[:12]
            value = 0
            for digit in stack:
                value = value * 10 + digit
            count += value
        return count
        
print(solution())