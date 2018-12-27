import operator

def get_closest(coord, data):
    min_dist = 99999
    min_location = (-1,-1)
    for location in data:
        dist = abs(coord[0] - location[0]) + abs(location[1] - coord[1])
        if dist < min_dist:
            min_dist = dist
            min_location = location
        elif dist == min_dist:
            min_location = (-1,-1)

    if min_location == (-1,-1):
        return False
    return min_location


input = open("Day6.txt", "r")
data = [tuple(int(c) for c in val.replace(" ", "").split(',')) for val in input.read().replace("+","").split('\n') if val]

min_x = min(data, key=lambda c: c[0])[0]
max_x = max(data, key=lambda c: c[0])[0]
min_y = min(data, key=lambda c: c[1])[1]
max_y = max(data, key=lambda c: c[1])[1]

areas = {}

for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        closest = get_closest((x,y), data)
        if closest:
            if x == min_x or x == max_x or y == min_y or y == max_y:
                areas[closest] = -1
            else:
                if closest in areas:
                    areas[closest] += 1
                else:
                    areas[closest] = 1
                

print(max(areas.items(), key=operator.itemgetter(1))[1])
