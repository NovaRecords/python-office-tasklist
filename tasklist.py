tasklist = []

# Funktion zum Hinzufügen einer Aufgabe
def add_task():
    task = input("\nBitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll:\n")
    if task:
        task_number = len(tasklist) + 1
        tasklist.append(f"{task_number}. {task}")
        print("\nDie Aufgabe wurde zur Liste hinzugefügt.")

# Funktion zum Entfernen einer Aufgabe
def remove_task():
    if not tasklist:
        print("\n********** Die Aufgabenliste ist leer. **********")
    else:
        print("\nWelche Aufgabe möchtest du entfernen?")
        for task_number, task in enumerate(tasklist, 1):
            print(task)
        try:
            choice = int(input("\nBitte gib die Nummer der Aufgabe ein, die du entfernen möchtest: "))
            if 1 <= choice <= len(tasklist):
                removed_task = tasklist.pop(choice - 1)
                print(f"Aufgabe '{removed_task}' wurde gelöscht.")
            else:
                print("\nUngültige Auswahl.")
        except ValueError:
            print("\nBitte gib eine gültige Zahl ein.")

# Funktion zum Anzeigen der Aufgabenliste
def show_tasklist():
    if tasklist:
        print("\n********** Deine Aufgabenliste **********")
        for task in tasklist:
            print(task)
    else:
        print("\n********** Deine Aufgabenliste ist leer **********")

# Hauptfunktion
def main():
    while True:
        print("\n********** Aufgabenliste **********")
        print("1. Aufgabe zur Aufgabenliste hinzufügen")
        print("2. Aufgabenliste anzeigen")
        print("3. Aufgabe löschen")
        print("4. Programm beenden")
        choice = input("\nBitte treffen Sie Ihre Auswahl: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasklist()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("\nProgramm wird beendet! Bis später!\n")
            break
        else:
            print("\nBitte wähle zwischen 1, 2, 3 oder 4.")