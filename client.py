import socket

# Define the server's IP address and Port number
HOST = "172.16.50.115" # Listen on all available network interfaces
PORT = 10000

def start_client(): # Call A Variable Of start_client
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Ipv4,TCP
    try:
        client_socket.connect((HOST, PORT)) # Connect Through Host+Port Defined Above
        print(f" connected to server in : {HOST} : {PORT}")
        
        # Receive the initial welcome message from the server and decode it
        wellcome = client_socket.recv(1024).decode('utf-8') 
        print(f"Server says: {wellcome}") # Print the welcome message received
        
        while True: # While There Is A Connection
            # Prompt the user to type a message to send to the server
            message = input("send message to server or exit ") 
            
            # Check if the user wants to terminate the connection
            if message.lower() == "exit": 
                break # Exit the loop to close the connection
            
            # Convert the string message to bytes and send it to the server
            client_socket.sendall(message.encode('utf-8'))

            # Wait for a response from the server and decode the received bytes
            response = client_socket.recv(1024).decode('utf-8')
            print(f"server {response}") # Display the server's response
            
    except ConnectionRefusedError: # Handle cases where the server is not reachable
        print("connection failed")
    finally:
        # Ensure the socket is closed whether the loop finished or an error occurred
        client_socket.close() 

# Entry point of the script: run the start_client function
if __name__ == "__main__":
    start_client()