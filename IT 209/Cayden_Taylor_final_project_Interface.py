
from Cayden_Taylor_final_project_CLASS import Item, SmartCart

class MyInterface():
    def __init__(self):
        self.SmartCart = cart()
        purchase_list = []
        subtotal = 0
        #cart() = self.SmartCart
	# initialize
	# use SmartCart class here
	
    def welcome(self):  # welcome screen
        print('****Welcome to Instant Cart!****')
        print('''Choose Option:
        1. Start Ordering
        2. Exit Order''')
        app_status = input('What is your option? ')
        # If else condition
        if int(app_status) == 1:#loop for 
            self.shop_by_category()
        else:
            quit
        self.checkout()

    def shop_by_category(self):
        subtotal = 0#initaialize
        cat_choice = 0
	
        print('''Choose Category
            Option 1: Dairy
            Option 2: Vegitables/Fruits
            Option 3: Meat
            Option 4: Seafood
            Option 5: Exit''')
        cat_choice = input('What is your category: ')
        while cat_choice != 5:#while loop to repeat while customers  chooses 
            self.shop_by_category()#call function

            if cat_choice == 1:#option 1 for dairy items
                for item in Item.dairy_items:
                    print(item.get_name(), end='')
                print()
                self.add_to_cart(item_cat = Item.dairy_items)

            if cat_choice == 2:#option 2 for veg and fruit items
                for item in Item.veg_fruit_items:
                    print(item.get_name(), end='')
                print()
                self.add_to_cart(item_cat = Item.veg_fruit_items)

            if cat_choice == 3:#option 3 for meat items
                for item in Item.meat_items:
                    print(item.get_name(), end='')
                print()
                self.add_to_cart(item_cat = Item.meat_items)

            if cat_choice == 4:#option 4 for seafood items 
                for item in Item.seafood_items:
                    print(item.get_name(), end='')
                print()
                self.add_to_cart(item_cat = Item.seafood_items)

            else:
                print("invalid option")
            
        # Use while loop. Also use if-else condition.


    def add_to_cart(self,item_cat):
        while True:
            item_to_add = input('Item Name|Unit: ')
            if item_to_add.lower() == 'done':
                break
            else:
                item_name, unit = item_to_add.split('|')
                for item in item_cat:
                    if item_name == item.get_name():
                        # self.subtotal += item.get_price() * int(unit)
                        self.cart[item] = int(unit)
    def checkout(self):
        
        for k, v, in self.cart.item() #checkout with key and values from dictionary 
        self.cart.subtotal() #call subtotal function
        
        
		# Use the cart instance to print items
		# calculate subtotal, tax, total

my_interface = MyInterface()
my_interface.welcome()
