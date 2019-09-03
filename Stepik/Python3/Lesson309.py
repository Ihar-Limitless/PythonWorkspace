import requests
lst = []
lst.append('')
r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
while True:
    lst[0] = r.text
    if(lst[0][:2]!='We'):
        str = 'https://stepic.org/media/attachments/course67/3.6.3/'+lst[0]
        r = requests.get(str)
    else:
        with open('text4.txt', 'w') as f:
             f.write(r.text)
        break
