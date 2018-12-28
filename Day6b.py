def calculate_distance(coord, data):
    return sum([abs(coord[0] - l[0]) + abs(coord[1] - l[1]) for l in data])

input = open("Day6.txt", "r")
data = [tuple(int(c) for c in val.replace(" ", "").split(',')) for val in input.read().replace("+","").split('\n') if val]

min_x = min(data, key=lambda c: c[0])[0]
max_x = max(data, key=lambda c: c[0])[0]
min_y = min(data, key=lambda c: c[1])[1]
max_y = max(data, key=lambda c: c[1])[1]

areas = []

for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        distance = calculate_distance((x,y), data)
        if distance < 10000:
            areas.append((x,y))

print(len(areas))
