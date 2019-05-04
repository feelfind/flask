# flask
learn flask
from flask import Flask#从 flask包导入 Flask类

app = Flask(__name__)#通过实例化这个类,创建一个程序对象app
@app.route('/<name>')#注册，就是给这个函数+一个装饰器帽子
def hello(name):#注册一个请求处理函数（view funciton视图函数）
    return '<h1>totoro:hello!%s</h1><img src="http://helloflask.com/totoro.gif"> ' %name

#wen jian ming gaiwei app.py huo set FLASK_APP= 
#enter url 127.0.0.1/+your name huo localhost:5000/+your's name


#使用 app.route() 装饰器来为这个函数绑定对应的 URL，
#当用户在浏览器访问这个 URL 的时候，就会触发这个函数，
#获取返回值return('welcom to www')，并把返回值显示到浏览器窗口
#填入 app.route() 装饰器的第一个参数是 URL 规则字符串，
#这里的/指的是根地址。

#我们只需要写出相对地址，主机地址、端口号等都不需要写出。
#所以说，这里的 / 对应的是主机名后面的路径部分,
#完整URL就是 http://localhost:5000/。
#如果我们这里定义的 URL 规则是 /hello，
#那么完整 URL 就是 http://localhost:5000/hello 。

#程序发现机制
#如果你把上面的程序保存成其他的名字，比如 hello.py，
#接着执行 flask run 命令会返回一个错误提示。
#这是因为Flask默认会假设你把程序存储在名为app.py或wsgi.py的文件中。
#如果你使用了其他名称，就要设置系统环境变量FLASK_APP来告诉Flask你要启动哪个程序。

#Flask通过读取这个文件对应的模块寻找要运行的程序实例，
#你可以把它设置成下面这些值：
#模块名
#Python 导入路径
#文件目录路径
