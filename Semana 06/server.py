import socket
import threading
import time

SERVER_IP = socket.gethostbyname(socket.gethostname()) #IP padrão
PORT = 5050 #porta
ADDR = (SERVER_IP, PORT) #endereço 
FORMATO = 'utf-8' #formato para decodificação da mensagem

print(SERVER_IP)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #classe e tipo de entrada e saída
server.bind(ADDR) #atribui um endereço de IP e um número de porta

conexoes = []
mensagens = []

def enviar_mensagem_individual(conexao): # Função para enviar mensagem individual
    print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
    for i in range(conexao['last'], len(mensagens)):
        mensagem_de_envio = "msg=" + mensagens[i]
        conexao['conn'].send(mensagem_de_envio.encode())
        conexao['last'] = i + 1
        time.sleep(0.2) # delay para dar tempo do envio e recebimento da mensagem

def enviar_mensagem_todos(): # Função para enviar mensagem para todos
    global conexoes
    for conexao in conexoes:
        enviar_mensagem_individual(conexao)






def handle_clientes(conn, addr):
    print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereco {addr}") #Printa o endereço de quem se conectou
    global conexoes
    global mensagens
    nome = False  #por enquanto não tem nome

    while(True):
        msg = conn.recv(1024).decode(FORMATO) # tamanho da mensagem
        if(msg): #caso a mensagem não seja nula
            if(msg.startswith("nome=")): #ate colocar o nome, nao recebe nada de volta
                mensagem_separada = msg.split("=")
                nome = mensagem_separada[1]
                mapa_da_conexao = {
                    "conn": conn,
                    "addr": addr,
                    "nome": nome,
                    "last": 0
                }
                conexoes.append(mapa_da_conexao)
                enviar_mensagem_individual(mapa_da_conexao) #quando enviar o nome, será passada o mapa de conexão 
            elif(msg.startswith("msg=")): #se houver a mensagem
                mensagem_separada = msg.split("=")
                mensagem = nome + "=" + mensagem_separada[1]
                mensagens.append(mensagem)
                enviar_mensagem_todos() # todos recebem a mensagem quando o usuário envia



def start():
    print("[INICIANDO] Iniciando Socket")
    server.listen() # ouvindo o cliente
    while(True):
        conn, addr = server.accept() # trava até alguém entrar
        thread = threading.Thread(target=handle_clientes, args=(conn, addr)) #quando entra uma nova pessoa, cria a thread
        thread.start() #inicia a thread

start()