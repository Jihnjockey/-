import re

import bs4.element
import requests
from bs4 import BeautifulSoup

# 获取指定页面的内容
def get_page_content(url,keyword):
    response = requests.get(url)
    response.encoding=response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('h3' ) #,,,string=re.compile("大作文"),class_='entry_tit'
    enditm=soup.find_all('滕王阁序')#初始化
    for item in items:
        try:
            if item.contents[0]['class'][0]=='entry_tit':
                if re.search("大作文",item.string) and re.search("类词汇表达",item.string):   #搜索规则，同时包含两个字符串
                    print(item.string," "+item.contents[0]['href'])
                    enditm.append(item)
        except:
            pass


    return enditm

# 获取指定网站上所有条目的内容
def get_all_content(base_url, page_count,keyword):
    all_items = []
    for page in range(1, page_count + 1):
        if page>1:
            url = base_url +  str(page)+ '.html'
        else:
            url =base_url
        items = get_page_content(url,keyword)
        all_items.extend(items)
    return all_items

# 示例使用
if __name__ == '__main__':
    base_url = 'https://ielts.koolearn.com/xiezuo/'
    page_count = 50
    keyword=re.compile("大作文")
    all_items = get_all_content(base_url, page_count,keyword=keyword)
    # for item in all_items:
    #     print(item.text.strip())