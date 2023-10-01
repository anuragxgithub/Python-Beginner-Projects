# Mad libs generator is a fun game that is usually played by kids.

# In this python game user has to enter substitutes for blanks in the story without knowing the
# story. It will be fun to read aloud the stories after filling the blanks.

#We will use fstring here.

adj = input("Adjective: ")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me excited all the time becasue \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)