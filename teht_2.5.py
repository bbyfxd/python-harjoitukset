import math

leiviskä = float(input("Anna leviskät:"))
naula = float(input("Anna nauloja:"))
luoti = float(input("Anna Luotoja:"))

vastaus1 = (leiviskä * 20) * 32 * 13.3
vastaus2 = (naula * 32) * 13.3
vastaus3 = luoti * 13.3
Gramma = vastaus3 + vastaus2 + vastaus1
KG = int(Gramma / 1000)

left_overs = math.floor(Gramma % 1000)

print(f"{KG} Kilo ja {left_overs} Gramma")
