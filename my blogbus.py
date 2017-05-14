# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = range(1,2)
for i in page:
    url = 'http://dalewa.blogbus.com/index_' + str(i) + '.html'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    try:
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)
        # print response.read()
        content = response.read().decode('utf-8')
        pattern=re.compile('h2.*?.html">(.*?)</a>.*?'+
                           '<h5 class="date">(.*?)</h5>.*?' +
                           '<div class="postBody">(.*?)</div> *?',re.S)
        items = re.findall(pattern, content)
        for item in items:
            li =  item[0].strip() + '\t' + item[1].strip() +  '\n' +  item[2].strip() +  '\n'
            print li
        

    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print e.code
        if hasattr(e, 'reason'):
            print e.reason
