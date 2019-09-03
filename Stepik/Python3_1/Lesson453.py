import json

data = [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
children = dict()

# for cls in data:
#     for par in cls["parents"]:
#         if par not in children:
#             children[par] = []
#         children[par].append(cls["name"])
#
# def dfs(v, used):
#     size = 1
#     used.add(v)
#     if v not in children:
#         return size
#
#     for child in children[v]:
#         if child not in used:
#             size += dfs(child, used)
#
#     return size
#
# ans = []
#
# for cls in data:
#     ans.append((cls["name"], dfs(cls["name"], set())))
#
#
# for i in sorted(ans):
#     print(i[0], ":", i[1])

import json

d = dict() #словарь для хранения имен классов(ключ) и всех потомков(значение)
data_json = json.loads(input())  #обработка входных данных
data_json.sort(key= lambda x: x['name'])   #сортировка по имени
for q in data_json :  #идем по всем значениям 'name'
    d[q['name']] = []  #создание элементов словаря
    for i in data_json:  #проходим по всем значениям 'parents' полученных после обработки входных данных
        if q['name'] in i['parents']:
            d[q['name']].append(i['name'])   #если имя класса есть в родителях  , то добавляем имя класса в значение словаря
            cnt = 0 #итератор по уже добавленным элементам значения в словаре
            while cnt < len(d[q['name']]) :  #выполняем цикл, пока итератор меньше длины списка потомков (типа начало рекурсии =) )
                for c in data_json:
                    if d[q['name']][cnt] in c['parents'] :  #ну здесь то уж , я думаю, что всё понятно
                        d[q['name']].append(c['name'])
                cnt += 1
for c in d:
    d[c] = set(d[c]) #убираем повторяющихся потомков
    print(c, ':', len(d[c]) + 1)