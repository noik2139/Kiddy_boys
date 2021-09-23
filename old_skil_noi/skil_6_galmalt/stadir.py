b = 0
word = ''
line = "xxx x     xx xxx   x x"

for letter in line:
    if letter.isalpha():
        if b != 1:
            word += letter
        else:
            word += " " + letter
        b = 0

    else:
        if b == 0:
            b+=1
        else:
            b = 2
            print(word)
            word = ""
print(word)
