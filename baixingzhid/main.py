from multiprocessing import Pool
from channel_extract import channel_list
from page_parsing import get_links_from

def get_all_links_from(channel):
    for num in range(1,5):
        get_links_from(channel,num)


# 可运行
#get_all_links_from('http://zhidao.baixing.com/page-23')

# bug
#pool = Pool()
#pool.list(map(get_all_links_from,channel_list.split()))

#可运行
list(map(get_all_links_from,channel_list.split()))
