def customer_summary(userid):
    file = open("orders.csv",'r')
    validation = False
    userlines = []
    num_orders = 0
    total_spent = 0

    for line in file:
        line = line.strip().split(",")
        if line[0] == userid:
            validation = True
            num_orders += 1
            total_spent += float(line[1])

    if validation is True:

        print("===================================")
        print(f" Customer Summary for {userid}")
        print("===================================")
        print(f" Total Orders : {num_orders}")
        print(f" Total Spent  : ${total_spent:.2f}")
        print("===================================")

    else:
        print("Invalid username")

customer_summary("test")
