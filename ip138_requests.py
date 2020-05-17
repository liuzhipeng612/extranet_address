import requests

proxy = '127.0.0.1:8080'  # 本地代理
# proxy='username:password@123.58.10.36:8080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}
headers = {
    "Host": "2020.ip138.com",
    "Connection": "close",
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36 Edg/80.0.361.109",
    "Sec-Fetch-Dest": "document",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}
try:
    response = requests.get('https://2020.ip138.com/', headers=headers, proxies=proxies, verify=False, )
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('错误:', e.args)
