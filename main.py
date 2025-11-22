import checker

# MENU PRINCIPALE

while True:
    print("The Checker")
    print("--- MENU ---")
    print("1. Controlla password")
    print("2. Exit")

    print("Scegli: ")

    userChoice = input()

    match userChoice:
        case "1":
            checker.passChecker()
        case "2":
            print("Arrivederci :)")
            break
        case _:
            print("Scelta non valida. Riprova.")
