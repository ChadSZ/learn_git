from flask import Flask
app=Flask(__name__)

# 实现输入的url末尾任意name 就可以获取 hello name
@app.route('/<name>')
def name(name):
    return 'hello %s' %name