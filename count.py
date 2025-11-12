with open("file.txt", "r") as file:
    testo = file.read()
    
    # Conta quante virgole ci sono
    numero_virgole = testo.count(",")
    print(f"Ci sono {numero_virgole} virgole")
