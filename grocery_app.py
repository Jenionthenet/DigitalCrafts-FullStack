shopping_list = []

"""def view_shopping_lists(arr):
    i = 1
    for index in range(0, len(arr)):
        store = arr[index]
        print(f"{i} - store name: {store.title},   store address: {store.address}")"""

   
class ShoppingList:
    def __init__(self, title, address):
        self.title = title
        self.address = address
        self.items = []
        
        
class Items:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity 
    

while True:

    print("")
    print("1 to Add a store to your shopping list")
    print("2 to Add items to your shopping list")
    print("3 to View your shopping lists")
    print("q to Quit")
    print("")

    option = input("Enter your option: ")

    
    if option == "1":
        store_name = input("Enter store name: ")
        store_addy = input("Enter store address: ")
        store = ShoppingList(store_name, store_addy)
        shopping_list.append(store)

    if option == "2":
      

        for i in range(0, len(shopping_list)):
            print(f"{i + 1} - {shopping_list[i].title}")
            store = shopping_list[i]
        store_index = int(input("Enter the store number: "))
        item_name = input("Enter the name of the item: ")
        price = float(input("Enter the price: "))
        quantity = int(input("Enter the quantity: "))
        thing = Items(item_name, price, quantity)
        
        shopping_list[store_index -1].items.append(thing)
      
     

    if option == "3":
        i = 1
        for index in range(0, len(shopping_list)):
            store = shopping_list[index]
            print(f"{i} - store name: {store.title},   store address: {store.address}")
            i += 1
        for index in range(0, len(store.items)):
            title = store.items[index].title
            quantity = store.items[index].quantity 
            print(title, quantity)
    
        
       
    if option == "q":
        break

    else: 
        print("Please enter a choice from the menu.")