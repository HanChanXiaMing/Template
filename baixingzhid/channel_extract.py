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
channel_list = '''
http://zhidao.baixing.com/paga-85.html
http://zhidao.baixing.com/paga-86.html
http://zhidao.baixing.com/paga-87.html
http://zhidao.baixing.com/paga-88.html
http://zhidao.baixing.com/paga-89.html
http://zhidao.baixing.com/paga-90.html
http://zhidao.baixing.com/paga-91.html
http://zhidao.baixing.com/paga-92.html
http://zhidao.baixing.com/paga-93.html
http://zhidao.baixing.com/paga-94.html
http://zhidao.baixing.com/paga-95.html
http://zhidao.baixing.com/paga-96.html
http://zhidao.baixing.com/paga-97.html
http://zhidao.baixing.com/paga-98.html
http://zhidao.baixing.com/paga-99.html
http://zhidao.baixing.com/paga-23.html
http://zhidao.baixing.com/paga-24.html
http://zhidao.baixing.com/paga-25.html
http://zhidao.baixing.com/paga-26.html
http://zhidao.baixing.com/paga-27.html
http://zhidao.baixing.com/paga-28.html
http://zhidao.baixing.com/paga-29.html
http://zhidao.baixing.com/paga-30.html
http://zhidao.baixing.com/paga-31.html
http://zhidao.baixing.com/paga-32.html
http://zhidao.baixing.com/paga-33.html
http://zhidao.baixing.com/paga-34.html
http://zhidao.baixing.com/paga-35.html
http://zhidao.baixing.com/paga-36.html
http://zhidao.baixing.com/paga-37.html
http://zhidao.baixing.com/paga-100.html
http://zhidao.baixing.com/paga-101.html
http://zhidao.baixing.com/paga-102.html
http://zhidao.baixing.com/paga-103.html
http://zhidao.baixing.com/paga-104.html
http://zhidao.baixing.com/paga-105.html
http://zhidao.baixing.com/paga-106.html
http://zhidao.baixing.com/paga-107.html
http://zhidao.baixing.com/paga-108.html
http://zhidao.baixing.com/paga-109.html
http://zhidao.baixing.com/paga-110.html
http://zhidao.baixing.com/paga-111.html
http://zhidao.baixing.com/paga-112.html
http://zhidao.baixing.com/paga-55.html
http://zhidao.baixing.com/paga-56.html
http://zhidao.baixing.com/paga-57.html
http://zhidao.baixing.com/paga-58.html
http://zhidao.baixing.com/paga-59.html
http://zhidao.baixing.com/paga-60.html
http://zhidao.baixing.com/paga-61.html
http://zhidao.baixing.com/paga-62.html
http://zhidao.baixing.com/paga-63.html
http://zhidao.baixing.com/paga-64.html
http://zhidao.baixing.com/paga-65.html
http://zhidao.baixing.com/paga-66.html
http://zhidao.baixing.com/paga-67.html
http://zhidao.baixing.com/paga-68.html
http://zhidao.baixing.com/paga-69.html
http://zhidao.baixing.com/paga-40.html
http://zhidao.baixing.com/paga-41.html
http://zhidao.baixing.com/paga-42.html
http://zhidao.baixing.com/paga-43.html
http://zhidao.baixing.com/paga-44.html
http://zhidao.baixing.com/paga-45.html
http://zhidao.baixing.com/paga-46.html
http://zhidao.baixing.com/paga-47.html
http://zhidao.baixing.com/paga-48.html
http://zhidao.baixing.com/paga-49.html
http://zhidao.baixing.com/paga-50.html
http://zhidao.baixing.com/paga-51.html
http://zhidao.baixing.com/paga-52.html
http://zhidao.baixing.com/paga-53.html
http://zhidao.baixing.com/paga-54.html
http://zhidao.baixing.com/paga-120.html
http://zhidao.baixing.com/paga-121.html
http://zhidao.baixing.com/paga-122.html
http://zhidao.baixing.com/paga-123.html
http://zhidao.baixing.com/paga-124.html
http://zhidao.baixing.com/paga-125.html
http://zhidao.baixing.com/paga-126.html
http://zhidao.baixing.com/paga-127.html
http://zhidao.baixing.com/paga-128.html
http://zhidao.baixing.com/paga-129.html
http://zhidao.baixing.com/paga-130.html
http://zhidao.baixing.com/paga-131.html
http://zhidao.baixing.com/paga-132.html
http://zhidao.baixing.com/paga-133.html
http://zhidao.baixing.com/paga-134.html
http://zhidao.baixing.com/paga-135.html
http://zhidao.baixing.com/paga-136.html
http://zhidao.baixing.com/paga-137.html
http://zhidao.baixing.com/paga-138.html
http://zhidao.baixing.com/paga-70.html
http://zhidao.baixing.com/paga-71.html
http://zhidao.baixing.com/paga-72.html
http://zhidao.baixing.com/paga-73.html
http://zhidao.baixing.com/paga-74.html
http://zhidao.baixing.com/paga-75.html
http://zhidao.baixing.com/paga-76.html
http://zhidao.baixing.com/paga-77.html
http://zhidao.baixing.com/paga-78.html
http://zhidao.baixing.com/paga-79.html
http://zhidao.baixing.com/paga-80.html
http://zhidao.baixing.com/paga-81.html
http://zhidao.baixing.com/paga-82.html
http://zhidao.baixing.com/paga-83.html
http://zhidao.baixing.com/paga-84.html
http://zhidao.baixing.com/paga-38.html
http://zhidao.baixing.com/paga-39.html
http://zhidao.baixing.com/paga-13.html
http://zhidao.baixing.com/paga-14.html
http://zhidao.baixing.com/paga-15.html
http://zhidao.baixing.com/paga-16.html
http://zhidao.baixing.com/paga-17.html
http://zhidao.baixing.com/paga-18.html
http://zhidao.baixing.com/paga-19.html
http://zhidao.baixing.com/paga-20.html
http://zhidao.baixing.com/paga-21.html
http://zhidao.baixing.com/paga-22.html
http://zhidao.baixing.com/paga-113.html
http://zhidao.baixing.com/paga-114.html
http://zhidao.baixing.com/paga-115.html
http://zhidao.baixing.com/paga-116.html
http://zhidao.baixing.com/paga-117.html
http://zhidao.baixing.com/paga-118.html
http://zhidao.baixing.com/paga-119.html
'''
