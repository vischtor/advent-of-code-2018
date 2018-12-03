input = open("Day1.txt", "r")
values = [int(val) for val in input.read().replace("+","").split('\n') if val]
current = 0
previous = set()
finished = False
while not finished:
    for value in values:
        current += value
        if current in previous:
            finished = True
            break
        previous.add(current)

print(current)
