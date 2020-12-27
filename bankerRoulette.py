import random
# a programm that picks a name of a person from a list who will then pay the bill

persons = input("Enter the name of people from you wanna choose one\n")
list_persons = persons.split(", ")

random_index = random.randint(0, len(list_persons) -1)

print("{} is going to pay the meal today".format(list_persons[random_index]))


