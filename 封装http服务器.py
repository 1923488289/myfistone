import socket
import sys
import re
import appmes
import gevent
from gevent import monkey

monkey.patch_all()


class ServerHttp(object):
    def __init__(self, port):
        self.port = port
        # 创建套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置地址重用
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
        # 绑定端口
        server_socket.bind(('', self.port))
        # 绑定监听
        server_socket.listen(128)
        self.server_socket = server_socket

    def start(self):
        while True:
            # 设置地址重用
            client_socket, ip_port = self.server_socket.accept()
            print('有新的客户端来了%s' % str(ip_port))
            # recv_message(client_socket)
            gevent.spawn(self.recv_message, client_socket)

    def recv_message(self, client_socket):
        # print('--------')
        message = client_socket.recv(1024)
        message = message.decode('utf8')
        if not message:
            print('客户端离开')
            client_socket.close()
            return
        # message = message.decode('gbk')
        result = re.search(r'\s(/.*?)\s', message)
        if not result:
            print('未能匹配到')
            client_socket.close()
            return

        url_1 = result.group(1)
        print(url_1)
        if url_1 == '/':
            url_1 = '/index.html'
        if url_1.endswith('.html'):
            env = {'path_url': url_1}
            response_messages = ''
            response_2 = ''
            print('_---------_')
            url_line, url_heard, url_body = appmes.app(env)
            response_1 = 'HTTP/1.1 %s\r\n' % url_line
            for i in url_heard:
                response_2 += '%s:%s\r\n' % i
            response_messages += response_1 + response_2 + '\r\n' + url_body
            response_messages = response_messages.encode('utf8')
            client_socket.send(response_messages)
            client_socket.close()
        else:
            response_header = 'Server:python-plus\r\n'
            response_kg = '\r\n'
            try:
                with open('static/' + url_1, 'rb') as file:
                    response_body = file.read()
            except Exception as e:
                response_line = 'HTTP/1.1 404 Not Found\r\n'
                response_body = '错误%s' % e
                response_body = response_body.encode('utf8')
            else:
                response_line = 'HTTP/1.1 200 OK\r\n'

            responses = response_line + response_header + response_kg
            responses = responses.encode('utf8') + response_body
            client_socket.send(responses)
            client_socket.close()


def main():
    if len(sys.argv) != 2:
        print('请重新输入')
        return
    if sys.argv[1].isdigit():
        port = int(sys.argv[1])
    else:
        print('请重新输入端口－格式如：8080')
        return
    serht = ServerHttp(port)
    serht.start()


if __name__ == '__main__':
    main()
