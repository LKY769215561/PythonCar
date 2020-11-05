import requests
import os
import time
import threading
from bs4 import BeautifulSoup
import util


main_url = 'http://meizitu.com/a/more_{}.html'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}


#  下载网页html内容


def download_page(url):
    r = requests.get(url,headers)
    r.encoding = 'gb2312'
    return r.text

#  从html网页中找出图片链接


def get_pic_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    pic_list = soup.find_all('li', class_ = 'wp-item')
    for pic in pic_list:
        a_tag = pic.find('h3',class_='tit').find('a')
        link = a_tag.get('href')
        text = a_tag.get_text()
        get_pic(link,text)

#  根据图片链接下载图片并保存到相应文件夹


def get_pic(link,text):
    html = download_page(link)
    soup = BeautifulSoup(html,'html.parser')
    pic_list = soup.find('div',id='picture').find_all('img')
    dicName = 'girlPic/{}'.format(text)
    util.create_pic_dir(dicName)

    for img in pic_list:
        pic_link = img.get('src')  # 下载图片，之后保存到文件
        r = requests.get(pic_link, headers=headers)
        path = 'girlPic/{}/{}'.format(text, pic_link.split('/')[-1])
        # w:写文件 wb:写入二进制文件  a:拼接文件
        with open(path, 'wb') as f:
            f.write(r.content)
            time.sleep(1)   # 休息一下，不要给网站太大压力，避免被封


#  在子线程执行任务
def execute(url):
    html = download_page(url)
    get_pic_list(html)


def main():
    #  创建存放图片的文件目录
    util.create_pic_dir('girlPic')
    #  妹子图片链接关键下标
    queue = list(range(1,10))
    threads = []
    while len(queue) > 0:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads) < 5 and len(queue) > 0: #最大线程数为5
            cur_page = queue.pop(0)  # 拿出数组中第一个元素
            url = main_url.format(cur_page)
            thread = threading.Thread(target=execute(url))
            thread.setDaemon(True) #守护线程，当祝线程销毁系统会主动kill掉所有子线程
            thread.start()
            logstr = '线程:{}正在下载url:{}'.format(threading.current_thread().name,url)
            print(logstr)
            threads.append(thread)

#程序入口
if __name__ == '__main__':
    main()
