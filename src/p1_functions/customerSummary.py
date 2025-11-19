def customer_summary(userid):
    file = open("content/products.csv",'r')
    products = []

    for line in file:
        name = line.strip().split(",")
        products.append(name[0])

    file.close()
   
    product_count = [0]*len(products)

    validation = False
    num_orders = 0
    total_spent = 0

    file = open("content/orders.csv",'r')
    for line in file:
        line = line.strip().split(",")

        if line[0] == userid:
            validation = True
            num_orders += 1
            total_spent += float(line[1])

            for i in range (len(products)):
                for i2 in range (2,len(line)):
                    if line[i2].strip() == products[i]:
                        product_count[i] += 1


    if validation is True:
        print("===================================")
        print(f" Customer Summary for {userid}")
        print("===================================")
        print(f" Total Orders : {num_orders}")
        print(f" Total Spent  : ${total_spent:.2f}")
        print("------------ Products -------------")

        for i in range(len(products)):
            if product_count[i] != 0: #print product quantity if not 0
                print(f"{products[i]:<15}| {product_count[i]}")
        print("===================================")

    else:
        print("Invalid username")

