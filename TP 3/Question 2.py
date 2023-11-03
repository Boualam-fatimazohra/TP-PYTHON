import math
def equation2deg():
    def delta(a,b,c):
        delta=b*b-4*a*c
    def NombreRacine(a,b,c):
        dlt=delta(a,b,c)
        if dlt==0:
            return 1
        elif dlt>0:
            return 2
        else:
            return 0
    def AfficheNombreRacine(a,b,c):
        nbrS=NombreRacine(a,b,c)
        print("il y a"+nbrS+"solution")
    def Racine1(a,b,c):
        x1=delta(a,b,c)
        return (-b+math.sqrt(x1))/2*a
    def Racine2(a,b,c):
        x2=delta(a,b,c)
        return (-b+math.sqrt(x2))/2*a




