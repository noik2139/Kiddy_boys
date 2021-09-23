def bjutify(list):
    """prints the stuff the right way baby!!!"""
    line = '{:<12}{:>12.2f}{:>12.2f}'.format(
        list[0], list[1], list[2])
    return line


def is_float(item):
    bool_float = True
    try:
        float(item)
    except:
        bool_float = False

    return bool_float


with open('file.txt') as file:
    for line in file:
        if line != '\n':
            line_list = line.split()
            for i in range(1, 3):
                if is_float(line_list[i]) == True:
                    line_list[i] = float(line_list[i])
                else:
                    line_list[i] = 0

            print(bjutify(line_list))
