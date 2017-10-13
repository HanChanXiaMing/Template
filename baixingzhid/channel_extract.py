from bs4 import BeautifulSoup
import requests

# 主页所有分类的链接
start_url = 'http://zhidao.baixing.com/'
url_host = 'http://zhidao.baixing.com'  # 网页头部分

def get_channel_urls(url):
    wb_data = requests.get(start_url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('ul.sub-menu > li > a')
    #print(links)
    #http://zhidao.baixing.com/cat85.html
    #http://zhidao.baixing.com/cat86.html

    for link in links:
        page_url = url_host + link.get('href')
        print(page_url)

#get_channel_urls(start_url)
# 把 cat替换成 paga-
# 部分链接
channel_list = '''
http://zhidao.baixing.com/paga-23.html
http://zhidao.baixing.com/paga-24.html
'''
