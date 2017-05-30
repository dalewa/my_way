import requests
from lxml import etree

data = ''
for i in range(3):
    url = 'http://www.qiushibaike.com/8hr/page/%d/' % i

    req = requests.get(url)
    html = req.text
    tree = etree.HTML(html)

    result = tree.xpath('//div[@class="article block untagged mb15"]')

    for div in result:
        author = div.xpath('.//h2/text()')
        data += ('\n' + author[0] + ':\t')
        if author[0] == '匿名用户':
            gender = '匿'
            age = '匿'
        else:
            xxx = div.xpath('.//div')
            gender = xxx[1].get('class')
            gender = gender.replace('articleGender ', '')
            gender = gender.replace('Icon', '')
            if gender == 'man':
                gender = '男'
            else:
                gender = '女'
            age = div.xpath('.//div[@class = "articleGender womenIcon"]/text()|'
                            './/div[@class = "articleGender manIcon"]/text()')
        data += (gender + '，')
        data += (age[0] + '\n')

        content = div.xpath('.//div[@class = "content"]/span/text()')
        haha = div.xpath('.//span[@class = "stats-vote"]/i/text()')
        comment = div.xpath('.//span[@class = "stats-comments"]/a/i/text()')
        data += (content[0] + '\t')
        data += ('好笑：' + haha[0] + '，')
        data += ('评论：' + comment[0] + '\n')

with open('QSBKnew.txt', 'w') as f:
    f.write(data)
