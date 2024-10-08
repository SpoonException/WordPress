#!/usr/bin/env python
# encoding: utf-8

import requests

# 发送请求到 WordPress API
url = "https://anspoon.com/wp-json/wp/v2/posts"
params = {
    "per_page": 100,  # 每次请求返回 100 篇文章
    "page": 1         # 起始页
}

posts = []
while True:
    response = requests.get(url, params=params)

    # 如果没有更多文章，停止请求
    if response.status_code != 200 or not response.json():
        break

    posts.extend(response.json())
    params["page"] += 1  # 下一页

# 打开或创建 README.md 文件
with open('README.md', 'w') as f:
    f.write('# WordPress 文章链接\n\n')

    # 写入每个文章的标题和链接
    for post in posts:
        title = post["title"]["rendered"]
        link = post["link"]
        f.write(f'- [{title}]({link})\n')

