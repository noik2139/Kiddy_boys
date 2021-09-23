#space for functions
print("svo nice að láta þetta virka")


def is_number_or_letter(char):
    if char.isalpha():
        return 1


    try:
        float(char)
    except:
        try:
            int(char)
        except:
            return 0
        else:
            return 1
    else:
        return 1


def file_2_uberlist(file):
    row_count = 0
    is_space_1 = 0
    is_space_2 = 0
    sub_list = []
    uber_list = []


    #les hverja línu í skjalinu
    for line in file:
        

        #telur fjölda dálka í skjalinu
        if row_count == 0:
            for letter in line:
                is_space_2 = is_space_1
                
                if letter == " ":
                    is_space_1 = True
                    
                else:
                    is_space_1 = False


                    

                if is_space_1 == False and is_space_2 == True:
                    uber_list.append([])

        #setur gildin úr töflnunni í lista
        else:
            collum_count = 0
            b = 0
            word = ''
            for letter in line:
                if is_number_or_letter(letter) and b != 1:
                    word += letter
                    b = 0
                if is_number_or_letter(letter) and b == 1:
                    word += ' ' + letter
                    b = 0
                elif not is_number_or_letter(letter) and b == 0:
                    b = 1

                elif not is_number_or_letter(letter) and b == 1:
                    b = 2
                    uber_list[collum_count].append(word)
                    word = ''
                    collum_count += 1


        row_count += 1


            

        

        
    return uber_list
        
    
   


#------------------------------

try:
    file_name = input('Enter a file name: ')
    file = open(file_name, "r")

    
except:
    print("file not found")

    
else:
    m = file_2_uberlist(file)
    print(m)

e = input("")
