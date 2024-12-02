f = [[int(num) for num in l.strip().split(" ")] for l in open("2.txt")]
answer = 0

def is_safe(line):
    if line == sorted(line) or line == list(reversed(sorted(line))):
        for i in range(len(line) - 1):
            difference = abs(line[i] - line[i + 1])
            if difference < 1 or difference > 3:
                return False
        return True
    return False

for line in f:
    if is_safe(line):
        answer += 1

print(answer)

# Part 2

for line in f:
    if not is_safe(line):
        for i in range(len(line)):
            if is_safe(line[:i] + line[i + 1:]):
                answer += 1
                break

print(answer)