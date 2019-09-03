import sys
import requests
url = sys.argv[1]
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print("Ошибка Timeout, url: ", url)
except requests.HTTPError as err:
    code = err.response.status_code
    print("Ошибка: URL {0}, code: {1}".format(url, code))
except requests.RequestException:
    print("Ошибка скачивания url: ", url)
else:
    print(response.content)
