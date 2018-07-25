# coding=UTF-8
"""
命令行火车余票查询
Usage:
    tickets [-gdtkz] <from> <to> <date>
Options:
    -h, --help 显示帮助菜单
    -g         高铁
    -d         动车
    -t         特快
    -k         快速
    -z         直达
"""


import requests
from docopt import docopt
import station
from prettytable import PrettyTable  # 设置表格形式
from colorama import init, Fore  # 设置颜色

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

init()  # 对颜色设置进行初始化


def cli():
    arguments = docopt(__doc__)  # 用docopt来解析参数
    print(arguments)
    from_station = station.get_telecode(arguments.get('<from>'))
    to_station = station.get_telecode(arguments.get('<to>'))
    date = arguments.get('<date>')
    options = ''.join([key for key, value in arguments.items() if value is True])
    # 构造请求地址
    url = ('https://kyfw.12306.cn/otn/leftTicket/query?'
           'leftTicketDTO.train_data={}&'
           'leftTicketDTO.from_station={}&'
           'purpose_codes=ADULT').format(date, from_station, to_station)
    r = requests.get(url, verify=False, headers=headers)
    r.encoding = r.apparent_encoding
    if r.text.find('网络可能存在问题') != -1:
        print('网络存在问题，请重试，可能是你访问的过于频繁！')
        exit()

    # requests里面自带了json解析器，可以用来解析python
    raw_trains = r.json()['date']['result']  # 原始火车信息
    pt = PrettyTable()  # 初始化一个prettytable对象
    pt._set_field_names('车次 车站 时间 历时 一等座 二等座 软卧 硬卧 硬座 无座'.split())
    for raw_trains in raw_trains:
        date_list = raw_trains.split('|')
        train_no = date_list[3]
        initial = train_no[0].lower()  # 获取首字母，表示车次
        if not options or initial in options:  # 如果没有设置首字母或者首字母在options里面
            from_station_code = date_list[6]
            to_station_code = date_list[7]
            start_time = date_list[8]
            arrive_time = date_list[9]
            time_duration = date_list[10]
            first_class_seat = date_list[31] if date_list[31] else '_ _'
            second_class_seat = date_list[30] if date_list[30] else '_ _'
            soft_sleep = date_list[23] if date_list[23] else '_ _'
            hard_sleep = date_list[28] if date_list[28] else '_ _'
            hard_seat = date_list[29] if date_list[29] else '_ _'
            no_seat = date_list[26] if date_list[26] else '_ _'
            pt.add_row([
                Fore.YELLOW + train_no + Fore.RESET,
                '\n'.join([
                    Fore.GREEN + station.get_name(from_station_code) + Fore.RESET,
                    Fore.RED + station.get_name(to_station_code) + Fore.RESET
                ]),
                '\n'.join([
                    Fore.GREEN + start_time + Fore.RESET,
                    Fore.RED + arrive_time + Fore.RESET
                ]),
                time_duration,
                first_class_seat,
                second_class_seat,
                soft_sleep,
                hard_seat,
                no_seat
            ])
    print(pt)


if __name__ == '__main__':
    cli()
