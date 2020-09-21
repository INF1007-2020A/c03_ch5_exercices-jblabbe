#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    mon_nombre = float(input("Veuillez entrer un nombre: "))

    if mon_nombre < 0:
        mon_nombre = -mon_nombre
        
    return mon_nombre


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    noms = []
    for prefix in prefixes:
        noms.append(prefix + suffixes)
    
    return noms


def prime_integer_summation() -> int:
    return 0


def factorial(number: int) -> int:
    if number == 0:
        resultat = 1
    else:    
        index = abs(number)
        resultat = 1
        while index > 0:
            resultat *= index
            index -= 1
    return resultat


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
