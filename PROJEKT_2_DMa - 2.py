"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

autor: David Marek
email: david.32@seznam.cz
discord: David M.#7065
"""
import random


import re


def hra_bulls_and_cows():
    pocet_pokusu = 25
    separator = "-" * 48
    bulls_cows = [0, 0]

    print()

    print(hlavicka())
    cislo = generator_cisla()

    while pocet_pokusu > 0:
        tip = input(">>> ")

        if overeni_cisla(tip):
            # vysledek(cislo, tip, pocet_pokusu, separator)
            # pocet_pokusu -= 1

            bulls_cows = vyhodnoceni_cisla(cislo,tip)
            bulls_text = "bull" if bulls_cows[0] == 1 else "bulls"
            cows_text = "cow" if bulls_cows[1] == 1 else "cows"
            print(f"{bulls_cows[0]} {bulls_text}, {bulls_cows[1]} {cows_text}")
            pocet_pokusu -=1
            print(separator)        
        
        if vyhra(bulls_cows):
            break
    else:
        print(f"You ran out of tries. Number was {cislo}")

    print()

def hlavicka():
    """
    Popis:
    Tato funkce vytváří hlavičku pro hru "Bulls and Cows". Hlavička obsahuje několik textových řádků, které jsou spojeny pomocí oddělovače.

    Výsledek:
    Funkce vrací textovou hlavičku jako řetězec.

    """
    text1 = ("I've generated a random 4 digit number for you.")
    text2 = ("Let's play a bulls and cows game.")
    text3 = ("You have 25 attempts to do this")
    osloveni = ("Hi there!")
    zadani = ("Enter a number:")
    separator = "-" * len(text1)
    zahlavi = '\n'.join([osloveni, separator, text1, text2, text3, separator, zadani, separator])
    return zahlavi

def cislice(cislo) -> int:
    """
    Popis:
    Funkce cislice() je definována s parametrem cislo,
    to představuje číslo, které chcete převést na seznam číslic

    Příklad:
    str(cislo) = provede přeměnu čísla na řetězec
    [int(i) for i in str(cislo)] = výraz který iteruje jednotlivé znaky v řetězci
    a díky int() provede přeměnu na celé číslo

    Výsledek:
    return = vrátí seznam číslic

    """
    return [int(i) for i in str(cislo)]

def jedinecne_cislo(cislo) -> bool:
    """
    Popis:
    Tato funkce ověřuje, zda jsou všechny číslice daného čísla jedinečné, tzn. že neobsahuje žádné duplicity.

    Příklad:
    Předpokládejme číslo 'abcd'. Máme 4 jedinečné znaky: (a, b, c, d). 
    1) len(set(cislo_hra)) vrátí 4, což odpovídá počtu jedinečných znaků. 
    2) Předpokládejme číslo 'aabc', které má 3 jedinečné znaky (a, b, c) a 1 opakovaný znak (a). 
       len(set(cislo_hra)) vrátí 3, což znamená, že číslo nemá všechny číslice jedinečné.

    Výsledek:
    Vrací True, pokud jsou všechny číslice čísla jedinečné, jinak vrací False.

    """
    cislo_hra = cislice(cislo)
    if len(cislo_hra) == len(set(cislo_hra)):
        return True
    else:
        return False

def generator_cisla() -> int:
    """
    Popis:
    Tato funkce generuje náhodné čtyřmístné číslo v rozmezí od 1000 do 9999 včetně. 
    Používá funkci "jedinecne_cislo", aby zajistila, že číslo bude obsahovat pouze jedinečné číslice.

    Výsledek:
    Vrací vygenerované náhodné čtyřmístné číslo, které je uložené v proměnné "cislo".
    """
    while True:
        cislo = random.randint(1000,9999)
        if jedinecne_cislo(cislo):
            
            return cislo

def overeni_cisla(tip) -> bool:
    """
    Popis:
    Tato funkce ověřuje správnost zadaného čísla pro hru "Bulls and Cows". 
    Zkontroluje, zda číslo obsahuje pouze číselné znaky, nezačíná nulou, 
    neobsahuje duplicitní znaky a má přesně 4 číslice.

    Argumenty:
    tip (str): Zadané číslo od uživatele ve formátu řetězce.

    Výsledek:
    Pokud číslo splňuje všechny podmínky, vrátí funkce hodnotu True, 
    jinak vypíše odpovídající chybové zprávy a vrátí hodnotu False.

    """
    if len(tip) != 4:
        print("The number must have exactly 4 digits.")
        return False
    if not re.match("^\d{4}$", tip):
        print("The number must contain only digits.")
        return False
    if tip[0] == '0':
        print("The number must not start with a zero.")
        return False
    if len(set(tip)) != 4:
        print("The number must not contain duplicate digits.")
        return False


    return True

def vyhodnoceni_cisla(cislo,tip) -> None:
    """
    Popis:
    Tento kód iteruje přes číslice "cislo_hra" a "tip_hra" pomocí funkce "zip()"
    a porovnává je. Pokud je číslice "j" přítomna v "cislo_hra", zjišťuje se,
    zda se shoduje s číslicí "i". V případě shody se zvyšuje počet bulls,
    jinak se zvyšuje počet cows.
    Na konci funkce se vrátí seznam "bulls_cows",
    který obsahuje počty správně umístěných číslic (bulls)
    a číslic na správném místě (cows).

    """

    bulls_cows = [0,0]
    cislo_hra = cislice(cislo)
    tip_hra = cislice(tip)

    for i,j in zip(cislo_hra,tip_hra):

        if j in cislo_hra:

            if j == i:
                bulls_cows[0] += 1

            else:
                bulls_cows[1] += 1

    return bulls_cows

def vysledek(cislo,tip,pocet_pokusu,separator):
    """
    Popis:
    Tato funkce slouží k vypsání výsledku ohodnocení tipu uživatele (počet bulls a cows) 
    a snížení počtu zbývajících pokusů.

    Argumenty:
    cislo (int): Generované čtyřmístné číslo, které má uživatel uhodnout.
    tip (str): Uživatelem zadaný tip na uhodnutí čísla.
    pocet_pokusu (int): Počet zbývajících pokusů.
    separator (str): Oddělovací řetězec pro vizuální oddělení jednotlivých částí výstupu.

    Výsledek:
    Funkce vypíše počet bulls a cows v tipu uživatele a sníží počet zbývajících pokusů o 1.
    
    """
    bulls_cows = vyhodnoceni_cisla(cislo,tip)
    bulls_text = "bull" if bulls_cows[0] == 1 else "bulls"
    cows_text = "cow" if bulls_cows[1] == 1 else "cows"
    print(f"{bulls_cows[0]} {bulls_text}, {bulls_cows[1]} {cows_text}")
    pocet_pokusu -=1
    print(separator)

def vyhra(bulls_cows):
    """
    Popis:
    Tato funkce slouží k ověření, zda uživatel uhodl čtyřmístné číslo.

    Argumenty:
    bulls_cows (list): Seznam obsahující počet bulls (správně umístěných číslic) a počet cows (číslic na správném místě).

    Výsledek:
    Pokud je počet bulls roven 4, vypíše se zpráva "Correct, you've guessed the right number!"
    a funkce vrátí hodnotu True. V opačném případě vrátí hodnotu False.

    """
    if bulls_cows[0] == 4:
        print("Correct, you've guessed the right number!")
        return True
    
    return False

hra_bulls_and_cows()