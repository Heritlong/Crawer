import urllib.request
import re

def get_html(url):
    try:
        page = urllib.request.urlopen(url)
        html = page.read()
        html = html.decode('utf-8')  # python3
    except urllib.request.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html

def get_image(html_code):
    reg = r'src="(.+?\.jpg)" style'
    reg_img = re.compile(reg)
    imglists = reg_img.findall(html_code)
    x = 0
    for img in imglists:
        print('开始下载 %s' % img)
        urllib.request.urlretrieve(img, '%s.jpg' % x)
        x += 1
        print('下载完成 %s' % img)


if __name__ == '__main__':
    print('网页抓取图片\n')
    url = input('输入URL：\n')

    html_code = get_html(url)

    print('开始下载图片')
    get_image(html_code)

    print('下载完成')



