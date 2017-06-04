import requests
from lxml import etree
import urllib.request
import time
import random
from threading import Thread

def down_pic(link, i):
    print('downloading', link)
    filename = str(i)
    urllib.request.urlretrieve(link,'pics/' + filename + '.jpg')

header = {'User-Agent': 'Mozilla / 12.0'}

for i in range(0, 2):
    url = 'https://www.douban.com/photos/album/1633835572/?start=%d' % i
    req = requests.get(url)
    html = req.text
    tree = etree.HTML(html)
    result = tree.xpath('//a[@class="photolst_photo"]/@href')
    get = result[0]
    pic_name = get.split('/')[-2]
    pic_addr = 'https://img3.doubanio.com/view/photo/photo/public/p'+ pic_name + '.jpg'
    down_pic(pic_addr,i)
    time.sleep(random.randint(1, 5))
    '''
    t = Thread(target=down_pic, args=(pic_addr,i,))
    t.start()
    '''


