import xml.etree.ElementTree as ET

tree = ET.fromstring(input())
ans = {"red": 0, "green": 0, "blue": 0}

def dfs(cube, res, depth):
    res[cube.attrib["color"]] += depth
    for i in cube.findall("cube"):
        dfs(i, res, depth + 1)

dfs(tree, ans, 1)
print(ans["red"], ans["green"], ans["blue"])

# from xml.etree import ElementTree
# colors = {"red": 0, "green": 0, "blue": 0}  # словарь ключ=цвет
# def finder(root, count=1):
#     colors[root.attrib["color"]] += count  # нашли цвет добавили к счётчику
#     [finder(child, count + 1) for child in root]  # поиск во вложениях
# finder(ElementTree.fromstring(input()))  # считываем xml-строку
# print(colors["red"], colors["green"], colors["blue"])  # выдаём ответ


values = {
    'blue': 0,
    'red': 0,
    'green': 0
}


# def func(tree, value=1):
#     values[tree.get('color')] += value
#
#     for element in tree:
#         func(element, value + 1)
#
#
# func(ElementTree.fromstring(input()))
#
# print(values['red'], values['green'], values['blue'])