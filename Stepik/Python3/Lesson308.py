import requests
lst=[]
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/314.txt')
with open('text4.txt', 'w') as f:
    f.write(r.text)
with open('text4.txt', 'r') as f:
    for line in f.readlines():
        lst.append(line.splitlines())
print(len(lst))
