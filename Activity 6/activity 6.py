name = input("Enter your name: ")
age = input("Enter your age: ")
# Use an f-string to format the output
print(f"Hello, {name}! You are {age} years old.")


item = "apples"
count = 5
# Use the .format() method
sentence = "I bought {} {} today.".format(count, item)
print(sentence)


city = "New York"
temperature = 22
# Use the % operator
print("The temperature in %s is %d degrees Celsius." % (city, temperature))
