#print("안녕하세요. \n만나서\t\t반갑습니다.")
#print("naver;kakao;sk;samsung")
#print("naver","kakao","sk","samsung",sep=';')
#print("first",end='');print("second")
#print(5/3)
#시가총액 = 2980000000000
#현재가 = 5000
#per = 15.79
#print(시가총액,type(시가총액))
#print(현재가,type(현재가))
#print(per, type(per))
#a= "132"; print(type(a))
#letters = 'python'; print(letters[0],letters[2])
#a = '24a 2210'; print(a[4:])
#c = 'ababab'; print(c[::-2])
#string = "python";print(string[::-1])
# a = '010-1111-2222';print(a[:3],a[4:8],a[9:]);print(a.replace("-"," "))
# a = 'http://sharebook.kr'; b = a.split('.'); print(type(b))
# a= "2020/03(E) (IFRS연결)"; print(a[0]), 'message')
# a = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']; a.remove("슈퍼맨");del a[1]; print(a)
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 +lang2; print(langs)
# a = [1, 2, 3, 4, 5, 6, 7]
# print("max : ",max(a),end = "");print("min : ",min(a));print(sum(a))

# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *a,b,c = scores; print(*a)
# _,_,*a=scores; print(a)
# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# del ice["메로나"]; print(ice)
# a= {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# a["폴라포"] = [500,40]
# b = list(a.keys());c = list(a.values());
# # print(b);print(c);print(d)
#
# for i in c:
#     a = 0
#     a += 1
#     print(c[a][0])
# print((4 != 3)and (3 != 3))

# user = int(input("숫자를 입력하세요: "))
# if user%2 == 0 :
#     print("짝수")
# else:
#     print("홀수")

# x = int(input(''))
# if x > 255 :
#     print(255)
# else:
#     print(10+x)

# a = input(''); b = input('')
# print("현재시각 : ",a,":",b)
# if b == "00":
#     print("정각입니다.")
# else:
#     print("정각이 아닙니다.")

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input('')
# if user in fruit.keys():
#     print("정답입니다.")
# else:
#     print( "오답입니다.")

# user = input("")
# if user.islower() is True :
#     print(user.upper())
# else :
#     print(user.lower())

# 환율 = {"달러": 1167,
#         "엔": 1.096,
#         "유로": 1268,
#         "위안": 171}
# user = input("입력: ")
# num, currency = user.split()
# print(float(num) * 환율[currency], "원")

# a = int(input(""))
# b = int(input(""))
# c = int(input(""))
# d = [a,b,c]
# print(max(d))

# dic = {"011":"skt","016":"kt","019":"lgu"}
# user = input("핸드폰 번호 : ")
# a = user.split()
# b = a[0]
# c = dic[b]
# print("당신은",c,"사용자입니다.")

# user = input("입력 : ")
# a,num = user.split("-")
# b = int(num[1:3])
# if b <9 :
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")

# my_list = ["가", "나", "다", "라","마"]
# for i in range(len(my_list)-1):
#     print(my_list[i],my_list[i+1])
#
# for a in range(len(my_list)-2):
#     print(my_list[a],my_list[a+1],my_list[a+2])
# for i in range(len(my_list)-1,0,-1):
    # print(my_list[i],my_list[i-1])

# a = [100, 200, 400, 800, 1000]
# b = [150, 300, 430, 880, 1000]
# d = []
# for i in range(len(b)):
#     d.append(b[i] - a[i])
# print(d)
# print(range(len(b)))

# apart = [ [101, 102], [201, 202], [301, 302] ]
# for col in apart:
#     for row in col:
#         print(row)

# for row in apart[::-1]:
#     for col in row:
#         print(col)

# for col in apart[::-1]:
#     for row in col[::-1]:
#         print(row)

# for row in apart:
#     print(row)
# for col in apart:
#     print(col)

# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for col in data:
#     sub = []
#     for row in col:
#         sub.append(row*1.00014)
#     result.append(sub)
# print(result)

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]

# for i in range(1,4):
#     print(ohlc[i][3])
# for row in ohlc[1:]:
#     print(row[3])
# for col in ohlc[1:]:
#     print(col[3])

# for row in ohlc[1:]:
#     if row[3] >150:
#         print(row[3])
# for row in ohlc[1:]:
#     if row[3] > row[0]:
#         print(row[3])
# volatility = []
# for row in ohlc[1:]:
#     volatility.append(abs(row[2]-row[1]))
# print(volatility)
# a = []
# for row in ohlc[1:]:
#     a.append(row[3]-row[0])
# print(sum(a))
#
# b = 0
# for row in ohlc[1:]:
#     b += (row[3]-row[0])
# print(b)

# def print_coin():
#     print("비트코인")
# print_coin()

# def print_with_smile(a):
#     print(a,":D")
# print_with_smile("hello")

# def print_upper_price(a):
#     print(a*1.3)
#
# def print_sum(a,b):
#     print(a+b)

# def print_max(a,b,c):
#     d = [a,b,c]
#     print(max(d))
# print_max(1,2,3)

# def print_reverse(a):
#     print(a[::-1])
# print_reverse("abcdefg")

# def print_score(d):
#     print(sum(d)/len(d))
# print_score([1,3,5,6])

# def print_even(a):
#     for i in a:
#         if i%2 == 0 :
#             print(i)
# print_even([2,5,1,2,5,6,7,46])

# def print_key(a):
#     for i in a.keys():
#         print(i)
#
# print_key({"이름":"김말똥", "나이":30, "성별":0})

# def make_list(a):
#     print(list(a))
# make_list("abdc")

def convert_int(a):
    return int(a.replace(',',''))
print(convert_int("1,2423,15235,123"))
