# -*- coding: cp936 -*-
import csv
import urllib2
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
# import cookielib
# import re
# import codecs
# import urllib

wiki = 'http://piaofang168.com/index.php/Jinzhun'
header = {'User-Agent': 'Mozilla / 12.0'}
req = urllib2.Request(wiki, headers = header)
page = urllib2.urlopen(req)
doc = page.read()
soup = BeautifulSoup(doc, 'html.parser', from_encoding = 'utf-8')

title = ""    # 片名
dailybox = ""    # 今日票房
totalbox = ""    # 累计票房
pscreenings = ""   # 今日排片
nscreenings = ""   # 今日场次
days = ""   # 上映天数
today = soup.find('h1')
today_text = today.get_text()
curtime = time.strftime('%Y-%m-%d')

table = soup.find('table', {'class': "gross_table"})
f = open(curtime + '.csv', 'wb')
csv_writer = csv.writer(f)

for row in table.find_all('tr'):
	cells = row.find_all('td')
	if len(cells) == 6:
		title = cells[0].find(text = True)
		if not title:
			continue
		dailybox = cells[1].find(text = True)
		totalbox = cells[2].find(text = True)
		pscreenings = cells[3].find(text = True)
		nscreenings = cells[4].find(text = True)
		days = cells[5].find(text = True)
		csv_writer.writerow([today_text.decode('utf-8').encode('mbcs')] +
                                    [x.decode('utf-8').encode('mbcs') for x in [title, dailybox, totalbox, pscreenings, nscreenings, days]])

f.close()
