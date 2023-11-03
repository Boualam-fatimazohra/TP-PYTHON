a=int(input("saisir un nombre"))
if a%2==0:
    print("le nombre est pair")
else:
    if a%2!=0 and  a%3==0 :
        print("le nombre est impair mais multiple par 3") 
    else:
        print("le nombre est impair mais n'est pas divisible par 3")