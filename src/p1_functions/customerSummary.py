def customer_summary(userid):
    file = open("content/products.csv",'r')
    products = []

    for line in file:
        name = line.strip().split(",")
        products.append(name[0])        #add product names to products list

    file.close()
   
    product_count = [0]*len(products)        #create a list has the same length as products list to store number of product

    validation = False
    num_orders = 0
    total_spent = 0

    file = open("content/orders.csv",'r')
    for line in file:
        line = line.strip().split(",")

        if line[0] == userid:        #search for the userid that was asked
            validation = True
            num_orders += 1        #plus one to number of order
            total_spent += float(line[1])        #add the money spend on this order to total spend

            for i in range (len(products)):
                for i2 in range (2,len(line)):        
                    if line[i2].strip() == products[i]:        #search for product name from each valid line by reading product name list
                        product_count[i] += 1


    if validation is True:
        print("===================================")
        print(f" Customer Summary for {userid}")
        print("===================================")
        print(f" Total Orders : {num_orders}")
        print(f" Total Spent  : ${total_spent:.2f}")
        print("------------ Products -------------")

        for i in range(len(products)):
            if product_count[i] != 0:             #print product quantity if not 0
                print(f"{products[i]:<15}| {product_count[i]}")
        print("===================================")

    else:
        print("Invalid username")        #if userid not found, invalid username

