from multiprocessing import Pool
from channel_extract import channel_list
from page_parsing import get_links_from

# 将详细页面链接保存到数据库
def get_all_links_from(channel):
    for num in range(1,5):
        get_links_from(channel,num)


# 可运行
#get_all_links_from('http://zhidao.baixing.com/page-23')

# BUG
#pool = Pool()
#pool.list(map(get_all_links_from,channel_list.split()))

#可运行
list(map(get_all_links_from,channel_list.split()))
'''
http://zhidao.baixing.com/question/302413.html
http://zhidao.baixing.com/question/298661.html
http://zhidao.baixing.com/question/297614.html
http://zhidao.baixing.com/question/297435.html
http://zhidao.baixing.com/question/297861.html
http://zhidao.baixing.com/question/297611.html
http://zhidao.baixing.com/question/297863.html
http://zhidao.baixing.com/question/297085.html
http://zhidao.baixing.com/question/296720.html
http://zhidao.baixing.com/question/296353.html
http://zhidao.baixing.com/question/296536.html
http://zhidao.baixing.com/question/295791.html
http://zhidao.baixing.com/question/295604.html
http://zhidao.baixing.com/question/295210.html
http://zhidao.baixing.com/question/295009.html
http://zhidao.baixing.com/question/294210.html
http://zhidao.baixing.com/question/294807.html
http://zhidao.baixing.com/question/293593.html
http://zhidao.baixing.com/question/293386.html
http://zhidao.baixing.com/question/293589.html
http://zhidao.baixing.com/question/308810.html
http://zhidao.baixing.com/question/308805.html
http://zhidao.baixing.com/question/309178.html
http://zhidao.baixing.com/question/308812.html
http://zhidao.baixing.com/question/308222.html
http://zhidao.baixing.com/question/307822.html
http://zhidao.baixing.com/question/308225.html
http://zhidao.baixing.com/question/307600.html
http://zhidao.baixing.com/question/307408.html
http://zhidao.baixing.com/question/307394.html
http://zhidao.baixing.com/question/307395.html
http://zhidao.baixing.com/question/306345.html
http://zhidao.baixing.com/question/306550.html
http://zhidao.baixing.com/question/306148.html
http://zhidao.baixing.com/question/305922.html
http://zhidao.baixing.com/question/306352.html
http://zhidao.baixing.com/question/306562.html
http://zhidao.baixing.com/question/305700.html
http://zhidao.baixing.com/question/305706.html
http://zhidao.baixing.com/question/304399.html
http://zhidao.baixing.com/question/302413.html
http://zhidao.baixing.com/question/298661.html
http://zhidao.baixing.com/question/297614.html
http://zhidao.baixing.com/question/297435.html
http://zhidao.baixing.com/question/297861.html
http://zhidao.baixing.com/question/297611.html
http://zhidao.baixing.com/question/297863.html
http://zhidao.baixing.com/question/297085.html
http://zhidao.baixing.com/question/296720.html
http://zhidao.baixing.com/question/296353.html
http://zhidao.baixing.com/question/296536.html
http://zhidao.baixing.com/question/295791.html
http://zhidao.baixing.com/question/295604.html
http://zhidao.baixing.com/question/295210.html
http://zhidao.baixing.com/question/295009.html
http://zhidao.baixing.com/question/294210.html
http://zhidao.baixing.com/question/294807.html
http://zhidao.baixing.com/question/293593.html
http://zhidao.baixing.com/question/293386.html
http://zhidao.baixing.com/question/293589.html
http://zhidao.baixing.com/question/292758.html
http://zhidao.baixing.com/question/292136.html
http://zhidao.baixing.com/question/291370.html
http://zhidao.baixing.com/question/290542.html
http://zhidao.baixing.com/question/290254.html
http://zhidao.baixing.com/question/290826.html
http://zhidao.baixing.com/question/289374.html
http://zhidao.baixing.com/question/289110.html
http://zhidao.baixing.com/question/288523.html
http://zhidao.baixing.com/question/287322.html
http://zhidao.baixing.com/question/286749.html
http://zhidao.baixing.com/question/284734.html
http://zhidao.baixing.com/question/285018.html
http://zhidao.baixing.com/question/285014.html
http://zhidao.baixing.com/question/284109.html
http://zhidao.baixing.com/question/284120.html
http://zhidao.baixing.com/question/283522.html
http://zhidao.baixing.com/question/283202.html
http://zhidao.baixing.com/question/283198.html
http://zhidao.baixing.com/question/281350.html
'''
