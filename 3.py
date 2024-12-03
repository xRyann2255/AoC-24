import re

with open("3.txt", "r") as file:
    f = file.read()

answer = 0

matches = re.findall(r"mul\((\d+),(\d+)\)", f)

for (x, y) in matches:
    answer += int(x)*int(y)

print(answer)

# Part 2

answer = 0

matches_conditionals = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", f)

enable = True
for (x, y, do, dont) in matches_conditionals:
    if do == "do()":
        enable = True
    if dont == "don't()":
        enable = False
    if enable and x and y: 
        answer += int(x)*int(y)

print(answer)