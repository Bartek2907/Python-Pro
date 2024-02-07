import random
symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
haslo = ""
length = int(input('podaj długość'))
for i in range(length):
    haslo += random.choice(symbol)

print(haslo)
