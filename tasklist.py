tasklist = []

# Wir machen hier eine add_task function
def add_task():
    task = input("\nBitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: ")
    print("\nDie Aufgabe wurde zu der Liste hinzugefügt.")
    if task:
        tasklist.append(task)

# An dieser Stelle bauen wir den show_tasklist
def show_tasklist():
    if tasklist:
        print("\n********** Deine Aufgabenliste **********")
        for task in tasklist:
                print(task)
    else:
        print("\n********** Deine Aufgabensliste ist leer **********")

        