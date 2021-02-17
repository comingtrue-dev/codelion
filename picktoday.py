import random
import time
menu = ["된장찌개","피자","제육볶음"]
while True:
    print(menu)
    item = input("음식을 입력하세요 :")
    if item == "q":
        break
    else:
        menu.append(item)
print(random.choice(menu))
set_menu = set(menu)

while True:
    print(set_menu)
    item = input("음식을 삭제하세요 :")
    if item == "q":
        break
    else:
        set_menu = set_menu - set([item])

print(set_menu,"중에서 선택합니다.")
for x in reversed(range(1,6)):
    time.sleep(1)
    print(x)
result = list(set_menu)
print(random.choice(result))

#for x in range(3):
#    result = random.choice(menu)
#    print(result)

#while True:
#    result = random.choice(menu)
#    print(result)
#    time.sleep(1)
#    if result == "피자" :
#        break
