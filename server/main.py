import socket
import json
import threading
from protocol import Protocols
import time

class Server:
    def __init__(self,host="127.0.0.1",port=55555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((self.host,self.port))
        self.server.listen()
         
        self.client_names = {}
        self.opponent = {}
        self.rooms = {}
        self.waiting_for_pair = None
         

    def receive(self):
        while true:
            client,address = self.server.accept()
            print(f"Connected with {address}")
            thread = threading.Thread(self.handle,args=(client,))
            thread.start()

    def handle(self,client):
        self.handle_connect(client)

    def handle_connect(self,client):
        while true:
            self.send(Protocols.Response.NICKNAME,None,client)
            message = json.loads(client.recv(1024).decode("ascii"))
            r_type = message.get("type")
            nickname = message.get("data")

            if r_type == Protocols.Response.NICKNAME:
                self.client_names[client] = nickname
            else:
                continue

            if not self.waiting_for_pair:
                self.waiting_for_pair = client
                print("waiting for a room")
            else:
                self.create_room(client)

            break    
        




    def send(self,r_type,data,client):
        message = {
            "type" : r_type,
            "data" : data
        }
        message = json.dumps(message).encode("ascii")
        client.send(message)
