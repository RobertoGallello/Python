# Crea un programma che chiede all'utente il suo nome e lo stampa sempre con l'iniziale minuscola

nome = input("Inserisci il tuo nome: ")
nome_minuscolo = nome[0].lower() + nome[1:]
print(nome_minuscolo)
