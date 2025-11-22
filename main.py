import checker
import minigame
import gamestate

# MENU PRINCIPALE

while True:
    print("The Checker")
    print("--- MENU ---")
    print("1. Controlla password")
    print("2. Minigame")
    print("3. Exit")
    if gamestate.trophy_unlocked:
        print("🏆")

    print("Scegli: ")

    userChoice = input()

    match userChoice:
        case "1":
            checker.passChecker()
        case "2":
            minigame.minigameBegin()
        case "3":
            print("Arrivederci :)")
            break
        case _:
            print("Scelta non valida. Riprova.")
