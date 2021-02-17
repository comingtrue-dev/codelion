import requests
from bs4 import BeautifulSoup
url = "http://www.naver.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

results = soup.findAll('a','issue')
#print(results)
#file = open("naver.html","w")
#file.write(response.text)
#file.close()
for result in results :
    print(result.get_text(),"\n")
