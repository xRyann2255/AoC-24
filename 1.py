left = []
right = []
length = 0
answer = 0

for line in open("1.txt"):
    parts = line.split("   ")
    left.append(int(parts[0]))
    right.append(int(parts[1]))
    length += 1

left.sort()
right.sort()

for i in range(length):
    answer += abs(left[i] - right[i])

print(answer)

# Part 2

answer = 0

for num in left:
    answer += num*right.count(num)

print(answer)
