# -*- coding:utf-8 -*-
import requests, ssl, logging

requests.packages.urllib3.disable_warnings()
logging.captureWarnings(True)
ssl._create_default_https_context = ssl._create_unverified_context()
import urllib3.contrib.pyopenssl

urllib3.contrib.pyopenssl.inject_into_urllib3()
# import re
#
# import requests
#
# html_text = requests.get("https://2020.ip138.com/").text
# # 正则匹配方式1
#
# ip_text = re.search(u'<span class="cf-footer-item"><span>Your IP</span>: (.*?)</span>', html_text)
#
# print(ip_text.group(1))
#
# # 正则匹配方式2
# ip_text = re.findall(u'<span class="cf-footer-item"><span>Your IP</span>: (.*?)</span>', html_text)
# print(ip_text[0])
url = "https://2020.ip138.com/"
proxy = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.8080'}
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
# requests.adapters.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False
res = requests.get(url, headers=headers, verify=False, proxies=proxy, timeout=3)
print(res.content.decode())
