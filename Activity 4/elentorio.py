sampleText2 = "My name is {0}, i love {1}, and playing {2}"
sampleText2a = sampleText2.format("belle", "pizza", "billiards")
print(sampleText2a)

sampleText3 = "My name is {newname} i love {newfood} and playimg {newgame}"
sampleText3a = sampleText3.format(newname="jean", newfood="burger", newgame="volleyball")
print(sampleText3a)

item = "milk"
cost = 36.50

sampleText4 = "The product %s costs %.2f" % (item, cost)
print(sampleText4)

My name is belle, i love pizza, and playing billiards
My name is jean i love burger and playimg volleyball
The product milk costs 36.50

item = "Apple watch"
    cost = 9900

    SampleText5 = f"The item is {item} and the cost is {cost * 100} pesos "
    print(SampleText5) # Output: The item is apple watch and the cost is
The item is Apple watch and the cost is 990000 pesos


strings = ["Animals", "Badger", "Honeybee", "Honey Badger"]

for string in strings:

    lowercase_string = string.lower()
    print(lowercase_string)


strings = ["Animals", "Badger", "Honeybee", "Honey Badger"]

for string in strings:
    uppercase_string = string.upper()
    print(uppercase_string)

animals
badger
honeybee
honey badger
ANIMALS
BADGER
HONEYBEE
HONEY BADGER


