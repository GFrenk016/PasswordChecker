# CHECKER DELLA PASSWORD 

def passChecker():
    while True:
        password = input("\nInserisci la password da controllare: ")
        print("Hai inserito:", password)

        if len(password) < 8:
            print("Password debole: troppo corta.")
        else:
            print("Password forte. Sei al sicuro!")

        print("\nScegli:")
        print("1. Riprova con un'altra password")
        print("2. Torna al menu principale")

        choice = input("Scegli: ")

        if choice == "1":
            continue     
        elif choice == "2":
            return       
        else:
            print("Scelta non valida, torno al menu principale.")
            return
