# 导入requests模块
import requests
import urllib.request
# 导入re模块
import re
# 爬取地址
url='https://www.cnblogs.com/Mr-choa/p/12495157.html'
# 创建网页响应的对象
response=requests.get(url)
# 获取整个网页的内容
html_page=response.text
# 按照标签查找
title_pattern=r'(<a.*id="cb_post_title_url".*>)(.*)(</a>)'
# 按照标签，匹配相应的数据
title_match=re.search(title_pattern,html_page)
# 获取标题
title=title_match.group(2)
# 打印标题
print(title)
# 导入bs4库的BeautifulSoup
from bs4 import BeautifulSoup
# 创建对象，基于bs4库HTML的格式输出
soup=BeautifulSoup(html_page,'html.parser')
#取出soup中所有的进行prettify()方法处理的数据
print(soup.prettify())
# 取出soup中的a标签进行prettify()方法处理的数据
print(soup.a.prettify())
# 定义一个soup进行find（）方法处理的标签
div=soup.find(id="cnblogs_post_body")
# 取出博客文章内容
print(div.text)
# 创建文件名
filename=title+'.txt'
# 在文件内添加数据
with open(filename,'w',encoding='utf-8') as f:
    # 在文件中添加博客文章的标题
    f.write(title)
    # 在文件中添加博客文章的具体内容
    f.write(div.text)
print(type(title_pattern))

