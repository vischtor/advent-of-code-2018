input = open("Day8.txt", "r")
data = [int(val) for val in input.read().split() if val]

class Node:
    def __init__(self, header, entries):
        self.header = header
        self.entries = entries

def create_node(header):
    for i in range(header[0]):
        create_node((data.pop(0), data.pop(0)))
    entries = []
    for i in range(header[1]):
        entries.append(data.pop(0))
    node = Node(header, entries)
    nodes.append(node)


nodes = []
create_node((data.pop(0), data.pop(0)))

print(sum([sum(node.entries) for node in nodes]))
