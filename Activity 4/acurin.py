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
