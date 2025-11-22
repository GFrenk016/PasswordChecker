
# MINIGIOCO A LIVELLI 

import time
import gamestate

def minigameBegin():

    while True:
        print("\nMINIGAME PASSWORD A LIVELLI")
        print("Un minigioco interattivo a livelli, dove ogni livello richiede una password sempre più complessa per essere superato.")
        print("1. Inizia il minigame")
        print("2. Torna al menu principale")

        choice = input("Scegli: ")

        if choice == "1":
            level1()
        elif choice == "2":
            return   
        else:
            print("Scelta non valida!")
            continue


# ----------------- LIVELLO 1 -----------------

def level1():
    gamestate.currentLevel += 1
    errorCount = 0

    while True:
        print("\n— LIVELLO 1 —")
        print("A volte basta essere brevi e semplici… o forse no?")
        password = input("Inserisci la password (ESCI per uscire): ")

        if password == "ESCI":
            return 

        if len(password) < 8:
            print("Password troppo debole. Riprova.")
            errorCount += 1

            if errorCount == 3:
                print("Hint: Prova ad allungare!")

            continue  

        print("✔ Password valida! Livello superato!")
        time.sleep(2)
        level2()
        return


# ----------------- LIVELLO 2 -----------------

def level2():
    gamestate.currentLevel += 1
    errorCount = 0

    while True:
        print("\n— LIVELLO 2 —")
        print("Una password vale quanto la sua prima lettera.")
        password = input("Inserisci la password (ESCI per uscire): ")

        if password == "ESCI":
            return

        upperCount = sum(1 for c in password if c.isupper())

        if len(password) < 8 or upperCount < 3:
            print("Password debole. Riprova.")
            errorCount += 1

            if errorCount == 3:
                print("Hint: La forza sta nella ripetizione!")

            continue

        print("✔ Password valida! Livello superato!")
        time.sleep(2)
        level3()
        return


# ----------------- LIVELLO 3 -----------------

def level3():
    gamestate.currentLevel += 1
    errorCount = 0

    specialChars = "!@#$%^&*()"
    numbers = "0123456789"

    while True:
        print("\n— LIVELLO 3 —")
        print("Il potere è nei simboli che portiamo dentro.")
        password = input("Inserisci la password (ESCI per uscire): ")

        if password == "ESCI":
            return

        upperCount = sum(1 for c in password if c.isupper())
        hasSpecial = any(c in specialChars for c in password)
        hasNumber = any(c in numbers for c in password)

        if len(password) < 10 or upperCount < 3 or not hasSpecial or not hasNumber:
            print("Password debole! Riprova.")
            errorCount += 1

            if errorCount == 3:
                print("Hint: Non guardare solo i simboli!")

            continue

        print("🎉 Password valida! Hai vinto il minigame!")
        gamestate.trophy_unlocked = True
        time.sleep(2)
        return 
