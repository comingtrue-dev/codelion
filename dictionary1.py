information = {"고향":"무안","취미":"영화감상","외모":"잘생김","취미":"피아노연주","3대":"330"}
food = ["국수","피자","제육볶음"]

print(information.get("3대"))
information["스내치"] = "잘 함"
information["클린"] = "잘 못함"
del information["고향"]
print(information)
print(len(information))
information.clear()
print(information)
print(food[2])
food.append("청국장")
food.remove("국수")
del food[0]
print(food)
