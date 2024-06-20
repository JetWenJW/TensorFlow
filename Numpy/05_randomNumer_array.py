from numpy.random import *
print(rand())
print(rand(5))
print(rand(3, 2))
print("-" * 40)

print(randint(100))
print(randint(10, 20))
print(randint(10, 20, 5))
print(randint(10, 20, (2, 3)))
print("-" * 40)

players = ["Curry", "Harden", "Lebron", "Durant", "McGee"]
print(choice(players))
print(choice(players, 3))
print("-" * 40)
print(choice(players, 3, replace = False))














