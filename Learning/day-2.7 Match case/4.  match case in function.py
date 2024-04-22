def provideAccess(user):
	return {
		"username": user,
		"password": "admin"
	}


def runMatch():
	user = str(input("Write your username -: "))

	# match statement starts here .
	match user:
		case "Debjeet":
			print("Debjeet do not have access to the database but only for the api code.")
		case "Mitali":
			print(
				"Mitali do not have access to the database but only for the frontend code.")

		case "Rishabh":
			print("Rishabh have the access to the database")
			print(provideAccess("Rishabh"))

		case _:
			print("You do not have any access to the code")


if __name__ == "__main__":
	for _ in range(3):    # this is used to loop the match case 3 times
		runMatch()
