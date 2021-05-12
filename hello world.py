print('Palindrome checker! versi gabut buat git')
angka = input("angka? ")
if (angka[::] == angka[::-1]):
    print("palindrome!")
else:
    print("bukan palindrome")