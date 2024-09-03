sampleText2 = "My name is {0}. I love {1}. and love playing {2}."
sampleText2a = sampleText2.format("shaina", "spaghetti", "badminton")
print(sampleText2a)

My name is shaina. I love spaghetti. and love playing badminton.

sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(name="shai", food="pizza", play="Mobile Legends")
print(sampleText3a)

My name is shai. I love pizza. I love playing Mobile Legends.

item = "milk"
cost = 35.50

sampleText4 = "The product is %s the cost %.2f," % (item, cost)
print(sampleText4)

The product is milk the cost 35.50
