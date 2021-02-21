import requests

url = 'https://www.naver.com'
res = requests.get(url)
print(res.status_code)