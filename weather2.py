import requests
import json

city = "Tokyo"
apikey = "83a0fbb409e6aa12fbd7d2310dcd0fa6"
lang = "kr"
units = "metric"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={units}"

result = requests.get(api)
#print(result.text)

data = json.loads(result.text)
#print(type(data))

print(data["name"],"의 날씨입니다.")
print("날씨는",data["weather"][0]["description"],"입니다.")
print("현재 온도는",data["main"]["temp"],"입니다. 하지만 체감온도는",data["main"]["feels_like"],"이고, 최저 기온과 최고 기온은",data["main"]["temp_min"],"과",data["main"]["temp_max"],"입니다.")
print("현재 기압은",data["main"]["pressure"],"이고 습도는",data["main"]["humidity"],"% 입니다.")
