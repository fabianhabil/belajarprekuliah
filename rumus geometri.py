print("rumus geometri \n")

print("Bidang datar: \n 1. Persegi \n 2. Segitiga\n 3. Persegi Panjang")

geometri = input("Bidang datar apa? ")


if (geometri == "1"):
    sisip = float(input("sisi persegi "))
    sisip = sisip ** 2
    print("luasnya adalah",sisip)
elif (geometri == "2"):
    alas = float(input("alas segitiga? "))
    tinggi = float(input("tinggi segitiga? "))
    luassegitiga = 0.5 * alas * tinggi
    print("luasnya adalah",luassegitiga)
elif (geometri == "3"):
    panjang1 = float(input("Panjang? "))
    lebar1 = float(input("Lebar? "))
    luaspersegipanjang = panjang1 * lebar1
    print("luasnya adalah",luaspersegipanjang)

else:
    print("salah!")