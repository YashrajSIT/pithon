#defining the function to calculate the total
def total_price(product_quantities,price):
    #calculateing the total price of each product
    totalprice=[product_quantities[i]*price[i] for i in range(len(product_quantities))]
    print("total price of each product=",totalprice)
    #calculating the grand total of product
    grandtotal=sum(totalprice)
    print("the grand total= ",grandtotal)

#giving the input of product_quantity and its price
product_quantities=[13,5,6,10,11]
price=[1.2,6.5,1.0,4.8,5.0]
#calling the function total_price to calculate the total price of the product
total_price(product_quantities,price)

