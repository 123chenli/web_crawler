# from .manager import Managerl
from manager import Managerl
# from .downloader import download
from downloader import download
# from .parser import parse
from paramer import parsell
# from .processor import Processor
from processor import Processor


movie_id = 26752088
base_url = 'https://movie.douban.com/subject/26752088/comments'


class Crawler(object):

    def __init__(self):
        self._manager = Managerl(base_url)
        self._processor = Processor(host='192.168.1.104',
                                    collection='movei_{}_comments'.format(movie_id))

    def start(self, urls):
        """
        启动爬虫方法
        :param urls:
        :return:
        """
        number = 0
        self._manager.append_new_urls(urls)
        while self._manager.has_new_url():
            number += 1
            new_url = self._manager.get_new_url()
            print('开始下载第{:03}个url: {}'. format(number, new_url))
            html = download(new_url)
            if html is None:
                continue
            links, results = parsell(html, new_url)
            if len(links) > 0:
                self._manager.append_new_urls(links)
            if len(results) > 0:
                self._processor.process(results)
            return number


if __name__ == '__main__':
    crawler = Crawler()
    # 同时抓取看过和为看过的链接，两者的区别在于status查询参数上
    root_urls = ['?'.join([base_url, 'start=0&limit=20&sort=new_score&status=P']),
                 '?'.join([base_url, 'start=0&limit=20&sort=new_score&status=F'])]
    nums = crawler.start(root_urls)
    print('爬虫执行完成，共抓取{}个URL'.format(nums))