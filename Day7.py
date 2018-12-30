input = open("Day7.txt", "r")
data = [val.split() for val in input.read().split('\n') if val]

right = {}
left = {}
all_nodes = set()

for instruction in data:
    parent = instruction[1]
    this = instruction[7]
    if this in left:
        left[this].append(parent)
    else:
        left[this] = [parent]
    if parent in right:
        right[parent].append(this)
    else:
        right[parent] = [this]
    all_nodes.add(parent)
    all_nodes.add(this)

starts = [node for node in right if node not in left]
nodes = []
for node in starts:
    left[node] = []
    nodes.append(node)

order = ""
current_index = 0

while len(order) < len(all_nodes):
    nodes.sort()
    current = nodes[current_index]
    if all((node in order for node in left[current])):
        current_index = 0
        order += current
        nodes.remove(current)
        if current in right:
            for child in right[current]:
                if all((node in order for node in left[child])):
                    nodes.append(child)
    else:
        current_index += 1
print(order)
