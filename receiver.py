import socket
import datetime

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

ip_address="127.0.0.1" 
port_no = 2525


complete_address=(ip_address,port_no)


s.bind(complete_address)

print("HEY i AM LISTENING... ")
while True:
    message, addr = s.recvfrom(100)
    print("Received: ", message.decode())
    print("\n")
    
    sentMsg=input("Enter message to send: ")
    s.sendto(sentMsg.encode(),addr)

    timeDate=str(datetime.datetime.now())
    with open('data.txt','a') as file_obj:
        file_obj.write(f"sent by receiver: {message.decode()}  ; sender's address: {addr}  ; date & time: {timeDate}  \n\n")



