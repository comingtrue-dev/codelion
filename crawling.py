import requests
from bs4 import BeautifulSoup
from datetime import datetime

#print(requests)

#print(requests.get)
url = "http://www.daum.net"
response = requests.get(url)

#print(type(response.text))

#print(type(BeautifulSoup(response.text,'html.parser')))

soup = BeautifulSoup(response.text,'html.parser')
rank = 1

results = soup.findAll('a','link_favorsch')

search_rank_file = open("rankresult.txt","w")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다."))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1

#file = open("daum.html","w")

#file.write(response.text)
#file.close()

#print(soup.title)

#print(soup.title.string)

#print(soup.span)

#print(soup.findAll('span'))

#print(response.url)

#print(response.content)

#print(response.encoding)

#print(response.headers)

#print(response.json)

#print(response.links)

#print(response.ok)

#print(response.status_code)
