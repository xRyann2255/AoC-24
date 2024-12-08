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
for frequency, antennas in antenna_locations.items():
    for (y1, x1) in antennas:
        for (y2, x2) in antennas:
            if (y1, x1) == (y2, x2):
                continue
            antinode = (2 * y2 - y1, 2 * x2 - x1)
            # Out of bounds check
            if (0 <= antinode[0] < n and 0 <= antinode[1] < m):
                antinodes.add(antinode)

print(len(antinodes))

# Part 2
antinodes_part2 = set()
for frequency, antennas in antenna_locations.items():
    for (y1, x1) in antennas:
        for (y2, x2) in antennas:
            if (y1, x1) == (y2, x2):
                continue
            distance = (y2 - y1, x2 - x1)
            # Out of bounds check
            while 0 <= y2 < n and 0 <= x2 < m:
                antinodes_part2.add((y2, x2))
                y2, x2 = tuple(a + b for a, b in zip((y2, x2), distance))

print(len(antinodes_part2))