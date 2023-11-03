for i in range(1,2) :
    nom=input(f"saisi le nom de l'article {i}:")
    qt=int(input(f"saisi la quentitée d'article{i}"))
    prix=int(input(f"saisi le prix d'article{i}"))
    print(f"le totale de l'article {i}",prix*qt)
    
print(f"le totale de facture",(prix*qt)+((prix*qt)*0.2))
