''' 所需安装模块
pip install websocket
pip install websocket-client
'''
import websocket
import _thread
import time

# 在接收到服务器发送消息时调用
def on_message(ws, message):
    print('Received: ' + message)

# 在和服务器简历完成连接时调用
def on_open(ws):
    # 线程运行函数
    def gao():
        # 往服务器依次发送 0-4, 每次发送完休息0.1 秒
        for i in range(5):
            time.sleep(0.01)
            msg = "{0}".format(i)
            ws.send(msg)
            print('Sent: ' + msg)
        # 休息1秒由于接受服务器回复的消息
        time.sleep(1)

        # 关闭websocket 连接
        ws.close()
        print('WebSocket closed')

    # 在另一个线程运行 gao() 函数
    _thread.start_new_thread(gao, ())


if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                                on_message = on_message,
                                on_open = on_open)
    ws.run_forever()