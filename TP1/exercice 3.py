distance=float(input("entrer la distance"))
temps=float(input("le temps:"))
if temps==0:
    temps=1
vitesse = distance/temps
print("vitesse=",vitesse)