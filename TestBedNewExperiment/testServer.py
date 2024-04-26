
import socket
 
# import thread module
from _thread import *
import threading
 
print_lock = threading.Lock()
 
# thread function
def threaded(c):
    while True:
 
        # data received from client
       data = c.recv(1024).decode()####1.Client Send the Agreeement Token 
        
       time.sleep(1)
       if data==result1[0]['txid']:
            # if data is not received break
            print("Txid Verification Ok: " + str(data))
            data="ACK Send Role"
            
            
            c.send(data.encode())  # send Request to Send role ###########2.Server Send Ack to Client 
            data1 = c.recv(1024).decode()####3.Recieved Role from CLient Machine 
            
            data2="Send the Node for Authentication"
            c.send(data2.encode())  # 4.Send Request to Client node Number
            data3 = c.recv(1024).decode()# 5. Recieve Client node Number
            
            print(data1,data3)
            
            collaborative(data1,data3)
            #print("user: " + str(data))
            
            
            c.send(data.encode())#6.Ack
            
            print("abey kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

    c.close()
 


import json
import random
import multichain
import hashlib
import socket
from datetime import datetime
hash1=hashlib.sha256(b"Rule").hexdigest()
hash2=hashlib.sha256(b"PolicyContract").hexdigest()
import time
with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/DiasasterService.txt", "r") as file:
    data = json.load(file)
    
############################Client Sent the Request For collaborative Request to DiaseterService##################



with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Rule.json", "r") as file:
    data = json.load(file)

Service1trust=data[-1]["Servicerthreshould"]
#print("Abey Haramiiiiiiiiiiiiiiiiiiiiiiiiiiii",Service1trust)    

with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Policy.json", "r") as file:
    data2 = json.load(file)
CollaborativeService1trust=data2[-1]["CollaborativeServiceTrust"]

with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Rule1.json", "r") as file:
    data3 = json.load(file)
Service2trust=data3[0]["Servicerthreshould"]

with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Policy1.json", "r") as file:
    data4 = json.load(file)
CollaborativeService2trust=data4[-1]["CollaborativeServiceTrust"]

with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/GlobalContract/Rule.json", "r") as file:
    data5 = json.load(file)
GlobalServicetrust=data5[-1]["Servicerthreshould"]

with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/GlobalContract/Policy.json", "r") as file:
    data6 = json.load(file)
GlobalCollaboratveServicetrust=data6[-1]["CollaborativeServiceTrust"]




##########################Step:7 Post this token in the LocalBlockchain###########################################

####Note Humeny Yehan per server chain ko connect kiya hai aur global rule ki authentication stream si kar li hai actual main global 
####chain bhi yahan per call karsaktey they but huney kyoun copy ofblockchain kya hai is liye global hisirf verif verfiy karna hai 

rpcuser = "multichainrpc"
rpcpassword = "J7csxdmUpgeCM39VXLrUFCWvANbYhiK5UQamXADrnhyv"
rpchost = "127.0.0.1"
rpcport = "9540"
chainname = "shahbaz"
mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)
result1 = mc.liststreamkeyitems('GlobalRule','key1',False,1)
##########################################################################################
#print(result1[0]['txid'])
txid1 = mc.create('stream', 'Application', True) # open to all to write


##########################################################################################


print("Security Token Verification on Server side")
###############################Server Verify the Security Verification##########################################	
with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application.txt", "r") as f:
	
	data = f.read()    
	data32 =json.loads(data)
	#print(data32[''])
	    ###Key Noticed result[0] only extract the Blockchain variable such as txid ,confirmation,publisherid not Application data
if (data32['BLockchainGlobalRule-1txid'] == result1[0]['txid'] and data32['BLockchainGlobalRule-1publisherid']==result1[0]['publishers'] ):
         print("Verifcation Ok")



#################################################################################################################

"""
#print(mc.getinfo())
#Agreement = mc.create('stream', 'LocalServiceAgreement', True) # open to all to write
txid1 = mc.publish('LocalServiceAgreement', 'key1', {'json' : {
	        "LocalRuleHash": hash2,
	        "LocalPolicyHash":hash1
	           }}) # JSON data
with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application.txt", "r") as f:
         data1 = f.read()    
         data2 =json.loads(data1)
	    ###Key Noticed result[0] only extract the Blockchain variable such as txid ,confirmation,publisherid not Application data
        data['Hash1'] =data2['LocalRuleHash']
        data['Hash2'] =data2['LocalpolicyHash']
        with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/DiasasterService.txt", "w") as f:
         json.dump(data, f,indent=4)    

        if (data['Hash1']==hash1 and data['Hash2']==hash2):
         print("Service Security Verify")
conn.close()  # close the connection

"""

def collaborative(user,Node):
   with open('Application/Application/Node'+str(Node)+'.json', "r") as f:
    data = f.read()    
    data32 =json.loads(data)
    print("SJJJJJJJJJJJJJJJJJJJ",data32[0]['ServiceTrust'])
    print("CollaborativeServiceCTrust",data32[1]['CollaborativeServiceCTrust'])
    print("Cola",CollaborativeService1trust)
   if (user=="User" and data32[0]['ServiceTrust']>Service1trust and data32[1]['CollaborativeServiceCTrust']>CollaborativeService1trust):
    print("Yes")
    ####Read or access to daiaster managment service data 
    with open('/home/ubuntu/Desktop/Shahbaz_Final_Project/DiasasterService.txt', "r") as f:
     data = f.read()    
    data32 =json.loads(data)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")  

    txid1 = mc.publish('Application', 'key1', {'json' : {
        "Time":current_time,
         "Applicationdata":data32
           }}) # JSON data
    print("Uploaded",txid1)       
    mc.subscribe('Application') # one asset or stream



     
   if (user=="User"):
    print("NO")
  



import socket
import time 


'''
 
def Main():
    host = ""
 
    # reserve a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 5004
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
 
    # put the socket into listening mode
    s.listen(1)
    print("socket is listening")
 
    # a forever loop until client wants to exit
    while True:
       conn, addr = s.accept()
 
       data = conn.recv(1024).decode()####1.Client Send the Agreeement Token 
        
       time.sleep(1)
       if data==result1[0]['txid']:
            # if data is not received break
            print("Txid Verification Ok: " + str(data))
            data="ACK Send Role"
            
            
            conn.send(data.encode())  # send Request to Send role ###########2.Server Send Ack to Client 
            data1 = conn.recv(1024).decode()####3.Recieved Role from CLient Machine 
            
            data2="Send the Node for Authentication"
            conn.send(data2.encode())  # 4.Send Request to Client node Number
            data3 = conn.recv(1024).decode()# 5. Recieve Client node Number
            
            print(data1,data3)
            
            collaborative(data1,data3)
            #print("user: " + str(data))
            
            
            conn.send(data.encode())#6.Ack
            
            time.sleep(2)    
            start_new_thread(threaded, (conn,))
            print("abey kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
 
    s.close()
''' 
def Main():
    host = ""
 
    # reserve a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 5002
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
 
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
 
    # a forever loop until client wants to exit
    while True:
 
        # establish connection with client
        c, addr = s.accept()
 
        # lock acquired by client
        print_lock.acquire()
        print('Connected tommmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm :', addr[0], ':', addr[1])
        print("chutuuuuuuuuuuuuuuuuuuuuuuuuu")
 
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()
 
 
if __name__ == '__main__':
    Main()

