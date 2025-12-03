def solution():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            line = line.strip()
            nums = [int(ch) for ch in line]

            maxDigitToRight = nums[-1]
            bestPair = 0
            for i in range(len(nums) - 2, -1, -1):
                currentDigit = nums[i]
                candidatePair = 10*currentDigit + maxDigitToRight
                bestPair = max(bestPair, candidatePair)
                maxDigitToRight = max(maxDigitToRight, currentDigit)
            count += bestPair
        return count       

print(solution())