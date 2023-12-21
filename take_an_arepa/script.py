class Menu:
    # Initialize a menu with a name, a dictionary of items with prices, and its availability times
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # the menu as a string showing its name and available times
    def __str__(self):
        return "{} menu available from {} to {}".format(self.name, self.start_time, self.end_time)

    # Calculate the total bill for a list of purchased items from the menu
    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return total

# Create various menus for the restaurant chain
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50,
    'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird_dinner_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 
    'coffee': 1.50, 'espresso': 3.00,
}
dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 
    'coffee': 2.00, 'espresso': 3.00,
}
kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
#instances of the menu class
brunch_menu = Menu("Brunch", brunch_items, 11, 16)
early_bird_dinner_menu = Menu("Early-bird", early_bird_dinner_items, 15, 18)
dinner_menu = Menu("Dinner", dinner_items, 17, 23)
kids_menu = Menu("Kids Menu", kids_items, 11, 21)

# Define the Franchise class to manage different restaurant locations
class Franchise:
    # Initialize a franchise with its address and a list of menus
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # Represent the franchise as a string showing its address
    def __str__(self):
        return f"Franchise located at {self.address}"

    # Find out which menus are available at a given time
    def available_menus(self, time):
        available_menus = [menu for menu in self.menus if time >= menu.start_time and time <= menu.end_time]
        return available_menus

# Create franchises for the restaurant chain
all_menus = [brunch_menu, dinner_menu, early_bird_dinner_menu, kids_menu]
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)

# Display available menus at flagship store at specific times
print("Menus available at 12 PM at the flagship store:")
for menu in flagship_store.available_menus(12):
    print(menu)
print("Menus available at 5 PM at the flagship store:")
for menu in flagship_store.available_menus(17):
    print(menu)

# Define a new Arepa menu for a new business venture
arepas_menu = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Define the Business class to manage entire restaurant businesses
class Business:
    # Initialize a business with its name and a list of franchises
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises
