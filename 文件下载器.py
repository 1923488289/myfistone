import socket

# 建立套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
server_socket.bind(('', 8080))
# 建立监听，让套接字主动变为被动
server_socket.listen(128)
# 创建一个新的套接字，用来接收新的客户端
client_socket, ip_port = server_socket.accept()
print('新客户端的ip%s及端口%s' % (ip_port[0], ip_port[1]))
# 接收客户端发来的消息
file_name = client_socket.recv(1024).decode('gbk')
try:
    with open(file_name, 'rb') as files:
        while True:
            file = files.read(1024)
            if file:
                client_socket.send(file)
            else:
                print('发送完毕')
                break
except Exception as e:
    print('错误%s' % e)
else:
    print('图片下载完成')
client_socket.close()
server_socket.close()
