input = open("Day8.txt", "r")
data = [int(val) for val in input.read().split() if val]

class Node:
    def __init__(self, header, entries, children):
        self.header = header
        self.entries = entries
        self.children = children

    def calc_value(self):
        if len(self.children) == 0:
            self.value = sum(self.entries)
        else:
            for child in self.children:
                child.calc_value()
            value = 0
            for index in self.entries:
                if len(self.children) >= index:
                    value += self.children[index-1].value
            self.value = value


def create_node(header):
    children = []
    for i in range(header[0]):
        children.append(create_node((data.pop(0), data.pop(0))))
    entries = []
    for i in range(header[1]):
        entries.append(data.pop(0))
    node = Node(header, entries, children)
    nodes.append(node)
    return node

nodes = []
create_node((data.pop(0), data.pop(0)))
nodes[-1].calc_value()

print(nodes[-1].value)
