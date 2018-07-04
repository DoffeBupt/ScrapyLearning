from urllib.request import urlopen
# python自带的一个库，用来打开网页

# if has Chinese, apply decode()
# url打开网页链接
# read 表示读取内容
# decode表示解码，中文编码恢复为中文
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html")\
    .read().\
    decode('utf-8')
print(html)


import re
# re:正则表达式库
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])
# Page title is:  Scraping tutorial 1 | 莫烦Python


res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])
# Page paragraph is:
#     这是一个在 <a href="https://morvanzhou.github.io/">莫烦Python</a>
#     <a href="https://morvanzhou.github.io/tutorials/scraping">爬虫教程</a> 中的简单测试.


res = re.findall(r'href="(.*?)"', html)
# 仿佛出来了一大堆各种各样的数组？
# res：数组，res[0]第一个数组
print("\nAll links: ", res)
# All links:  ['https://morvanzhou.github.io/static/img/description/tab_icon.png', 'https://morvanzhou.github.io/', 'https://morvanzhou.github.io/tutorials/scraping']
