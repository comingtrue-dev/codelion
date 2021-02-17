foods = ["grape","orange","paech"]

#for x in foods:
#    print(x)

#information = {"a":"b","c":"d","e":"f"}

#for x,y in information.items():
#    print(x)
#    print(y)

foods.append("grape")
foods.extend(["banana","orange","apple"])
print(foods)
foods_set = set(foods)
foods_list = list(foods_set)
print(foods_set)
print(foods_list)
foods_set2 = set(foods_list)
# |,&,-
foodss = foods_set | foods_set2
print(foodss)
