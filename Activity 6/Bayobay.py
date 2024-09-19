name = input("Enter your name: ")
age = input("Enter your age: ")
# Use f-string to format the output
print(f"Hello, {name} You are {age} years old. ")

item = "banana"
count = 7
# Use the .format() method
sentence = "I bought {} {} today. " .format(count, item)
print(sentence)

city = "Paris"
temperature = 24
# Use the % operator
print("The temperature in %s is %d degrees celcius." %(city, temperature))


Enter your name: ashly
Enter your age: 18
Hello, ashly You are 18 years old. 
I bought 7 banana today. 
The temperature in Paris is 24 degrees celcius.
