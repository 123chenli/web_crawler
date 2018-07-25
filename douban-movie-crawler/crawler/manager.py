"""
处理重复数据
"""

class Managerl(object):

    def __init__(self, base_url=None):
        self.base_url = base_url
        self.new_urls = []
        self.old_urls = []

    def append_new_url(self, urls):
        if len(urls) == 0:
            return
        for url in urls:
            # 过滤非目标url
            if self.base_url not in url:
                continue
            # 排列倒序数据，避免重复抓取
            if '&20limit=-20' in url:
                continue
            # 去掉多余查询参数
            if '&percent_type' in url:
                url = url.replace('&percent_type', '')
            # url重复检查
            if url not in self.new_url and url not in self.old_url:
                self.new_urls.append(url)

    def has_new_url(self):
        return len(self.new_urls) > 0

    def get_new_url(self):
        # 获取一个新的url，内部隐含了url抓取过后加入已经抓取队列操作
        url = self.new_urls.pop()
        self.old_urls.append(url)
        return url