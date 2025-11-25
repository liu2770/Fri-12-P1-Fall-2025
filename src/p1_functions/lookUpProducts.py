def lookup_products(products):
    '''Returns a 2D list of products and their prices from the inputted string that matched a product in the products.csv file.
    Outputting an error print if any inputted product names didn't match any in products.csv. Made by KRYSTEN SCASE, 400628749'''
    file = open("./content/products.csv") #open file
    wanted_products = products.split(" ") # List of products that were in the string of "products"
    final_list = []
    products_file = []

    for line in file: # Stripping white space from lines and appending to product_file list, making a 2D list of available products
        line_copy = line
        line_copy = line_copy.strip()
        products_file.append(line_copy.split(","))

    for index in range(len(products_file)): # Turning price values into integers or float if price isn't a whole number
        if "." in products_file[index][1]:
            products_file[index][1] = float(products_file[index][1])
        else:
            products_file[index][1] = int(products_file[index][1])

    for name in wanted_products:
        match = False
        for index in range(len(products_file)): # Checking for matches between list of available products and input string of wanted products
            if name == products_file[index][0]:
                match = True
                index_match = index
        if match == True: # Match
            final_list.append(products_file[index_match]) # Appending final list with matched product list and price
        elif match == False: # No Match (error)
            print(f"Error, product '{name}' not found")

    file.close()
    return final_list
