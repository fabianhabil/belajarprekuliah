print("Calculator bianha v.0.1")

num1 = input("Angka berapa? ")
if (num1.isalpha()):
    print("salah!")
    num1 = input("Angka berapa? ")
num2 = input("Angka berapa? ")
operation = input("Operasi hitung? (pakai simbol) ")

if (num2.isalpha()):
    print("salah!")
elif operation=="+":
    print(float(num1) + float(num2))
elif operation=="-":
    print(float(num1) - float(num2))
elif operation=="/":
    print(float(num1) / float(num2))
elif operation=="*":
    print(float(num1) * float(num2)) 

# print(type(num1))
# print(type(num2))