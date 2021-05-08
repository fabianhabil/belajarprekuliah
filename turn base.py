pokemon1 = input("Nama Pokemon? ")
hp1 = float(input("Hp? "))
attack1 = float(input("Attack? "))

print("\n")

pokemon2 = input("Nama Pokemon? ")
hp2 = float(input("Hp? "))
attack2 = float(input("Attack? "))

ronde = 1
print("\n")

Mati = False
while (Mati == False):
    if (hp2 and hp1 >0):
        hp2 = hp2 - attack1
        print("Sekarang ronde",ronde)
        print(pokemon1,"menyerang",pokemon2,"dan",pokemon2,"menyisakan darah",hp2)
    if (hp1 and hp2 >0):
        hp1 = hp1 - attack2
        print(pokemon2,"menyerang",pokemon1,"dan",pokemon1,"menyisakan darah",hp1)
        ronde = ronde + 1
        # print("Sekarang ronde",ronde)
    if hp2<=0:
        print(pokemon1,"memenangkan battle dengan sisa hp",hp1)
        print("Game Over!")
        Mati = True
    if hp1<=0:
        print(pokemon2,"memenangkan battle dengan sisa hp",hp2)
        print("Game Over!")
        Mati = True

    # hp1 = hp1 - attack2
    # print(pokemon2,"menyerang",pokemon1,"dan",pokemon1,"menyisakan darah",hp1)

    # hp2 = hp2 - attack1
    # print(pokemon1,"menyerang",pokemon2,"dan",pokemon2,"menyisakan darah",hp2)