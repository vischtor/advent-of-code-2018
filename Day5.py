input = open("Day5.txt", "r")
data = [val for val in input.read().replace("+","").split('\n') if val][0]

finished = False

while not finished:
    upper = 65
    lower = upper + 32
    finished = True
    while upper <= 90:
        old_data = data
        data = data.replace(chr(upper)+chr(lower), "")
        data = data.replace(chr(lower)+chr(upper), "")
        if data != old_data:
            finished = False
        upper+=1
        lower+=1
print(len(data))
            

