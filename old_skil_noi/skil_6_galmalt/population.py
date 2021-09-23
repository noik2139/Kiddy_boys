

#gefur 1 ef bók/tölustafur en annars 0
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


#tekur á móti skjali og breytir því svo í töflu/fylki
#(samt bara lista af listum)


def file_2_matrix(file):
#-----------------------------<_____file_2_matrix_____>------------------------------------#
    row_count = 0
    matrix = [[]]


    for line in file:
        collum_count = 0
        space_counter = 0
        item = ''
#-------------------------<_____main_part_of_function_____>--------------------------------#
        
#skoðar hvert stak í línnuni og ef stakið er tölu/bókstafur þá bætist stakið í "item"
#þessi kóði sér til þess að nýtt item verður til ef að nýr stafur kemur eftir tvö eða meiri bil
#þessi kóði sér til þess að búa ekki til nýtt item ef það er bara eitt bil (t.d new york ætti að vera vera eitt "item")
        
        for letter in line:
            if is_number_or_letter(letter) and space_counter != 1:
                item += letter
                space_counter = 0

            elif is_number_or_letter(letter) and space_counter == 1:
                item += ' ' + letter
                space_counter = 0

            elif not is_number_or_letter(letter) and space_counter == 0:
                space_counter = 1

            elif not is_number_or_letter(letter) and space_counter == 1:
                if row_count == 0:
                    matrix.append([])
                space_counter = 2
                matrix[collum_count].append(item)
                item = ''
                collum_count += 1
                
        space_counter = 2
        matrix[collum_count].append(item)
        item = ''
        collum_count += 1

#-------------------------<_____main_part_of_function/end_____>------------------------------#
        row_count += 1


    return matrix
        
#-----------------------------<_____file_2_matrix/end_____>------------------------------------#





   


#------------------------------<_____main_code_____>-----------------------------------------


#byrjar á að leita af skjalinu ef ekki þá villumelding
try:
    file_name = input('Enter filename: ')
    file = open(file_name, "r")

    
except:
    print("Filename " + file_name + " not found!")

    
else:
    matrix = file_2_matrix(file)

    row_lenght = len(matrix[0])
    collum_length = len(matrix)
    
    #while-lykkja sem bíður þángað til notandi slær inn gildi sem
    #passar við gildið á eitt af hausum dálkanna
    year = input("Enter year: ")
    year_list = []
    valid = 0
    while not valid:
        for i in range(collum_length):
            if matrix[i][0] == year:
                year_list = matrix[i][1::]
                valid= 1
                break
        if not valid:
            print("Invalid year!")
            year = input("Enter year: ")
                

    #finnur lægsta/hægsta gildið á dálkinum sem notaninn sló inn
    #og setur það gildi og gildið úr fyrsta dálkinum sem er í sömu röð
    #saman í tubles
    state_list = matrix[0][1::]
    year_list = [int(i) for i in year_list]
    min_year = min(year_list)
    max_year = max(year_list)
    min_state = state_list[year_list.index(min_year)]
    max_state = state_list[year_list.index(max_year)]
    
    #veit ekki afhverju, en það stendur í verkefnalýsingu
    min_tubles = (min_year, min_state)
    max_tubles = (max_year, max_state)


    #printar loka gildin
    print("Minimum: " + str(min_tubles))
    print("Maximum: " + str(max_tubles)) 
    
        
        
    

    


    
