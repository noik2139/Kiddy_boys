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


def not_int_to_zero(item):
    if is_float(item) == True:
        item = float(item)
    else:
        item = 0
    return item

def avg_of_list(list_inn):
    sum_of_list = sum(list_inn)
    length_of_list = len(list_inn)
    avg_of_list = sum_of_list/length_of_list
    return avg_of_list


with open('file.txt') as file:
    master_list = [[], [], []]
    for line in file:
        if line != '\n':
            line_list = line.split()
            for i in range(1, 3):
                line_list[i] = not_int_to_zero(line_list[i])
        for i in range(3):
            master_list[i].append(line_list[i])

        print(bjutify(line_list))
    print(master_list)
    #print('{:.2f}'.format(int(avg_of_list(master_list[1]))))
