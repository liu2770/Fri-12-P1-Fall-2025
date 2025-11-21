import random

def complete_order(userid, product_list):
    tax = 0.13   #sets tax to 0.13 percent
    random_discount = random.uniform(0.05,0.50)   #generates random float value between 0.05 and 0.50 for discount

    subtotal = 0   #sets subtotal to 0

    product = []   #empty list to store product names

    for i in range(len(product_list)):   #for loop that appends product names from products.csv to product list
        product_names = product_list[i][0]
        product.append(product_names)
    ordered_products = ", ".join(product)

    print(ordered_products)

    for i in range(len(product_list)):   #for loop that calculates order subtotal based on price of ordered products
        price = float(product_list[i][1])
        subtotal += price

    discount = subtotal * random_discount   #calculates discount based on subtotal and random discoun value

    pre_tax_total = subtotal - discount   #calculates pre-tax price of order

    tax_applied = pre_tax_total * tax   #calculates tax on order

    total = round(pre_tax_total + tax_applied, 2)   #calculates order total and rounds it to 2 decimal places

    total = str(total)

    order_count = 0   #initializes order count to keep track of customer orders

    filename = "./content/orders.csv"   #sets filename to orders.csv so it can be opened later

    file = open(filename, "r")   #opens orders.csv to read from

    for line in file:   # for loop that runs through each line in the file to find other instances of orders by user
        for word in line.split(","):  
            if word == userid:
                order_count += 1

    file.close()

    file = open(filename, "a")   #opens orders.csv to append new order

    file.write(userid + ", " + total + ", " + ordered_products + "\n")   #writes user order and total under userid
    order_count += 1

    print(order_count)

    print("\n   FRI-12 Warehouse   ")   #print statements that print formatted reciept 
    print(f"-" * 25)

    for i in range(len(product_list)):
        product_name = product_list[i][0]
        product_price = float(product_list[i][1])
        print(f"{product_name:<11}{'$' + format(float(product_price), ',.2f'):>15}")

    print("-" * 25)
    print(f"{'Subtotal':<10}{'$' + format(subtotal, ',.2f'):>15}")
    print(f"{'Discount':<10}{'$' + format(discount, ',.2f'):>15}")
    print(f"{'Tax':<10}{'$' + format(tax_applied, ',.2f'):>15}")
    print(f"{'Total':<10}{'$' + format(float(total), ',.2f'):>15}")
