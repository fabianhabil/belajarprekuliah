panjang = 1
baris = int(input("berapa baris? "))
for i in range(0, baris):
    print(" " * (baris - (i+1)), "* " * panjang)
    panjang = panjang + 1