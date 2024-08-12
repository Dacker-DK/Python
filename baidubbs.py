#DK
from urllib.request import Request,urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

def get_html(url):
    header={
        "User-Agent":UserAgent().chrome
    }
    request = Request(url,headers=header)
    response = urlopen(request)
    print(response.read().decode())
    return response.read()
def save_html(filename,html_bytes):
    with open(filename,"wb") as f:
        f.write(html_bytes)

def main():
    content = input("请输入要下载的内容")
    num = input("请输入要下载的页数")
    base_url = "https://tieba.baidu.com/f?&ie=utf-8&{}"
    for pn in range(int(num)):
        args = {
            "pn": pn * 50,
            "kw": content
        }
        filename = str(content) + "吧的第" + str(pn) + "页.html"
        args = urlencode(args)
        print("正在下载"+filename)
        html_bytes = get_html(base_url.format(args))
        save_html(filename, html_bytes)
    for pn in range(int(num)):
        args = {
            "pn":pn*50,
            "kw":content
        }
        args=urlencode(args)
        print(str(content) + "吧的第" + str(pn) + "页")
        print(base_url.format(args))

if __name__ == '__main__':
    main()