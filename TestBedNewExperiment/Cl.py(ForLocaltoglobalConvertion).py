import json
import random
import multichain
import hashlib
import socket
import time
from datetime import datetime


hash1=hashlib.sha256(b"Rule").hexdigest()
hash2=hashlib.sha256(b"PolicyContract").hexdigest()

with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/DiasasterService.txt", "r") as file:
    data = json.load(file)
    
#################################################Service-2 Request #####################################################


###############################Agent first Fetch the Txid from the GlobalChain####################################

#########Local Blockchain Verfication ##############################
rpcuser = "multichainrpc"
rpcpassword = "2PZRJWQgycsQU6W6wKFJtPMjXcaXbdMqAu4QjmaDh6ZT"
rpchost = "127.0.0.1"
rpcport = "4780"
chainname = "shahbaz"
list3b=[]
list2b=[]

#################################################TestBed Timmer################################
now = datetime.now()
time.sleep(0.06)# for 600ms  100
 #time.sleep(0.12)# for 120ms 500 
 #time.sleep(0.06)# for 60ms  1000 
 #time.sleep(0.03)# for 30ms  2000 
# time.sleep(0.015)# for 15ms  3000 

current_time = now.strftime("%H:%M:%S")  
current_time_seconds = time.time() 
mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)
result1 = mc.liststreamkeyitems('GlobalRule','key1',False,1)
##########################################################################################
#print(result1[0]['txid'])

now2 = datetime.now()
recieve_time = now2.strftime("%H:%M:%S")  
recieve_time_seconds = time.time()
list3b.append(((recieve_time_seconds - current_time_seconds)))
tuple_ind2 = (str(current_time), str(recieve_time), str(((recieve_time_seconds - current_time_seconds))))
str_file='/home/ubuntu/Desktop/Shahbaz_Final_Project/TestBedNewExperiment/exp1.txt'
f=open(str_file,"a")
f.write(str(tuple_ind2)+'\n')
   

###########################################################################################################
print("Security Token Verification on Client side with Global Adaptive Agent")
###############################Server Verify the Security Verification##########################################	
with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application2.txt", "r") as f:
	
	data = f.read()    
	data32 =json.loads(data)
	#print(data32[''])
	    ###Key Noticed result[0] only extract the Blockchain variable such as txid ,confirmation,publisherid not Application data
if (data32['BLockchainGlobalRule-2txid'] == result1[0]['txid'] and data32['BLockchainGlobalRule-2publisherid']==result1[0]['publishers'] ):
         print("Verifcation Ok")



#################################################################################################################

########################################################Local Portion Hai ###############################################################

with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Rule.json", "r") as file:
    data = json.load(file)


with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Policy.json", "r") as file:
    data2 = json.load(file)
    
with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Rule1.json", "r") as file:
    data3 = json.load(file)


with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Policy1.json", "r") as file:
    data4 = json.load(file)
    

latest_data1 = data[-1]
latest_data2 = data2[-1]
latest_data3 = data3[-1]
latest_data4 = data4[-1]

##########################################################Globa######################################################

with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/GlobalContract/Rule.json", "r") as file:
    data5 = json.load(file)


with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/GlobalContract/Policy.json", "r") as file:
    data6 = json.load(file)

latest_data5 = data5[-1]
latest_data6 = data6[-1]
concatenated_data2 = [latest_data1,latest_data2,latest_data3, latest_data4, latest_data5, latest_data6]


################################################Adapbtibility of Rules and Policies #########################################
####################(Load LocalRule Create Loop to Create 100 Nodes Data)#################################
"""
for i in range (100):

     file2='/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application/Node'+str(i)+'.json'
     with open(file2,'w') as file1:
  
       #List23=y.keys()
       #Apllicationdata={"Ambulance":[{i:"" for i in List23}]}
       json.dump(concatenated_data2,file1,indent=4)
       file1.close()
       """
#######################################################################################################################
def client_program():
    node=1
    host = socket.gethostname()  # as both code is running on same pc
    port = 5005  # socket server port number
    
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    message =result1[0]['txid']  # take input    
    while message.lower().strip() != 'bye':
     #################################Rule add trust Service-1###################################   
#################################################TestBed Timmer################################
        now = datetime.now()
        
 #time.sleep(0.12)# for 120ms 500 
 #time.sleep(0.06)# for 60ms  1000 
 #time.sleep(0.03)# for 30ms  2000 
# time.sleep(0.015)# for 15ms  3000 

        current_time = now.strftime("%H:%M:%S")  
        current_time_seconds = time.time() 
        time.sleep(0.12)# for 600ms  100
        mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)
        result2 = mc.liststreamkeyitems('GlobalRule','key1',False,1)
##########################################################################################
#print(result1[0]['txid'])

        with open('Application/Application/Node'+str(node)+'.json', "r") as file:
         data = json.load(file)
        data[0]["PreviousTrust"] =data[0]["ServiceTrust"]
        data[0]["ServiceTrust"] =data[0]["ServiceTrust"]+0.01
        #print('Application/Application/Node'+str(node)+'.json' ,data[0]["ServiceTrust"],data[0]["ServiceTrust"]+0.01)

        data[1]["CollaborativeService"] =data[1]["CollaborativeServiceCTrust"]
        data[1]["CollaborativeServiceCTrust"] =data[1]["CollaborativeServiceCTrust"]+0.1
       
    ##GlobalContext Increase   
        print(data[5]) 
        data[4]["PreviousTrust"] =data[4]["ServiceTrust"]
        data[4]["ServiceTrust"] =data[4]["ServiceTrust"]+0.01
       #print("Shahbaz",data[4])
   
      ##GlobalPolicy Increase   
        data[-1]["CollaborativeService"] =data[-1]["CollaborativeServiceCTrust"]
        data[-1]["CollaborativeServiceCTrust"] =data[-1]["CollaborativeServiceCTrust"]+0.1

        with open('Application/Application/Node'+str(node)+'.json', "w") as file:
         json.dump(data, file, indent=4)
         #print("ffffffffffffffffffffffffff",data[0]["LocalRuleHash"],data[1]["LocalpolicyHash"])
        
        
        client_socket.send(message.encode())  # 1.Send Txid of Blockchain
        data = client_socket.recv(2024).decode()  # 2.receive Ack From Server 
        print('Received-0 from server: ' + data+''+str(node))  # show in terminal
        
        
        Role=["User","Admin"]
        message1 =random.choice(Role)
        
        client_socket.send(message1.encode())  # 3.send Role to Server  
        data = client_socket.recv(2024).decode()  # 4.Receivied Ack 
        print('Received-1 from server: ' + data+''+str(node))  # show in terminal
        
        message2 =str(node)
        client_socket.send(message2.encode())  # 5.Send Node number forSearching 
        
        time.sleep(1)
        data = client_socket.recv(2024).decode()  # 6. receive Ack
        print('Received-2 from server: ' + data+''+str(node))  # show in terminal
        
        now2 = datetime.now()
#        txid1 = mc.publish('GlobalRule', 'key1', {'json' : {
 #       "Contract": "GLobal",
  #      "Servicerthreshould":0.1,
   #     "PreviousTrust":0,
    #    "ServiceTrust": 0.0,
     #   "Service Value":0.0,
      #  "Time":current_time

       #    }}) # JSON data
        #mc.subscribe('GlobalRule') # one asset or streamfrom datetime import datetimevurre

        
        
        
        
        node=node+1
        if node==10:
           node=1
           
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

