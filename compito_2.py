# Crea un programma che chiede all'utente un numero intero e stampa se il numero è divisibile per 2, per 3 o per 5 (Hint: usare operatore %)

numero = int(input("Inserisci un numero intero: "))

if numero % 2 == 0:
    print(f"Il numero {numero} è divisibile per 2")
else:
    print(f"Il numero {numero} NON è divisibile per 2")
if numero % 3 == 0:
    print(f"Il numero {numero} è divisibile per 3")
else:
    print(f"Il numero {numero} NON è divisibile per 3")
if numero % 5 == 0:
    print(f"Il numero {numero} è divisibile per 5")
else:
    print(f"Il numero {numero} NON è divisibile per 5")
