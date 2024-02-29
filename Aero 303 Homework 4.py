# Aero 303 Homework 4
# Joel Surfleet

from SurfleetToolbox import *

shock = oblique(1.4)

shock.getBeta(15,2.8)

shock.M(2.8)

print("Mach 2.8 15*")
print("Mn",shock.Mn)
print("Mn2",shock.Normal.M2)
print("Pratio",shock.Normal.Pratio)
print("M2",shock.Normal.M2 / (sin(radians(shock.b - 15))))
print(" ")

shock = oblique(1.4)

shock.getBeta(30,2.8)

shock.M(2.8)

print("Mach 2.8 30*")
print("beta",shock.b)
print("Mn",shock.Mn)
print("Mn2",shock.Normal.M2)
print("Pratio",shock.Normal.Pratio)
print("M2",shock.Normal.M2 / (sin(radians(shock.b - 30))))
print(" ")

shock = oblique(1.4)

shock.getBeta(15,2)

shock.M(2)

print("1mach 2 15*")
print("Mn",shock.Mn)
print("Mn2",shock.Normal.M2)
print("Pratio",shock.Normal.Pratio)
print("M2",shock.Normal.M2 / (sin(radians(shock.b - 15))))
print(" ")

shock1 = oblique(1.4)

shock1.b = 25.5

shock1.M(3)

print(shock1.Mn)

print(shock1.Normal.M2)

m2 = shock1.Normal.M2 / (sin(radians(shock1.b - 8)))

print(m2)

shock2 = oblique(1.4)

shock2.b = 28.5

shock2.M(m2)

print(shock2.Mn)

print(shock2.Normal.M2)

M3 = shock2.Normal.M2 / (sin(radians(shock2.b - 8)))

print(M3)

shock3 = normal(1.4)

shock3.M(M3)

air = isentropic(1.4)

air.M(shock3.M2)

print(air.Pratio)
print(" ")

shock1 = oblique(1.4)

shock1.b = 40

shock1.M(3)

print(shock1.Mn)

print(shock1.Normal.M2)

m2 = shock1.Normal.M2 / (sin(radians(shock1.b - 8)))

print(m2)

shock2 = oblique(1.4)

shock2.b = 52

shock2.M(m2)

print(shock2.Mn)

print(shock2.Normal.M2)

M3 = shock2.Normal.M2 / (sin(radians(shock2.b - 8)))

print(M3)