input = open("Day1.txt", "r")
values = [int(val) for val in input.read().replace("+","").split('\n') if val]
print(sum(values))
