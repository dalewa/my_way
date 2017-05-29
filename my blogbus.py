# -*- coding:utf-8 -*-
import requests
import re

page = range(1, 2)
data_all = ''
for i in page:
    url = 'http://dalewa.blogbus.com/index_%d.html' % i
    req = requests.get(url)
    html = req.text

    pattern = re.compile('h2.*?.html">(.*?)</a>.*?'+
                           '<h5 class="date">(.*?)</h5>.*?' +
                        '<div class="postBody">(.*?)</div> *?',re.S)
    items = re.findall(pattern,html)
    for item in items:
        li = item[0].strip() + '\t' + item[1].strip() + '\n' + item[2].strip() + '\n\n'
        li = li.replace('<p>','')
        li = li.replace('</p>', '')
        li = li.replace('<br /><br />', '\n')
        data_all += li

with open('myblog.txt', 'w', encoding = 'utf-8')  as f:
    f.write(data_all)
