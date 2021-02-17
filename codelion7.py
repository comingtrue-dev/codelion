#dictionary
menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육": 9000}
menu["냉면"] = 6000
menu["라조기"] = 12000
menu["탕수육"] = 8500
del menu["짜장"]
print(menu)

print(menu["짬뽕"],menu["라조기"],menu["탕수육"])
