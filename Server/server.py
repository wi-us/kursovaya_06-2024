import socket
import datetime
import route
import json

def serializeJson(object) -> str:
    return json.dumps(object)

def deserializeJson(string : str) -> str:
    return json.loads(string)

IP = '0.0.0.0'
PORT = 8001

PROTOCOL = "HTTP/1.1"
CONTENT = "Content-Type: application/json;"
CHARSET = "charset=utf-8"
HEADERS = f"{CONTENT} {CHARSET}"
#"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
CODE_200 = "200 OK"
CODE_401 = "401 Unauthorized"
CODE_404 = "404 Not_Found"
CODE_404 = "404 Not_Found"


class Server:

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
        

        if '{' in requestData:
            _index = requestData.find('{')
            _json = requestData[_index-1:]
            json = deserializeJson(_json[1:])
            response = route.routeToAPI(_data[0], _data[1][1:], **json)
        else:
            response = route.routeToAPI(_data[0], _data[1][1:])
        
        #answer = serializeJson(response['answer'])
        #_ans = serializeJson(response['answer']).encode('utf-8')
        #_a = bytearray(serializeJson(response['answer']).encode('utf-8'))
        return f"{PROTOCOL} {response['code']}\r\n{HEADERS}\r\n\r\n".encode('utf-8') + bytearray(serializeJson(response['answer']).encode('utf-8'))
        try:
            with open('views' + path, 'rb') as file:
                response = file.read()
            return f"{PROTOCOL} {CODE_200}\r\n{HEADERS}\r\n\r\n".encode('utf-8') + response 
        except: #страница не найдена
            message = "ТЕСТПИРОВАИНВШГЛЫМДЫвлм"
            return (f"{PROTOCOL} {CODE_404}\r\n{HEADERS}\r\n\r\n" + message).encode('utf-8')
        
    


    
if __name__ == "__main__":
    Server().startServer()