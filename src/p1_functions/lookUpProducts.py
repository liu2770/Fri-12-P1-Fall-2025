def lookup_products(products):  #TODO:General lack of comments
    file=open("./content/products.csv","r")
    items = products.split(",")
    list = []   #TODO:variable names are hard to distinguish
    products_file = []
    for line in file:
        line_copy = line
        line_copy = line_copy.replace("\n","")
        products_file.append(line_copy.split(","))
    for name in items:
        match = False
        for index in range(len(products_file)):
            if name == products_file[index][0]:
                match = True
                index_match = index
        if match == True:   #TODO:redundant if statements
            list.append(products_file[index_match])
        elif match == False:
            print(f"Error, product '{name}' not found")
    file.close()
    return list #?On the P1 documents it says "Make sure the data types are correct." Does it mean we need to make prices into floats?
