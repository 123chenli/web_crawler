import urllib.parse
import urllib.request
response = urllib.request.urlopen('http://www.python.org')
# print(response.read().decode('utf-8'))  # 查看输出信息
# print(dir(response))  # 查看HTTPResponsne类型的对象的属性
# print(response.status)
# print(response.getheaders())  # 响应头信息
# print(response.getheader('Server'))  # 使用Nginx服务器搭建的


# data参数
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')  # 转化为字节流，将参数字典转化为字符串，并指定编码形式
response = urllib.request.urlopen('http://httpbin.org/post', data =data)  # 使用新连接来测试post请求
print(response.read())

# timeout参数： 若请求超过设定的timeout还没有相应，就会抛出异常


#