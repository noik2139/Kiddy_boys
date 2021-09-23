#fall sem tekur inn skrá og finnur nafnið á dálkum í textaskrá
#og skilar þeim í lista

def read_table(file):
    count= 0
    is_space = 0
    is_space_2 = 0
    titles = []
    title = ""
    #tekur in nýja línu
    for line in file:
        #svo að bara fyrsta línan er tekin
        if count== 0:
            #skoðar hvern staf í línunni og ef stafurinn er ekki bil þá bætist
            # stafurinn við hálfgert dummy orð en ef það kemur bil eftir staf þá fer dummy orðið
            # í lista
            for letter in line:
                is_space_2 = is_space
                if letter == " ":
                    is_space = 1
                else:

                    
                    is_space = 0

                if is_space != True:
                    title += letter
                    
                else:
                    if is_space_2 != is_space:
                        title = [title]
                        titles += title
                    else:
                        title = ""
        #til að fallið sé ekki of lengi
        else:
            return titles
            break
        count+= 1
