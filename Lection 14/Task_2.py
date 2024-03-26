class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        if dish_name in self.menu:
            dish_info = self.menu[dish_name]
            if dish_info['quantity'] >= quantity:
                total_cost = dish_info['price'] * quantity
                dish_info['quantity'] -= quantity
                return total_cost
            else:
                return "Requested quantity not available"
        else:
            return "Dish not available"


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))   
print(mc.order('burger', 15))  
print(mc.order('soup', 5))     