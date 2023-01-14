def rectangle(width, height):
    height =int (input("metter la longuuer: "))
    for i in height:
        if i == 0 or i == height - 1:
            print("-" *  width)
        else:
            print("|" + "" * (width -2) + "|")
rectangle(10, 3)