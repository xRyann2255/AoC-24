f = [(int(calibration), [int(nums) for nums in nums.split()]) for (calibration, nums) in (l.strip().split(":") for l in open("7.txt"))]

def eval_line(nums, configuration):
    nums_copy = nums.copy()
    operations = ["+" if char == "0" else "*" for char in configuration]
    result = nums_copy.pop(0)
    exp = zip(operations, nums_copy)
    for pair in exp:
        operation, num = pair
        if operation == "+":
            result += num
        elif operation == "*":
            result *= num
    return result

def check(line):
    calibration, nums = line
    num_configurations =  2 ** (len(nums) - 1)
    for i in range(num_configurations):
        if calibration == eval_line(nums, bin(i)[2:].zfill(len(nums) - 1)):
            return calibration
    return 0

answer = 0
for line in f:
    answer += check(line)

print(answer)

# Part 2

def eval_line_part2(nums, configuration):
    nums_copy = nums.copy()
    operations = ["+" if char == "0" else ("*" if char == "1" else "||") for char in configuration]
    result = nums_copy.pop(0)
    exp = zip(operations, nums_copy)
    for pair in exp:
        operation, num = pair
        if operation == "+":
            result += num
        elif operation == "*":
            result *= num
        elif operation == "||":
            result = int(str(result) + str(num))
    return result

def to_ternary(n, padding):
    if n == 0:
        return "0".zfill(padding)
    ternary = ""
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3
    return ternary.zfill(padding)

def check_part2(line):
    calibration, nums = line
    num_configurations =  3 ** (len(nums) - 1)
    for i in range(num_configurations):
        if calibration == eval_line_part2(nums, to_ternary(i, len(nums) - 1)):
            return calibration
    return 0

answer = 0
total_lines = len(f)
for i, line in enumerate(f):
    print(f"{i}/{total_lines}: {line}") # Progress Bar
    answer += check_part2(line)

print(answer)