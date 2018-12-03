input = open("Day2.txt", "r")
boxes = [val for val in input.read().replace("+","").split('\n') if val]
for box in boxes:
    for compare_box in boxes:
        matches = ''.join([char for i, char in enumerate(box) if compare_box[i] == char])
        if len(matches) == (len(box) - 1):
            print(matches)
