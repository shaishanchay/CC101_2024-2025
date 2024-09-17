name = input("Enter your name: ")
age = input("Enter your age: ")
# Use an f-string to format the output
print(f"Hello, {name}! You are {age} years old.")

item = "grapes"
count = 10
# use the .format() method
sentence = "I bought {} {} today.".format(count, item)
print(sentence)

city = "Japan"
temperature = 16
# Use the % operator
print("The temperature in %s is %d degrees Celsius." % (city, temperature))

Enter your name: milva
Enter your age: 18
Hello, Milva! You are 18 years old.
I bought 10 grapes today.
The temperature in Japan is 16 degrees Celsius.

Process finished with exit code 0
