def hex_digit_to_dec(hex_digit):
    # This function takes a single hex digit and turns it to a decimal value
    hex_digit = str(hex_digit)
    if hex_digit.upper() == 'A':
        dec_out = 10
    elif hex_digit.upper() == 'B':
        dec_out = 11
    elif hex_digit.upper() == 'C':
        dec_out = 12
    elif hex_digit.upper() == 'D':
        dec_out = 13
    elif hex_digit.upper() == 'E':
        dec_out = 14
    elif hex_digit.upper() == 'F':
        dec_out = 15
    else:
        dec_out = int(hex_digit)

    return dec_out


def dec_to_hex_digit(dec):
    # this function takes a decimal values from 0 to 16 and turns it to a single hex digit
    dec = int(dec)
    if dec == 10:
        hex_digit = 'A'
    elif dec == 11:
        hex_digit = 'B'
    elif dec == 12:
        hex_digit = 'C'
    elif dec == 13:
        hex_digit = 'D'
    elif dec == 14:
        hex_digit = 'E'
    elif dec == 15:
        hex_digit = 'F'
    else:
        hex_digit = dec

    return hex_digit


def decimal_to_hex_str(dec_int):
    # This takes decimals and turn them into hex
    dec_int = int(dec_int)
    hex_string = ''
    while dec_int > 0:
        hex_string = str(dec_to_hex_digit(dec_int % 16))+hex_string
        dec_int = dec_int//16
    return hex_string


def hex_str_to_decimal(hex_str):
    # This function takes hex and turn them into decimal
    hex_str = str(hex_str)
    lengt_of_str = len(hex_str)
    sum = 0
    list_of_hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                          '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']

    # runs throug the numbers one by one to convert each induviduali
    for i in range(0, lengt_of_str):
        # Here i'm using a function that handel small hex numbers, smaller then 15(in dec)
        if hex_str[i] in list_of_hex_digits:
            number = hex_digit_to_dec(hex_str[i])
            # the formula is a bit nasty but works to revese i
            sum += number*(16**(lengt_of_str-i-1))
        else:
            return None
    return sum


def print_options():
    print("")
    print("d. Decimal to hex")
    print("h. Hex to decimal")
    print("x. Exit")
    print("")


def display_menu():
    # The main code baby!!!
    print_options()
    main_input = input('Enter option: ')
    is_no_error = False

    while main_input != "x":
        if main_input == 'd':
            dec_int = int(input("Decimal number: "))
            hex_string = decimal_to_hex_str(dec_int)
            print(f'The hex is {hex_string}')

        elif main_input == 'h':
            hex_string = input('Hex number: ')
            dec_int = hex_str_to_decimal(hex_string)
            print(f'The decimal is {dec_int}')

        elif main_input == 'x':
            break

        else:
            print("Invalid option!")

        print_options()
        main_input = input("Enter option: ")


# the actual code starts here baby!!! (The most ambitious crossover event in history! function within function within function and stuff)
display_menu()
