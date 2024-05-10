import socket
import requests
import json
import time

def serializeJson(object) -> str:
    return json.dumps(object)

def deserializeJson(string : str) -> str:
    return json.loads(string)
IP = '5.141.89.214'
PORT = 8001

header = {
    "Content-Type": "application/json; charset=utf-8",
    

}

test = {}
#req = requests.get(url=f"http://{IP}:{PORT}/table", headers=header)
strJson = serializeJson({"guestCountMax":5, "vipStatus":True})
req = requests.post(url=f"http://{IP}:{PORT}/table", headers=header, data=strJson)
print(deserializeJson(req.content))

time.sleep(1) 
print(deserializeJson(requests.get(url=f"http://{IP}:{PORT}/table", headers=header).content))

PROTOCOL = "HTTP/1.1"
CONTENT = "Content-Type: text/html;"
CHARSET = "charset=utf-8"
HEADERS = f"{CONTENT} {CHARSET}"
#"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
CODE_200 = "200 OK"
CODE_401 = "401 Unauthorized"
CODE_404 = "404 Not_Found"
CODE_404 = "404 Not_Found"


class Client:

    def startServer(cls):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((IP, PORT))
            server.listen()

            while 1:
                print("Working...")
                
                clientSocket, adress = server.accept()
                print(f"Connected by {adress}")
                data = clientSocket.recv(1024).decode('utf=8')
                content = cls.loadPageFromGetRequest(data)
                clientSocket.sendall(content)
                clientSocket.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            server.close()
            print('shutdown server...')

    def loadPageFromGetRequest(cls, requestData : str):
        _data = requestData.split(' ') #разбиение ответа
        path = ""
        if len(_data) > 0:
            path = requestData.split(' ')[1] #получение пути

        response = ''

        try:
            with open('views' + path, 'rb') as file:
                response = file.read()
            return f"{PROTOCOL} {CODE_200}\r\n{HEADERS}\r\n\r\n".encode('utf-8') + response 
        except: #страница не найдена
            message = "ТЕСТПИРОВАИНВШГЛЫМДЫвлм"
            return (f"{PROTOCOL} {CODE_404}\r\n{HEADERS}\r\n\r\n" + {message}).encode('utf-8')
        
    
''''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((f"{IP}:{PORT}/user"))

    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")

'''
