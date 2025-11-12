# Crea un programma in python che chiede all'utente una frase e stampi la stringa un carattere si e uno no (Caratteri alternati)

frase = input("Inserisci una frase: ")
frase_alternata = frase[::2] 
print(frase_alternata)

# [inizio:fine:passo] --> lo slicing = 
# inizio: se omesso parte dall'inizio (frase[0]), 
# fine: se omessa va fino alla fine (frase[-1]), 
# passo: ogni quanti caratteri prende, se omesso = 1 prende tutti i caratteri