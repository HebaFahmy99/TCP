from socket import *
serverIP = '127.0.0.1'
serverPort = 1060

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
while True:

    sentence = input('Enter message to send or type Exit to disconnect: ')
    clientSocket.send(sentence.encode())
    ClientSentence = clientSocket.recv(1024)
    if ClientSentence.decode() == "Exit":
        print("Received Message from server: Disconnect")
        print("Now you are disconnected from the server")
        break
        clientSocket.close()
    inBytes =clientSocket.recv(100)
    print ('Received Message from server: Your data was', inBytes.decode(),"bytes")
