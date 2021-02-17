myGrade = int(input("학번을 입력하세요"))
yourGrade = int(input("학번을 입력하세요"))

print(myGrade != yourGrade)
print(myGrade == yourGrade)
print(myGrade >= yourGrade)

if myGrade == yourGrade :
    print("앗 동기네요")
    print("반갑습니다")
else :
    print("누구세요?")

if myGrade == yourGrade :
    print("안녕 반가워")
elif myGrade > yourGrade :
    print("안녕 후배야")
elif myGrade < yourGrade :
    print("안녕 선배야")
else :
    print("누구세요?")
