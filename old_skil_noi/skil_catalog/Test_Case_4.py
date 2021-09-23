from catalog import Item
from catalog import Catalog

item1 = Item("12 Angry Men", "Drama")
item2 = Item("The Godfather", "Crime")
item3 = Item("Schindler's List", "Biography")
item4 = Item("Pulp Fiction", "Crime")
catalog = Catalog('Films')
catalog.add(item1)
catalog.add(item2)
catalog.add(item3)
catalog.add(item4)
catalog.remove(item3)
catalog.set_name("My Favorites")
print(catalog)