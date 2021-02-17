from googletrans import Translator

translator = Translator()

#sentence = "안녕하세요 코드라이언입니다."
sentence = input("언어를 감지할 문장을 입력해주세요 : ")

result = translator.translate(sentence,'en')
detected = translator.detect(sentence)

print("===========출 력 결 과===========")
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print("=================================")
