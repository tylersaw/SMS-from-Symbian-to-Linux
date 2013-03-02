# encoding: utf-8
import socket
import os
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=server #接受信息的主机IP
print host
port=port #自定义端口
s.bind((host,port))
s.listen(5)
while True:
        c,addr=s.accept()
        while True:
                try:
                        a=raw_input("input:")
                        if a=="read":
                                c.send(a)
                                m=c.recv(1024)
                                c.send("ok")
                                n=int(m)
                                print "insgsamt "+str(n)+" SMS"
                                while n>0:
                                        print "No."+str(n)+":"+c.recv(1024)
                                        c.send("time recived")
                                        print c.recv(1024)
                                        c.send(str(n))
                                        n=n-1
                                print "it is over"
                                c.send("message has recivied")
                        elif a=="send":
                                c.send(a)
                                b=raw_input(c.recv(1024))
                                c.send(b)
                                b=raw_input(c.recv(1024))
                                c.send(b)
                                print c.recv(1024)
                        else:
                                continue
                except:
        c.close()

