import requests
import re

# f = open("test3.html", "r")  # открыть файл на чтение
# data = f.read()
# f.close()
linkToHTMLFile = "https://stepic.org/media/attachments/lesson/24471/01"
#linkToHTMLFile = input()
response = requests.get(linkToHTMLFile)
if response.status_code == 200:
    data = response.text

result = []
for link in re.findall(r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)", data):
    domain = link[8]
    print(link)
    if domain not in result:
        result.append(domain)

result.sort()

for domain in result:
    print(domain)

# import re
# import requests
#
# resp = requests.get(input()).text
# sites = set()
# for site in re.findall(r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)', resp):
#     sites.add(site)
#
# for site in sorted(sites):
#     print(site)

# import requests, re
# for i in sorted({i.group(2) for i in re.finditer(
#     r'<a.*?href=[\'|"](\w+://)?(([\w|-]+\.)+\w+).*?>', requests.get(input('')).text)}):
#     print(i)

# import requests, re
# urls = set(re.findall(r"(?:.*)?(?:<a(?:.*)? href=[\"\'])(?:\w+://)?(\w[\w\.-]*)", requests.get(input()).text))
#
# print('\n'.join(sorted(urls)))