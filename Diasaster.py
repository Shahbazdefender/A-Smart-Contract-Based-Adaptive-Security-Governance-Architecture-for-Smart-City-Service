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
print("Abey Haramiiiiiiiiiiiiiiiiiiiiiiiiiiii",Service1trust)    

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




##########################Step:7 Post this token in the LocalBlockchain(Application-1)#########################################

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

def server_program():
    # get the hostname
    
    host = socket.gethostname()
    port = 5002  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        
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

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()

