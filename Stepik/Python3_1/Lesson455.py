import sys, requests, json

template = 'http://numbersapi.com/{}/math?json=true'

with open('dataset_24476_3.txt', 'r') as f:
    for num in f:
        num = int(num.rstrip())
        res = requests.get(template.format(num))
        if res.status_code == 200:
            data = res.json()
            if data['found'] == True:
                print('Interesting')
            else:
                print('Boring')

import requests as re

# with open('dataset_24476_3.txt') as file:
#     for num in file:
#         response = re.get('http://numbersapi.com/{number}/math?json=true'.format( number=num.rstrip() )).json()﻿
#         ﻿
#         print('Interesting') if response['found'] else print('Boring')﻿

# import requests
#
# with open('dataset_24476_3.txt') as f:
#     for i in f:
#         res = requests.get('http://numbersapi.com/' + i.strip() + '/math?json=true')
#         print('Interesting' if res.json()['found'] else 'Boring')
#  Взял лучшее из двух нижележащих решений )