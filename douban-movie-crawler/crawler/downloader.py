import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Cookie': 'bid=qFxaj2kLyc8; ap=1; gr_user_id=2feda33f-c50b-406b-8970-44586f3ea240; _vwo_uuid_v2=D2C2C70D11F35719728840EF7D89E66F4|93a17e68a16b6eed86995c39b7a798cd; viewed="3066477"; douban-fav-remind=1; __utmz=30149280.1532418191.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="118088"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1532484854%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DBDVY3VpnYIhXw-vKqx9remYPhm60Un_ODavKx3KLzskHPb_25MqxIAaA4OagDDNi%26wd%3D%26eqid%3Dee4015b900000bf7000000025b57dcf3%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.569107117.1532247545.1532418191.1532484860.4; __utmb=30149280.0.10.1532484860; __utmc=30149280; __utma=223695111.1455210317.1532484861.1532484861.1532484861.1; __utmc=223695111; __utmz=223695111.1532484861.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __yadk_uid=zXTv31yt5tBuGfFbJr4M6fqaFO8pGGh5; _pk_id.100001.4cf6=fc817c97b52b1bf8.1532484854.1.1532484892.1532484854.; __utmb=223695111.3.10.1532484861'
}


# 抓取短评数据
def download(url):
    try:
        # 若不登陆抓取的数据会有限，这里简化处理认证部分，直接把cookie的信息负值过来
        resp = requests.get(url,
                            header=headers,
                            timeout=3.0)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(e)
    except Exception as e:
        print(e)