#Catlog.py skilaverkefni


class Item():
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def set_name(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

    def __str__(self):
        return "Name: {}, Category: {}".\
            format(self.name, self.category)
    
    



class Catalog():

    def __init__(self, name):
        self.name = name
        self.collection = {}

    def add(self, item):
        self.collection[item.name] = item.category
    
    def remove(self, item):
        del self.collection[item.name]
    
    def set_name(self,name):
        self.name = name

    def find_item_by_name(self, item):
        try:
            self.collection[item]
        except:
            #ekkert gerist
            return "None"
        else:
            return "Name: {}, Category: {}".\
                format(item, self.collection[item])

    def __str__(self):
        str_out = "Catalog {}:".format(self.name)
        for key in self.collection:
            str_out += "\n\tName: {}, Category: {}".\
            format(key, self.collection[key])

        return str_out

    def clear(self):
        self.collection = {}


        
    
