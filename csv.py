#!/usr/bin/env python3
import os

def Tallenna(tiedostonimi):
    f = open(tiedostonimi, "w")
    f.write("Nimi;Ikä;Ammatti;\n")
    f.write(Nimi + ";" + Ikä + ";" + Ammatti + ";")
    f.close()
    print("Tallennettu onnistuneesti!")


Nimi = input("Nimi: ")
Ikä = input("Ikä: ")
Ammatti = input("Ammatti: ")
tallennetaanko = input("Tallennetaan? y/n: ")
if tallennetaanko == "y":
    tiedostonimi = input("Tiedostonimi: ") + ".csv"
    Tallenna(tiedostonimi)
else:
    print("Selvä ja näkemiin!")
