from socket import *
serverPort = 1060
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))

serverSocket.listen(1)
server_address_before = serverSocket.getsockname()

def Length(s):
    return len(s.encode('utf-8'))

connectionSocket, addr = serverSocket.accept()
server_address_after = connectionSocket.getsockname()

print("listening at",server_address_before)
print("The server now is connected to:", addr)

print("Sockets connects between",server_address_after," and", addr)
while True:
     sentence = connectionSocket.recv(1024).decode()
     print("Received Message from client:", sentence)
     SizeOfSentence = Length(sentence)
     connectionSocket.send(sentence.encode())
     connectionSocket.send(str(SizeOfSentence).encode())
     if sentence == "Exit":
          print("Reply sent, Server socket closed")
          print("listening at", server_address_before)
          break
          connectionSocket.close()
     
