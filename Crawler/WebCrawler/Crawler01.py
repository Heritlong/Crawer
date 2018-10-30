import urllib.request
import urllib.parse
import http.cookiejar

page = 1

# url = 'https://www.python.org'
url = 'https://httpbin.org/post'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent, 'Host': 'httpbin.org'}
dic = {'name': 'Germey'}
data = bytes(urllib.parse.urlencode(dic), encoding='utf-8')



try:
    # cookie save

    filename = 'cookies.txt'
    cookie = http.cookiejar.LWPCookieJar(filename)
    # cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    response = opener.open('http://www.baidu.com')

    cookie.save(ignore_discard=True,ignore_expires=True)

    for item in cookie:
        print(item.name+'='+item.value)

    # cookie use
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    html = response.read()
    html = html.decode('utf-8')  # python3

    print(html)


    # page = urllib.request.urlopen(url, data=data)
    # request = urllib.request.Request(url=url,data=data, headers=headers, method='POST')
    # response = urllib.request.urlopen(request)
    # html = response.read()
    # html = html.decode('utf-8')  # python3

    # print(html)

    # print(type(page))

except urllib.request.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)
