import socket
import threading
import time

PORT = 5050 #porta
FORMATO = 'utf-8' #formato para decodificação da mensagem
SERVER = "192.168.56.1" #IP 
ADDR = (SERVER, PORT) #endereço 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #classe e tipo de entrada e saída
client.connect(ADDR) #conexão

def handle_mensagens(): #gerenciar as mensagens do servidor
    while(True):
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])

def enviar(mensagem):
    client.send(mensagem.encode(FORMATO))

def enviar_mensagem():
    mensagem = input()  #envia a mensagem
    enviar("msg=" + mensagem) # chama a função

def enviar_nome():
    nome = input('Digite seu nome: ') #envia o nome
    enviar("nome=" + nome)  # chama a função

def iniciar_envio():
    enviar_nome()       # chama a função
    enviar_mensagem()   # chama a função

def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start() #inicia a thread
    thread2.start() #inicia a thread

iniciar()