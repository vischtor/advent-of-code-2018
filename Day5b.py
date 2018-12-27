input = open("Day5.txt", "r")
input_data = [val for val in input.read().replace("+","").split('\n') if val][0]
lengths = []

for char in "abcdefghijklmnopqrstuvwxyz":
    if char in input_data:
        finished = False
        data = input_data.replace(char,"")
        data = data.replace(char.upper(),"")
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
        lengths.append(len(data))
        print("CHAR: " + char + " gives shortest: " + str(len(data)))
print(min(lengths))
            

