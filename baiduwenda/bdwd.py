# 仿百度知道
import web

urls = (
    '/', 'Index',
)

app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self): # 执行的函数是根据请求的方式来确定 GET POST
        return render.head('hello world')

if __name__ == '__main__':
    app.run()