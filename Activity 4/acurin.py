sampleText2 = "my name is {0}, i love {1} and playing {2}"
sampleText2a = sampleText2.format("shaina", "spaghetti", "badminton")
print(sampleText2a)

My name is shaina. I love spaghetti. and love playing badminton.


sampleText3 = "my name is {name}, i love {food}, i love playing {play}"
sampleText3a = sampleText.format(name="shaishai", food="pizza", play="mobile legends")
print(sampleText3a)

My name is shai. I love pizza. I love playing Mobile Legends.

item = "milk"
cost = 35.50
sampleText4 = ("the product %s is cost %.2f" % (item, cost))
print(sampleText4)

The product is milk the cost 35.50,

# item = "milk"
# cost = 35.5
# SampleText4 = "The product is %s the cost is %.5f." % (item, cost)
# print(SampleText4)

item = "apple watch"
cost = 9900
SampleText5 = f"The item is {item} and the cost is {cost * 100} pesos."
print(SampleText5)  # Output: The item is apple watch and the cost is

The item is apple watch and the cost is 990000 pesos.

# 9
strings = ["Animals", "Badger", "Honey Bee", "Honey Badger"]

for string in strings:
    lowercase_string = string.lower()
    print(lowercase_string)

animals
badger
honey bee
honey badger

# 10
strings = ["Animals", "Badger", "Honey Bee", "Honey Badger"]

for string in strings:
    uppercase_string = string.upper()
    print(uppercase_string)

ANIMALS
BADGER
HONEY BEE
HONEY BADGER

