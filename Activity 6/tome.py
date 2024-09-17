name = input("Enter your name: ")
age = input("Enter your age: ")
sport = input("Enter your sport: ")

# Use an f-string to format the output
print(f"Welcome, {name}! You are {age} years of age and  you love to play {sport}.")

item = "Samsung Tab S9"
count = 1

# Using the .format method
sentence = " I bought a {} {} today.".format(count, item)
print(sentence)

place = "Buenavista"
temperature = 21
#Using the % operator
print("The temperature in %s is %d degrees celsius." % (place, temperature))
