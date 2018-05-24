from app import app

# 如果当前这个文件是作为入口程序执行，那么就执行 app.run()
if __name__ == '__main__':
    app.run()     # 启动一个应用服务器，来接受用户的请求（一直在监听是否有请求，做死循环）
