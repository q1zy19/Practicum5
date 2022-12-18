#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket, random, threading, csv
from CIPHERS import Ciphers
PORT = 9090
HOST = 'localhost'
sock = ''

def main():
    sock = socket.socket()
    sock.setblocking(True)
    Ch_p = Ciphers()
    sock.connect((HOST, PORT))
    print(f"Подсоединились к порту: {PORT}")
    keys = Ch_p.getting_key_client(sock)
    private_key = keys[5]
    port = int(Ch_p.decrypt(private_key, sock.recv(1024).decode()))
    sock.close()
    sock = socket.socket()
    sock.setblocking(True)
    sock.connect((HOST, port))
    print(f"Привязка к порту: {port}")
    threading.Thread(target=Ch_p.listening, args=(sock,private_key,), daemon=True).start()
    while True:
        cmd = input()
        if cmd == "exit":
            break
        Ci_cm = Ciphers()
        cmd = Ci_cm.encrypt(private_key, cmd)
        sock.send(cmd.encode())
    sock.close()

if __name__ == '__main__':
    main()

