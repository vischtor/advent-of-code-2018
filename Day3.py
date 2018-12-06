import itertools
from collections import defaultdict

input = open("Day3.txt", "r")
data = [val for val in input.read().replace("+","").split('\n') if val]
fabric = defaultdict(int)
for claim in data:
    id, _, coordinates, size = claim.split()
    x,y = coordinates.replace(":","").split(",")
    w,h = size.split("x")
    x,y,w,h = int(x), int(y), int(w), int(h)
    
    for coordinate in itertools.product(range(x, x+w), range(y, y+h)):
        fabric[coordinate] += 1

print(sum([1 for x in fabric if fabric[x] >= 2]))
