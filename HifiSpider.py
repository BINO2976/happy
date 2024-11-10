import requests
from lxml import etree
from functools import partial
import subprocess
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import requests
import re
import execjs
import os

class HifiSpider:
    def __init__(self):
        self.url = 'https://hifini.com/tag-1870-{}.htm'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        return response.text

    def parse_data(self, html):
        html = etree.HTML(html)
        link = html.xpath('//div[@class="subject break-all"]//a/@href')
        for link in link:
            link = 'https://hifini.com/' + link
            data = self.get_data(link)
            name = re.findall(r"title:\s*'([^']+)'", data)
            if name:
                url = re.findall(r"url:\s*'([^']+)'", data)
                data = re.findall(r"generateParam\('([^']+)'\)", data)
                if not data:
                    continue
                node = execjs.get()
                fp = open('HifiSpider.js', 'r', encoding='utf-8')
                ctx = node.compile(fp.read())
                result = ctx.call('generateParam', data[0])
                link = 'https://hifini.com/{}&p={}'.format(url[0], result)
                content = requests.get(link, headers=self.headers).content
                if not os.path.exists('music'):  # 判断文件夹是否存在
                    os.mkdir('music')
                with open('music/{}.m4a'.format(name[0]), 'wb') as f:
                    f.write(content)
                print('{} 下载成功'.format(name[0]))
                print('--------------------')


    def save_data(self, data):
        pass

    def run(self):
        for i in range(6, 8):
            html = self.get_data(self.url.format(i))
            print('正在获取第 {} 页数据'.format(i))
            self.parse_data(html)

if __name__ == '__main__':
    spider = HifiSpider()
    spider.run()