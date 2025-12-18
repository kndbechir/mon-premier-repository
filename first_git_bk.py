import math

# Saisie des coefficients
a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

# Vérification que a ≠ 0
if a == 0:
    print("Ce n'est pas une équation du second degré.")
else:
    # Calcul du discriminant
    delta = b**2 - 4*a*c
    print(f"Discriminant Δ = {delta}")

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print("L'équation admet deux solutions réelles distinctes :")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

    elif delta == 0:
        x = -b / (2*a)
        print("L'équation admet une solution réelle double :")
        print(f"x = {x}")

    else:
        print("L'équation n'admet pas de solution réelle.")
5