def customer_summary(userid):
    file = open("orders.csv",'r')
    validation = False
    num_orders = 0
    total_spent = 0
    products = ["Sponge", "Bottle", "Rook", "D12", "Bowl", "WitchHat"]
    product_count = [0,0,0,0,0,0]
    for line in file:
        line = line.strip().split(",")
        if line[0] == userid:
            validation = True
            num_orders += 1
            total_spent += float(line[1])
            for p in range (len(products)):
                for i in range (len(line)):
                    if line[i] == products[p]:
                        product_count[p] += 1

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

