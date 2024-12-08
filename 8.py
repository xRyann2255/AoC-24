# line by line input
from collections import defaultdict

antenna_locations = defaultdict(list)

f = [l.strip() for l in open("8.txt")]

n, m = len(f), len(f[0])

for i in range(n):
    for j in range(m):
        if f[i][j] != ".":
            antenna_locations[f[i][j]].append((i, j))

antinodes = set()
for frequency in antenna_locations:
    for antenna_1 in antenna_locations.get(frequency):
        (y1, x1) = antenna_1
        for antenna_2 in antenna_locations.get(frequency):
            (y2, x2) = antenna_2
            if antenna_1 == antenna_2:
                continue
            antinode = (2 * y2 - y1, 2 * x2 - x1)
            # Out of bounds check
            if not (antinode[0] < 0 or antinode[0] >= n or
            antinode[1] < 0 or antinode[1] >= m):
                antinodes.add(antinode)

print(len(antinodes))

# Part 2
antinodes_part2 = set()
for frequency in antenna_locations:
    for antenna_1 in antenna_locations.get(frequency):
        (y1, x1) = antenna_1
        for antenna_2 in antenna_locations.get(frequency):
            (y2, x2) = antenna_2
            if antenna_1 == antenna_2:
                continue
            antinode = (y2, x2)
            distance = (y2 - y1, x2 - x1)
            # Out of bounds check
            while not (antinode[0] < 0 or antinode[0] >= n or
            antinode[1] < 0 or antinode[1] >= m):
                antinodes_part2.add(antinode)
                antinode = tuple(a + b for a, b in zip(antinode, distance))

print(len(antinodes_part2))
            
            