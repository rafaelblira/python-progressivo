import random

def par(x):
    if (x%2)==0:
        return True
    else:
        return False

while True:
    num = random.randint(1, 10000)
    if par(num):
        print("É par")
    else:
        print("É ímpar")