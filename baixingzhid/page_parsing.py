from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017) # 激活
# 创建库
cheshi = client['cheshi']
url_list = cheshi['url_list3']
item_info = cheshi['item_info4']

url_host = 'http://zhidao.baixing.com'

# spider 1
# 获取各类里的所有链接
# http://zhidao.baixing.com/page-23-1.html
#   http://zhidao.baixing/page-85-1
def get_links_from(channel,pages):  # channel 是类的html   pages 是当前类的页数
    # http://zhidao.baixing.com/page-23-1.html   内科第2页
    list_view = '{}-{}.html'.format(channel,str(pages))
    wb_data = requests.get(list_view)
    time.sleep(3)   # 延迟时间
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('footer','dwqa-footer-meta'):    # 判断当前页有无信息
        for link in soup.select('a.dwqa-title'):
            url = url_host + link.get('href')
            url_list.insert_one({'url':url})
            print(url)
    else:
        pass
        # Nothing !

# spider 2
# 获取各页里的信息
def get_item_info(url):
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        titles = soup.title.text                                                            # 标题
        datas = soup.select('div.dwqa-question > header > div > span.dwqa-date')[0].text    # 提问时间
        #Answer_times = soup.select('header div span.dwqa-date a')  # 未被采用回答时间
        if soup.find('div','acceptAnswer'):                     # 回答是否被采用
            best_times = soup.select('div.acceptAnswer div span:nth-of-type(2)')[0].text    # 采用回答时间
        else:
            best_times = None
        print(titles,datas,best_times)

        item_info.insert_one({'titele':titles,'datas':datas,'best_time':best_times})


#get_links_from('http://zhidao.baixing.com/page-23',1)
#get_item_info('http://zhidao.baixing.com/question/297863.html')
