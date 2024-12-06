f = [l.strip() for l in open("6.txt")]

num_rows, num_cols = len(f), len(f[0])

directions = [
    (-1, 0),  # Up
    (0, 1),   # Right
    (1, 0),   # Down
    (0, -1),  # Left
]

def turn_right(dir_index):
    return (dir_index + 1) % len(directions)

def forward(guard_position, escaped, visited):
    i, j, dir_index = guard_position
    di, dj = directions[dir_index]
    new_i = i + di
    new_j = j + dj
    if (new_i < 0 or new_i >= num_rows or
    new_j < 0 or new_j >= num_cols):
        escaped = True
        return guard_position, escaped, visited
    elif f[new_i][new_j] == "#":
        return (i, j, turn_right(dir_index)), escaped, visited
    else:
        if (new_i, new_j) not in visited:
            visited.add((new_i, new_j))
        return (new_i, new_j, dir_index), escaped, visited

escaped, visited = False, set()

for i in range(num_rows):
    for j in range(num_cols):
        if f[i][j] == "^":
            visited.add((i, j))
            initial_guard_position = (i, j, 0)

guard_position = initial_guard_position
while not escaped:
    guard_position, escaped, visited = forward(guard_position, escaped, visited)

print(len(visited))

# Part 2

answer = 0
guard_position = initial_guard_position
escaped, loop, visited = False, False, set()

def forward_part2(guard_position, escaped, visited, loop, answer):
    i, j, dir_index = guard_position
    di, dj = directions[dir_index]
    new_i = i + di
    new_j = j + dj
    if (new_i < 0 or new_i >= num_rows or
    new_j < 0 or new_j >= num_cols):
        escaped = True
        return guard_position, escaped, visited, loop, answer
    elif new_f[new_i][new_j] == "#":
        return (i, j, turn_right(dir_index)), escaped, visited, loop, answer
    else:
        if (new_i, new_j, dir_index) in visited:
            loop = True
            answer += 1
            return (new_i, new_j, dir_index), escaped, visited, loop, answer
        visited.add((new_i, new_j, dir_index))
        return (new_i, new_j, dir_index), escaped, visited, loop, answer

for i in range(num_rows):
    for j in range(num_cols):
        guard_position = initial_guard_position
        escaped, loop, visited = False, False, set()
        new_f = [row[:] for row in f]
        if new_f[i][j] != ".":
            continue
        else:
            row_list = list(new_f[i])
            row_list[j] = "#"
            new_f[i] = "".join(row_list)
            while not loop and not escaped:
                 guard_position, escaped, visited, loop, answer = forward_part2(guard_position, escaped, visited, loop, answer)

print(answer)