from dataclasses import dataclass

@dataclass
class client:
	name: str
	company: str
	budget: int


@dataclass
class Programmer:
	name: str
	language: str
	framework: str


def runMatch(instance):
	match instance:
		case Programmer("Debjeet", language="Python",
						framework="Django"):
			print("He is Debjeet and he is a Python programmer and \nhe is using Django Framework for the backend of the project!")

		case Programmer("Rishabh", "C++"):
			print("He is Rishabh and is a C++ programmer and he is writing the inner code!")

		case client(name, company, budget):
			print(f"He is {name} and the  client for the project 'wordpress' and has the company named {company} which has a budget of {budget}")

		case Programmer(name, language, framework):
			print(f"He is programmer , his name is {name} , he works in {language} and uses {framework} for the current project!")

		case _:
			print("This person is not related to the recenet project works !")


if __name__ == "__main__":
	programmer1 = Programmer("Debjeet", "Python", "Django")
	programmer2 = Programmer("Rishabh", "C++", None)
	programmer3 = Programmer("Sankalp", "Javascript", "React")
	client1 = client("Vishal", "'The summer store'", 760000)
	runMatch(programmer1)
	runMatch(programmer2)
	runMatch(client1)
	runMatch(programmer3)
