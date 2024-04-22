def runMatch(user):
    user = str(input("Write your username -: "))

    # match statement starts here.
    match user:
        case "Sayani" | "Snigdha":
            print("sdffedfeyou don't have any access, for any requirment please contact a verified employee")
        case "Debjeet" | "Mitali":
            print("Debjeet do not have access to the database but only for the api code.")
        case "Rishabh" | "rishabh":
            print("Rishabh have the access to the database")
        case _:
            print("You do not have any access to the code")

if __name__ == "__main__":
    for _ in range(3):
        runMatch(user)
