import itertools
from collections import defaultdict

input = open("Day3.txt", "r")
data = [val for val in input.read().replace("+","").split('\n') if val]
fabric = defaultdict(int)
claims = {}
for claim in data:
    id, _, coordinates, size = claim.split()
    x,y = coordinates.replace(":","").split(",")
    w,h = size.split("x")
    x,y,w,h = int(x), int(y), int(w), int(h)
    claims[id] = []
    for coordinate in itertools.product(range(x, x+w), range(y, y+h)):
        fabric[coordinate] += 1
        claims[id].append(coordinate)

for claim in claims:
    overlap = False
    for coordinate in claims[claim]:
        if fabric[coordinate] > 1:
            overlap = True
            break
    if not overlap:
        print(claim)
