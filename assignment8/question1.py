#making a dictionary named products to store the name and price of product
products=[
    {"name":"orange","price":20},
    {"name":"apple","price":8},
    {"name":"banana","price":10},
    {"name":"kiwi","price":30}
    
]

for product in products:
    #cheaking the price is >10 or not
    if product["price"]>10:
        #printing the name of item having price greater than 10
        print(product["name"])


