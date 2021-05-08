g = 10
kecepatan = int(input("kecepatan? "))
t = 0
tmax = 2 * (kecepatan / g)

while(t<=tmax):
    jarak = (kecepatan * t) - (0.5 * g * (t**2))
    print("Jarak saat",t,"detik adalah",jarak,"meter")
    t = t + 1
