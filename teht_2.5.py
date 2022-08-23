import math

leiviskä = float(input("Anna leviskät:"))
naula = float(input("Anna nauloja:"))
luoti = float(input("Anna Luotoja:"))

naula = leiviskä * 20
luoti = naula * 32
g =  luoti * 13.3
kg = g / 1000

loput = g-math.floor(kg) * 1000
print(f"Massa nykyarvoilla: {kg:0.2f} {loput:0.2f}")