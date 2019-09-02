import re
import random

file = open('inputText', 'r') #открываем файл с текстом для чтения
data = file.read().lower() #читаем строчки из файла и преобразуем к нижнему регистру
file.close() #закрываем файл


data = re.sub(r'[.,!?:;–]', '', data) #заменяем всю пунктуацию на пустой символ
data = re.sub(r'\n', ' ', data) #заменяем переносы строки на пробелы
data = re.sub(r' +', ' ', data).split(' ') #заменяем все множественные пробелы на одинарные и разбиваем строку по пробелам

dic = {}

for i in range(len(data)-1):
    if data[i] not in dic:
        dic.update({data[i]: [data[i + 1]]})
    else:
        dic.update({data[i]: dic.get(data[i]) + [data[i + 1]] })

for key in dic:
    for i in range(len(dic.get(key))):
        dic.update({key: dic.get(key) + [dic.get(key).count(dic.get(key)[i])] })
        #print(dic.get(key).count(dic.get(key)[i]))
firstWord = random.choice(list(dic.keys()))
strlen = 5
answer = ''

print(firstWord)

for i in range(strlen):
    answer += firstWord + ' '

    maxNum = max(dic.get(firstWord)[int(len(dic.get(firstWord))/2):])
    firstWordIndex = dic.get(firstWord).index(maxNum)-len(dic.get(firstWord))/2
    firstWord = dic.get(firstWord)[int(firstWordIndex)]


print(dic)
print(answer)
