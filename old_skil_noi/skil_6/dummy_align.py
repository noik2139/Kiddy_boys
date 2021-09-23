def bjutify(item1,item2,item3):
    """prints the stuff the right way baby!!!"""
    line = '{0:<12}{1:>12}{2:>12}'.format(
        item1, item2, item3)
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
