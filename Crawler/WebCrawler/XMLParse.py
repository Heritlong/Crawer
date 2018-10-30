from lxml import etree

html = etree.parse('./html.txt', etree.HTMLParser())
result = html.xpath('//*')
print(result)