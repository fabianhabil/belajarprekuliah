number = -1
Range = int(input("how many layers do you want the tree?"))
for x in range(0,Range):
    number = number + 2
    print(" " * (Range - x), "+" * number)