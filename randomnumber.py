import random
#randomNumber = random.sample(range(1,46),6)
#print(randomNumber)


a = int(input("몇개 살거야?"))


for x in range(a):
    b = random.sample(range(1,46),6)
    b.sort()
    print(b)
