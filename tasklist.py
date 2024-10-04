tasklist = []

# Wir machen hier eine add_task function
def add_task():
    task = input("\nBitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: ")
    print("\nDie Aufgabe wurde zu der Liste hinzugefügt.")
    if task:
        tasklist.append(task)

add_task()

