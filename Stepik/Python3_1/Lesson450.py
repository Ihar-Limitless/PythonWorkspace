import re, requests
url1 = r"https://stepic.org/media/attachments/lesson/24472/sample0.html"
url2 = requests.get(url1)
print(url2.status_code)
print(url2.headers['Content-Type'])
print(url2.text)
print(re.findall(r'https://.*html', url2.text))