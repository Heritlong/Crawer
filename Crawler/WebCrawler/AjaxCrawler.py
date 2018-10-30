from urllib.parse import urlencode

import pymongo
import requests
try:
    # Python 3.x
    from urllib.parse import quote_plus
except ImportError:
    # Python 2.x
    from urllib import quote_plus

base_url='https://m.weibo.cn/api/container/getIndex?'

headers={
    'Host':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/2830678474',
    'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X 10_12_3) AppleWebKit/537.36(KHTML,like Gecko Chrome/58.0.3029.110 Safari/537.36)',
    'X-Requested-With':'XMLHttpRequest',
}

def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page':page,
    }
    url = base_url+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error',e.args)

from pyquery import PyQuery as pq
def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            blog = item.get('mblog')
            if blog:
                print(str(blog))
                weibo = {}
                weibo['id'] = blog.get('id')
                weibo['text'] = pq(blog.get('text')).text()
                weibo['attitudes'] = blog.get('attitudes_count')
                weibo['comments'] = blog.get('comments_count')
                weibo['reposts'] = blog.get('reposts_count')
                yield weibo

usename = 'ats_test_01'
password = 'ats_test_01'
host = '10.97.2.44:27017/ATS_SYS'
uri = "mongodb://%s:%s@%s" % (
quote_plus(usename), quote_plus(password), host)
client = pymongo.MongoClient(uri)
db = client['ATS_SYS']
collection = db['weibo']

def save_to_mongo(result):
    if collection.insert_one(result):
        print('Saved to Mongo')



if __name__=='__main__':
    for page in range(1,11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)
