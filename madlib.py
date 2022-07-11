# 12 Beginner Python Projects - FreeCodeCamp
# Madlibs

# String concatenation (putting strings together)
# Suppose we want to create a string that says "Merry Christmas, _____"
# person = "John" # some string variable

# ways to do this
# print("Merry Christmas, " + person)
# print("Merry Christmas, {}".format(person))
# print(f"Merry Christmas, {person}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

name = input("Random name: ")
planet = input("Planet: ")
adj = input("Adjective: ")
age = input("Your age: ")
verb = input("Verb: ")

madlib2 = f"Hello, my name is {name}, I'm a robot from planet {planet}. Nice to meet you! You seem so {adj}.\
My readings indicate you are {age} years old. I hope we can {verb} together!"

print(madlib2)