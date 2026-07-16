import socket
import threading

HOST = "172.20.10.2"
PORT = 10000

def handle_client(conn , addr ): #Define The Function Of handle_client
    print(f"client connected in : {addr}")
    try:
        wellcome = "wellcome"
        conn.sendall(wellcome.encode('utf-8')) #Encode The String Which Will Be Send To The Whole Clients
        #Sends To All Of The Clients Which Connected
        
        while True:
            data = conn.recv(1024) #Limit The Packets In Order To See How It Being Splited On WireShark
            if not data: #If I didn't Get Any Data From Client
                break
            data_d = data.decode("utf-8") #Getting The Data On Specific Encoding
            print(f"got from client message : {addr} : {data_d}")
            response = f"server receive {data_d.upper()}"
            conn.sendall (response.encode('utf-8'))
    except ConnectionResetError: #Handle Connection Error From Client
        print(f" client dissconnected {addr}")
    finally:
        conn.close() #Close The Connection With The Client
        




def start_server(): #Define The Start Of The Server 
    server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #Server Will Be Run On Ipv4,TCP
    server_socket.bind((HOST , PORT)) #Server Will Be Run On The Variables Above
    server_socket.listen() #Define Lisetener Which Handle Client Connection

    print( f"server listn in :  { HOST}: {PORT}")

    while True: #While Server Is Running
        conn , addr = server_socket.accept() #Accept Clients Which Connect Through The Host And Port
        client_thread = threading.Thread (target=handle_client , args=(conn , addr)) #Define Something To Give The Client
        client_thread.start() #Starting The handle_client
        print(f"client online  {threading.active_count() -1} " ) #Print How Many Clients Active

if __name__ == "__main__":
    start_server()