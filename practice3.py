#a = 1
#result = 0
#while a < 1000 :
#    if a%3 == 0 :
#        result += a
#    a += 1
#print(result)


# 잘못된 예
#a = 1
#while a<6:
#    if 1:print("*")
#    elif 2:print("**")
#    elif 3:print("***")
#    elif 4:print("****")
#    else :print("*****")
#    a += 1

#a = 1
#while a < 6:
#    print("*" * a)
#    a += 1

#for i in range(1,101) :
#    print(i)


#k = 0
#mark = [70,60,55,75,95,90,80,80,85,100]
#for i in mark :
#    k += i
#print(k/len(mark))


num = [1,2,3,4,5]
result = [a*2 for a in num if a %2 == 1]
print (result)
