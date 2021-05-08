import math

print("gerak vertikal ")
v0 = float(input("Kecepatan? "))
sudut = math.radians(float(input("sudut? ")))
g = 10
tmax = 2 * v0 * math.sin(sudut) / g
t = 0

# print(math.sin(sudut))
print(math.sin(sudut))
print("waktu maksimal adalah",tmax,"detik")
while (tmax >= t):
    fungsi = (v0 * t * math.sin(sudut)) - 0.5 * g * (t ** 2)
    print("jarak saat",t,"detik adalah",fungsi,"meter")
    t = t + 0.1