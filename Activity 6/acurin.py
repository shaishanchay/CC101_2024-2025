name = input("Enter your name: ")
age = input("Enter your age: ")
# Use an f-string to format the output
print(f"Hello, {name}! You are {age} years old.")

item = "banana"
count = 7
# use the .format() method
sentence = "I bought {} {} today.".format(count, item)
print(sentence)

city = "Paris"
temperature = 24
# Use the % operator
print("The temperature in %s is %d degrees Celsius." % (city, temperature))

Enter your name: shaina
Enter your age: 18
Hello, shaina! You are 18 years old.
I bought 7 banana today.
The temperature in Paris is 24 degrees Celsius.

Process finished with exit code 0
