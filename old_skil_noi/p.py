def clean(list_inn):
    word = ''
    list_out = []
    no_no = ['!', '"', "'", ',','.','\n']
    for item in list_inn:
        word = ''
        for char in item:
            if not char in no_no:
                word+= char
        if word != '':
            list_out.append([word])
    return list_out

def unic(list_inn):
    list_out = []
    for item in list_inn:
        if not item in list_out:
            list_out.append([item])
    return list_out



file_name = input("Enter filename: ")
file = open(file_name, "r")


jass = []
low = []
for line in file:
    words = line.split(' ')
    jass.append(clean(words))
    jass = unic(jass)
    out = tuple(jass)
    out = sorted(out)
    print(out)


print(low)