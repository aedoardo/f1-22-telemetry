#  Copyright (c) 2022.
#
#  25/12/22, 17:00, main.py created by Edoardo.
#
#  25/12/22, 10:55, main.py created by Edoardo.

import socket

from Managers.MainManager import PacketsManager

if __name__ == "__main__":

    pManager = PacketsManager()
    HOST, PORT = "192.168.56.1", 27222

    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((HOST, PORT))

    while True:
        try:
            data: bytes = UDPServerSocket.recv(2048)
            pManager.onData(data)

        except Exception as e:
            pass


