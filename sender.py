import socket
import datetime 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


target_ip='127.0.0.1'
target_port=2525
target_address=(target_ip,target_port)

while True:
    message  = input('plz enter your message: ')
    message= message.encode('ascii')
    s.sendto(message,target_address)
    receivedMsg,addr=s.recvfrom(100)
    print("Received : ",receivedMsg.decode())
    print("\n")

    timeDate=str(datetime.datetime.now())
    with open('data.txt','a') as file_obj:
        file_obj.write(f"sent by sender: {message.decode()} ;  'receivers ' address: {addr}  ;  date & time: {timeDate}  \n\n")


