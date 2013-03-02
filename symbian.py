#!/usr/bin/python
# encoding: utf-8
import socket
import appuifw,e32
import inbox,messaging
def init():
    appuifw.app.screen='normal'
def quit():
    app_lock.signal()
box=inbox.Inbox()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=server #server端地址
port=12345  #port
s.connect((host,port))
init()
while True:
        a=s.recv(1024)
        if a=="read":
                sms_id=box.sms_messages()
                n=0
                for j in range(len(sms_id)):
                        if(box.unread(sms_id[j])==1):
                                n=n+1
                #print n
                s.send(str(n))
                s.recv(1024)
                for i in range(len(sms_id)):
                        if(box.unread(sms_id[i])==1):
                                time=str(box.time(sms_id[i]))
                                add=box.address(sms_id[i]).encode('utf-8')
                                s.send(time+"  "+add)
                                s.recv(1024)
                                msg=box.content(sms_id[i]).encode('utf-8')
                                s.send(msg)
                                print s.recv(1024)
                                box.set_unread(sms_id[i],0)
                print s.recv(1024)
        elif a=="send":
                s.send("Phone-num:")
                num=s.recv(1024)
                s.send("content:")
                content=s.recv(1024)
                messaging.sms_send(num,content.decode('utf-8'),'UCS2')
                print "success"
                s.send("success")                
s.close()

