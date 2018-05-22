# coding=utf-8
# 3.X支持读取和写入二进制文件
f = open('file.txt', 'wb')
f.write(bytes([12, 12, 12, 0x12]))
f.close()
f = open('file.txt', 'rb')
s = f.read()
f.close()
print(s)
