# import urllib.request
#
# file = urllib.request.urlopen()
#
# output = open('text', 'wb')
# output.write(file.read())
# output.close()

# import urllib.request
# url = urllib.request.urlopen("https://stepik.org/explore")
# f = url.read()
# open("file2","wb").write(f)

import requests #импортируем модуль
send=requests.post("https://stepik.org/explore") #делаем запрос
file = open('text3','w') #создаем файл для записи результатов
file.write(send.text) #записываем результат
file.close() #закрываем файл


# import requests
# url = 'https://stepik.org/explore'
# res = requests.get(url)
#
# with open("text.html", "w") as f:
#     for i in res.text.splitlines():
#         print(i, file=f)