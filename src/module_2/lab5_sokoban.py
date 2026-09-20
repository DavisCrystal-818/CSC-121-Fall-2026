# Refer to this module's readme
def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "Undo":
            undone = history.pop()
            print(f"Undone: '{undone}'")
            print(history)
        elif action == "Restart":
            history.clear()
            print(history)
        else:
            history.append(action)
            print(history)
main()