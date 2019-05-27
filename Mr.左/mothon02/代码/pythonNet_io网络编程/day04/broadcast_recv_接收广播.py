# 广播接收
"""
1.创建udp套接字
2.设置套接字为可以接收广播
3.选择接收端口
"""
from socket import *

s = socket(AF_INET, SOCK_DGRAM)

# 　让套接字可以接收广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

s.bind(('0.0.0.0', 3189))

# 循环接收
while True:
    try:
        msg, addr = s.recvfrom(1024)
    except KeyboardInterrupt:
        break
    else:
        print(msg.decode())

s.close()
