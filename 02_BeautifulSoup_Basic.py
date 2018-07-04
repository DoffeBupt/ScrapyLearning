from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')

# 用beautifulsoup进行解析
# 这样子可以逐标签提取内容
soup = BeautifulSoup(html, features='lxml')
# printsouph1即把h1标签下的内容打出来
#print(soup.h1)
#print('\n', soup.p)

all_href = soup.find_all('a')
print('\n', all_href)
for l in all_href:
    print(l)
    print(type(l))
    # l为bs4标签类型，像下方这么写可以写出对应的值
    print(l['href'])

#all_href = [l['href'] for l in all_href]
#print('\n', all_href)