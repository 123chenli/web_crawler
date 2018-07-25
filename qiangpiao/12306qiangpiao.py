import requests
import re
from pprint import pprint
def main():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9025'
    r = requests.get(url, verify=False)  # verify可以去除https验证
    r.encoding = r.apparent_encoding
    pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'  # 正则表达式，匹配汉字和字母
    result = dict(re.findall(pattern, r.text))
    print(result.keys())
    print(result.values())

if __name__ == '__main__':
    main()