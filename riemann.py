# import math

print("Integral Riemann")

b = float(input("integral batas atas? "))
a = float(input("integral batas bawah?" ))
n = float(input("hingga n? "))
i = 1
deltax = (b - a)/n
fungsi = 0

# fungsi = x^2
print("delta x=",deltax)

while(n >= i):
    xi = (a + (i * deltax))
    fungsi = (xi ** 2) * deltax + fungsi
    i = i + 1
print(fungsi)