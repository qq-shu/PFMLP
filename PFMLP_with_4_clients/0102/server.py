import json
import socket  # 导入 socket 模块
import numpy as np
from encrypt_paillier import create_key_pair
import pickle

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12346  # 设置端口
s.bind((host, port))  # 绑定端口
flag = 0
s.listen(5)  # 等待客户端连接
list = []
p = []
p1 = []
C = []
c1 = []
while True:
    c, addr = s.accept()  # 建立客户端连接
    print(addr)
    C.append(c)
    res = c.recv(1024)
    print(res)
    if len(res) == 1:
        # print('*')
        # list.append(json.loads(res.decode('utf-8')))
        flag += 1
        if flag == 4:
            input1 = open("mid_need/grad1.pkl",'rb')
            in_a = pickle.load(input1)
            input2 = open("mid_need/grad2.pkl",'rb')
            in_b = pickle.load(input2)
            input3 = open("mid_need/grad4.pkl", 'rb')
            in_c = pickle.load(input3)
            input4 = open("mid_need/grad5.pkl", 'rb')
            in_d = pickle.load(input4)
            input1.close()
            input2.close()
            input3.close()
            input4.close()
            # a = pickle.load("mid_need/grad1.pkl",encoding='bytes')
            # b = pickle.load("mid_need/grad2.pkl",encoding='bytes')
            print(len(in_a[0]))
            print(len(in_b[0]))
            print(len(in_c[0]))
            print(len(in_d[0]))
            # print(a[1])
            # print(b[1])
            # c = np.add(a[1], b[1]).tolist()
            out = []
            for item in range(len(in_a)):
                tmp = np.add(in_a[item], in_b[item])
                tmp = np.add(tmp,in_c[item])
                tmp = np.add(tmp,in_d[item])
                out.append(tmp)
            print(len(out[0]))
            output = open('mid_need/grad3.pkl', 'wb')
            pickle.dump(out, output)
            output.close()
            # np.save("C:\\Users\\FangHaokun\\PycharmProjects\\ml\\1209\\mid_need\\grad3.npy", c)
            print('load_finish')
            for i in C:
                i.send('finish'.encode('utf-8'))
                i.close()  # 关闭连接

            print('send_finish')
            flag = 0
            C = []
            # list = []
    if len(res) == 3:
        # print('*')
        # list.append(json.loads(res.decode('utf-8')))
        flag += 1
        if flag == 2:
            input1 = open("mid_need/grad1.pkl",'rb')
            a = pickle.load(input1)
            input2 = open("mid_need/grad2.pkl",'rb')
            b = pickle.load(input2)
            input1.close()
            input2.close()
            # a = pickle.load("mid_need/grad1.pkl",encoding='bytes')
            # b = pickle.load("mid_need/grad2.pkl",encoding='bytes')
            print(len(a[0]))
            print(len(b[0]))
            # print(a[1])
            # print(b[1])
            # c = np.add(a[1], b[1]).tolist()
            c = []
            for item in range(len(a)):
                tmp = np.add(a[item], b[item]).tolist()
                c.append(tmp)
            print(len(c[0]))
            print(c)
            output = open('mid_need/grad3.pkl', 'wb')
            pickle.dump(c, output)
            output.close()
            # np.save("C:\\Users\\FangHaokun\\PycharmProjects\\ml\\1209\\mid_need\\grad3.npy", c)
            print('load_finish')
            for i in C:
                i.send('finish'.encode('utf-8'))
                i.close()  # 关闭连接

            print('send_finish')
            flag = 0
            C = []
            # list = []
    if len(res) == 2:
        print('%')
        flag += 1
        if flag == 4:
            public_key, private_key = create_key_pair()
            key = []
            key.append(public_key)
            key.append(private_key)
            # key.append(pickle.dumps(public_key))
            # key.append(pickle.dumps(private_key))
            key_pair = pickle.dumps(key)
            print(key_pair)
            print('create_key_pair_finish')
            for i in C:
                i.send(key_pair)
                i.close()  # 关闭连接
            print('send_finish')
            flag = 0
            C = []

    if res.decode('utf-8') == 'close':
        s.close()
        break
print('Successful Closed.')