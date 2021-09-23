equation_str = input("Enter an equation: ")
anwser = float
is_Error = False

while equation_str != 'q':
    
    equation_list = equation_str.split()
    is_Error = False

    if equation_list[0].isnumeric() == True and equation_list[2].isnumeric() == True:
        
        num_1 = int(equation_list[0])
        num_2 = int(equation_list[2])
        operator = equation_list[1]

        if operator == '+':
            anwser = num_1+num_2
        
        elif operator == '-':
            anwser = num_1-num_2

        elif operator == '*':
            anwser = num_1*num_2
        
        elif operator == '/':
            if num_2 != 0:
                anwser = num_1/num_2
            else:
                print("Can't divide by 0")
                is_Error = True
        
        else:
            print("Invalid operator")
            is_Error = True

    else:
        print("Invalid operands")
        is_Error = True

    if is_Error == False:
        print('Result: {:5.2f}'.format(round(anwser,2)))

    equation_str = input("Enter an equation: ")
