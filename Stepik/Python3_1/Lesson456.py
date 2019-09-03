import requests
import json

client_id = '18bb1959eb23b0ee1ecb'
client_secret = '395af8e2609049f6564b6cc4016f479a'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)  # разбираем ответ сервера
token = j["token"]  # достаем токен
headers = {"X-Xapp-Token": token}  # создаем заголовок, содержащий наш токен

f = open("dataset_24476_4.txt", "r")  # открыть файл на чтение
lst = []
for line in f:
    line = line.rstrip()
    template = 'https://api.artsy.net/api/artists/{}'
    r = requests.get(template.format(line), headers=headers)  # инициируем запрос с заголовком
    r.encoding = 'utf-8'
    # j = json.loads(r.text)  # разбираем ответ сервера
    lst.append(json.loads(r.text))
f.close()

sorted_lst = sorted(lst, key=lambda person: (int(person['birthday']), person['sortable_name']))
for item in sorted_lst:
    print(item['sortable_name'])
#
# res = []
# with open('dataset_24476_4.txt', 'r') as f, open('result.txt', 'w', encoding='utf-8') as w:
#     for i in f:
#         req_str = 'https://api.artsy.net/api/artists/' + i.rstrip()
#         j = requests.get(req_str, headers=headers).json()
#         res.append(j['birthday']+j['sortable_name'])
#     for i in sorted(res):
#         w.write(i[4:]+'\n')﻿