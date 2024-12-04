f = [l.strip() for l in open("4.txt")]
rows = len(f)
cols = len(f[0])

answer = 0

directions = [
    (0, 1),   # Right
    (1, 1),   # Bottom-Right
    (1, 0),   # Bottom
    (1, -1),  # Bottom-Left
    (0, -1),  # Left
    (-1, -1), # Top-Left
    (-1, 0),  # Top
    (-1, 1)   # Top-Right
]
words = ['XMAS']

def search(row, col, dr, dc):
    row += dr
    col += dc
    for ch in "MAS":
        if 0 <= row < rows and 0 <= col < cols and f[row][col] == ch:
            row += dr
            col += dc
        else:
            return False
    return True

for row in range(rows):
    for col in range(cols):
        if f[row][col] == "X":
            for dr, dc in directions:
                if search(row, col, dr, dc):
                    answer += 1

print(answer)

# Part 2

answer = 0

def top_right(row, col):
    if f[row-1][col+1] == "M" and f[row+1][col-1] == "S":
        return True
    elif f[row-1][col+1] == "S" and f[row+1][col-1] == "M":
        return True
    
    return False

def search_mas(row, col):

    # Top-Left 
    if f[row-1][col-1] == "M" and f[row+1][col+1] == "S":
        return top_right(row, col)
    elif f[row-1][col-1] == "S" and f[row+1][col+1] == "M":
        return top_right(row, col)
    
    return False
    
for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        if f[row][col] == "A" and search_mas(row, col):
            answer += 1

print(answer)

