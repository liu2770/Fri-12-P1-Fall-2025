def customer_summary(userid):
    file = open("./content/orders.csv",'r')
    validation = False
    userlines = []
    for line in file:
        line = line.strip().split(",")
        if line[0] == userid:
            validation = True
            userlines.append(line)

    if validation is True:
        num_orders = len(userlines)  # total number of orders
        total_spent = 0.0
        product_count = [0, 0, 0, 0, 0, 0]
        products = ["Sponge", "Bottle", "Rook", "D12", "Bowl", "WitchHat"]

        for order in userlines:
            product = str(order[1])
            qty = int(order[2])
            price = float(order[3])
            total_spent += qty * price  # total spent of orders

            for i in range(len(products)):  #store quantity of each product into the list
                if product == products[i]:
                    product_count[i] += qty

        print("===================================")
        print(f" Customer Summary for {userid}")
        print("===================================")
        print(f" Total Orders : {num_orders}")
        print(f" Total Spent  : ${total_spent:.2f}")
        print("------------ Products -------------")

        for i in range(len(products)):
            if product_count[i] != 0:   #print product quantity if not 0
                print(f"{products[i]}             | {product_count[i]}")
                
        print("===================================")

    else:
        print("Invalid username")
