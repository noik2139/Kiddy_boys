n = 300
with open('test.py','w') as file:
    file.write("list = [")
    for i in range(n):
        if i != 0:
            file.write("        [")
        else:
            file.write("[")
        for j in range(n):
            file.write('{},'.format(j+i*i))
        file.write('],\n')

    file.write('       ]')
    file.write("\nprint(list[20][40])")
