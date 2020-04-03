# -*- coding:utf-8 -*-

import re

import requests

html_text = requests.get("https://ip.cn/").text
# 正则匹配方式1

ip_text = re.search(u'<span class="cf-footer-item"><span>Your IP</span>: (.*?)</span>', html_text)

print(ip_text.group(1))

# 正则匹配方式2
ip_text = re.findall(u'<span class="cf-footer-item"><span>Your IP</span>: (.*?)</span>', html_text)
print(ip_text[0])
