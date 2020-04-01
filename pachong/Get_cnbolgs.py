"""简单获取一篇博客文章的标题和内容
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
"""

import urllib.request
import re
from bs4 import BeautifulSoup
#该作者的博文一共有多少页
pageNo=18
#后面需要添加页码
url='https://www.cnblogs.com/Mr-choa/default.html?page='
# 获取网页源码
def get_html(url):
    """
    返回对应url的网页源码，经过解码的内容
    :param url:
    :return:
    """
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    html_page = resp.read().decode('utf-8')
    return html_page
# 获取博客文章的标题
def get_title(url):
    '''
    获取对应url下文章的标题
    :param url:
    :return:
    '''
    html_page = get_html(url)
    title_pattern = r'(<a.*id="cb_post_title_url".*>)(.*)(</a>)'
    title_match = re.search(title_pattern, html_page)
    title = title_match.group(2)
    return title
# 获取博客文章的文本
def get_Body(url):
    """
    获取对应url的文章的正文内容
    :param url:
    :return:
    """
    html_page = get_html(url)
    soup = BeautifulSoup(html_page, 'html.parser')
    div = soup.find(id="cnblogs_post_body")
    return div.text
# 保存文章
def save_file(url):
    """
    根据url，将文章保存到本地
    :param url:
    :return:
    """
    title=get_title(url)
    body=get_Body(url)
    filename="Mr_choa"+'-'+title+'.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(title)
        f.write(url)
        f.write(body)
# 遍历所有的博客文章链接，保存博客的文章
def save_files(url,pageNo):
    '''
    根据url和pageNo，保存博主所有的文章
    :param url:
    :param pageNo:
    :return:
    '''
    totol_urls=get_Urls(url,pageNo)
    for url_ in totol_urls:
        save_file(url_)
# 获取所有的链接
def get_Urls(url,pageNo):
    """
    根据url，pageNo，能够返回该博主所有的文章url列表
    :param url:
    :param pageNo:
    :return:
    """
    total_urls=[]
    for i in range(1,pageNo+1):
        url_1=url+str(i)
        html=get_html(url_1)
        title_pattern=r'<a.*class="postTitle2".*href="(.*)">'
        urls=re.findall(title_pattern,html)
        for url_ in urls:
            total_urls.append(url_)
    #print(total_urls.__len__())
    return total_urls
save_files(url,pageNo)
