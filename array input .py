x = int(input("jumlah elemen? "))
array = [0 for i in range(x)]
for i in range(0, x):
    array[i] = int(input())
nyari = int(input("nyari? "))
i = 0
ketemu = False
while ((ketemu != True) or (i < x)):
    if array[i] == nyari:
        ketemu = True
        print("sama di elemen ke",i+1)
    i = i + 1
# for i in range(0, x):
#     if array[i] == nyari:
#         print("sama di elemen ke",i+1)
print(array)