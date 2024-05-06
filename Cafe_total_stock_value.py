Cafe_name = "Welcome to MIANA's cafe"

Menu = ['Pizza', 'Hot dog', 'Panini', 'English breakfast']

# Dictionary called "stock" which contains the stock value. 

Stock = { 'Pizza': 900, 'Hot dog' : 500, 'Panini' : 700,
        'English breakfast' : 1500}

# A dictionary called "price" which contains individual product prices. 

Prices =  {'Pizza': 15, 'Hot dog':  7, 'Panini': 8,
        'English breakfast': 12}

x = 0

# You can calculate the total stock worth by looping through the menu list, 
# and for each item, multiply its stock value by its price, like in the following:

for item in Menu:
    item_value =  (Stock[item] * Prices[item])
    x += item_value
 
print("Stock value:\n", Stock, "\n")
print("Product prices:\n", Prices, "\n") 
print ("The total stock worth is:", x, "£")    # x = value for total stock worth.
