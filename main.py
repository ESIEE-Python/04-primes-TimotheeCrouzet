import math

#### Fonction secondaire
def isprime(p):
    """cherche si un nombre est premier
    Args: 
        p : entier relatifs
    Returns:
        True or False
    >>> isprime(7)
    True
    >>> isprime(4)
    False
    >>> isprime(-3)
    False
    """
    if p <= 1:
        return False
    if p == 2:
        return True
    x = int(math.sqrt(p))  # Calcul de la racine carrée de p
    for i in range(2, x + 1):
        if p % i == 0:
            return False
    return True
   
print(isprime(5))



#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
