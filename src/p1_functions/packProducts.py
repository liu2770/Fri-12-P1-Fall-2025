def pack_products(product_list):
    for product in product_list:
        if product in product_list:
            ##Product moving code
            print(f"{product[0]} has been packed")
        else:
            print("The product you are looking for is not available, please try again")
    print("testing!")   #!Remove this line, stub
    return

# product_list = []

# file = open("./content/products.csv", "r")

# for line in file:
#     product = []
#     for word in line.split(","):
#         product.append(word)

# print(product_list)
