zero = [" -- ","| |", "| |", "   ", "| |", "| |", " -- "]
one = ["   "," |"," |","   "," |"," |","   "]
two = [" -- "," |"," |"," -- ","| ","| "," -- "]
three = [" -- "," |"," |"," -- "," |"," |"," -- "]
four = ["   ","| |","| |"," -- "," |"," |","   "]
five = [" -- ","| ","| "," -- "," |"," |"," -- "]
six = [" -- ","| ","| "," -- ","| |","| |"," -- "]
seven = [" -- "," |"," |","   "," |"," |","   "]
eight = [" -- ","| |","| |"," -- ","| |","| |"," -- "]
nine = [" -- ","| |","| |"," -- "," |"," |"," -- "]
digits = [zero,one,two,three,four,five,six,seven,eight,nine]
conv = {"ugol":"x", "l":"-", "stolb":"|", "space":' '}

s = input()
length = conv["l"] * (len(s) * 4 + (len(s)))
line = ''
print(conv["ugol"] + length + conv["ugol"])
for j in range(0,7):
    line = conv["stolb"]
    for i in s:
        line += str(digits[int(i)][j]) + conv["space"]
    line += conv["stolb"]
    print(line)
print(conv["ugol"] + length + conv["ugol"])