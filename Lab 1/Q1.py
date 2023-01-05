import math
Radius = float(input("Enter a radius: "))
Volume = 4 / 3 * math.pi * pow(Radius, 3)
print("Volume of sphere with a radius of {0}cm is {1:.2f}.".format(Radius, Volume))