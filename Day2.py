input = open("Day2.txt", "r")
boxes = [val for val in input.read().replace("+","").split('\n') if val]
twos, threes = 0, 0
for id in boxes:
    if [True for char in id if id.count(char) == 2]:
        twos += 1
    if [True for char in id if id.count(char) == 3]:
        threes += 1
        
print(twos * threes)
