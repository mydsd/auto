import socket
class ConnectTcp():
    def __init__(self,host,port):
        self.connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect.connect((host,port))
    def send_tcp(self,msg,bate):
        self.connect.send(msg)
        response = self.connect.recv(bate).decode('utf-8')
        self.connect.close()
        return response