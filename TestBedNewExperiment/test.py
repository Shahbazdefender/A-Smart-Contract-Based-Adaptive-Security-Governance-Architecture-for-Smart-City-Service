from threading import Thread
import time
import random 
num=10
list31b=[]
list32b=[]
list33b=[]
def one():
	rpcuser = "multichainrpc"
	rpcpassword = "BQhpwCy7mHLfi3MFaUx4kCHM8zrC6VQoL5i1FCyHD11h"
	rpchost = "127.0.0.1"
	rpcport = "4763"
	chainname = "server"
	list3b=[]
	list2b=[]
	now = datetime.now()
	time.sleep(0.6)
	sleep=0.6  
	current_time = now.strftime("%H:%M:%S")  
	current_time_seconds = time.time() 
	ServiceLoad=random.uniform(0.05,0.07)

#################################################TestBed Timmer################################
	mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)
	result1 = mc.liststreamkeyitems('GlobalRule','key1',False,1)
	print("service Token",result1)
##########################################################################################
#print(result1[0]['txid'])

   

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




#time.sleep(0.12)# for 120ms 500 
#time.sleep(0.06)# for 60ms  1000 
#time.sleep(0.03)# for 30ms  2000 
# time.sleep(0.015)# for 15ms  3000 
	#print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSss",ServiceLoad+sleep)
	time.sleep(ServiceLoad)# for 600ms  100
	mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)

	result2 = mc.liststreamkeyitems('GlobalRule','key1',False,1)       	
	now2 = datetime.now()
	print("Start of 1---------------------------------------------------------------")






	recieve_time = now2.strftime("%H:%M:%S")  
	time.sleep(sleep+ServiceLoad)
	list31b.append(sleep+ServiceLoad)
	recieve_time_seconds = time.time()

	print("agggggggggggggggggggggggggggggggggggggggggggggggffff",list31b)
	#Average=sum(list31b)/len(list31b)

	tuple_ind2 = (str(current_time), str(recieve_time), str(((recieve_time_seconds - current_time_seconds))))


#str_file='/home/ubuntu/Desktop/Shahbaz_Final_Project/TestBedNewExperiment/ServiceLevel(1).txt'
#f=open(str_file,"a")
#f.write(str(tuple_ind2)+'\n')
	print("End of 1---------------------------------------------------------------")


          
def two():
	rpcuser = "multichainrpc"
	rpcpassword = "BQhpwCy7mHLfi3MFaUx4kCHM8zrC6VQoL5i1FCyHD11h"
	rpchost = "127.0.0.1"
	rpcport = "4763"
	chainname = "server"
	list3b=[]
	list2b=[]
	now = datetime.now()
 
 #time.sleep(0.12)# for 120ms 500 
 #time.sleep(0.06)# for 60ms  1000 
 #time.sleep(0.03)# for 30ms  2000 
# time.sleep(0.015)# for 15ms  3000 
	time.sleep(1.2)  

	sleep=(0.6)  

	current_time = now.strftime("%H:%M:%S")  
	current_time_seconds = time.time() 
	ServiceLoad=random.uniform(0.05,0.05)

#################################################TestBed Timmer################################
	mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)
	result1 = mc.liststreamkeyitems('GlobalRule','key1',False,1)
	print(result1)
##########################################################################################
#print(result1[0]['txid'])

   

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

# for 600ms  100       

	mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)

	result2 = mc.liststreamkeyitems('GlobalRule','key1',False,1)       
	now2 = datetime.now()
	print("Start of 2---------------------------------------------------------------")

	txid1 = mc.publish('GlobalRule', 'key1', {'json' : {
"Contract": "GLobal",
"Servicerthreshould":0.1,
"PreviousTrust":0,
"ServiceTrust": 0.0,
"Service Value":0.0,
"Time":current_time

   }}) # JSON data
	mc.subscribe('GlobalRule') # one asset or streamfrom datetime import datetimevurre  
	recieve_time = now2.strftime("%H:%M:%S")  

	time.sleep(sleep+ServiceLoad)
	list31b.append(sleep+ ServiceLoad)
	recieve_time_seconds = time.time()
#print(list3b)
#Average=sum(list32b)/len(list32b)
###this value is in  second to convert in mili *1000 
	tuple_ind2 = (str(current_time), str(recieve_time), str(((recieve_time_seconds - current_time_seconds))))
#str_file='/home/ubuntu/Desktop/Shahbaz_Final_Project/TestBedNewExperiment/ServiceLevel(2).txt'
#f=open(str_file,"a")
#f.write(str(tuple_ind2)+'\n')
	print("End of 2---------------------------------------------------------------")


        


def three():
	rpcuser = "multichainrpc"
	rpcpassword = "BQhpwCy7mHLfi3MFaUx4kCHM8zrC6VQoL5i1FCyHD11h"
	rpchost = "127.0.0.1"
	rpcport = "4763"
	chainname = "server"
	list3b=[]
	list2b=[]
	now = datetime.now()

#time.sleep(0.12)# for 120ms 500 
#time.sleep(0.06)# for 60ms  1000 
#time.sleep(0.03)# for 30ms  2000 
# time.sleep(0.015)# for 15ms  3000 
  
	current_time = now.strftime("%H:%M:%S")  
	current_time_seconds = time.time() 
	time.sleep(5.8)
	sleep=5.8  

	ServiceLoad=random.uniform(0.5,0.8)
	time.sleep(ServiceLoad)# for 600ms  100

#################################################TestBed Timmer################################
	mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)
	result1 = mc.liststreamkeyitems('GlobalRule','key1',False,1)
	print(result1)
##########################################################################################
#print(result1[0]['txid'])

   

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




	mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)
	result2 = mc.liststreamkeyitems('GlobalRule','key1',False,1)

	print("Start of 3---------------------------------------------------------------")

	now2 = datetime.now()
	txid1 = mc.publish('GlobalRule', 'key1', {'json' : {
"Contract": "GLobal",
"Servicerthreshould":0.1,
"PreviousTrust":0,
"ServiceTrust": 0.0,
"Service Value":0.0,
"Time":current_time
   }}) # JSON data
	mc.subscribe('GlobalRule') # one asset or streamfrom datetime import datetimevurre
	txid12 = mc.publish('LocalServiceAgreement', 'key1', {'json' : {
        "TransactionalHash":txid1        
           }}) # JSON data
	recieve_time = now2.strftime("%H:%M:%S")  

	time.sleep(sleep+ServiceLoad)
	recieve_time_seconds = time.time()
	list31b.append(((recieve_time_seconds - current_time_seconds)*1000)+sleep+ ServiceLoad)     
	Average=sum(list31b)/len(list31b)
	tuple_ind2 = (str(current_time), str(recieve_time), str(((recieve_time_seconds - current_time_seconds)*1000)),Average)

	str_file='/home/ubuntu/Desktop/Shahbaz_Final_Project/TestBedNewExperiment/ExecutionContract(3).txt'
	f=open(str_file,"a")
	f.write(str(tuple_ind2)+'\n')
	print("End of 3---------------------------------------------------------------")






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
rpcpassword = "BQhpwCy7mHLfi3MFaUx4kCHM8zrC6VQoL5i1FCyHD11h"
rpchost = "127.0.0.1"
rpcport = "4763"
chainname = "server"
list3b=[]
list2b=[]

#################################################TestBed Timmer################################
now = datetime.now()
#time.sleep(0.6)# for 600ms  100
time.sleep(0.12)# for 120ms 500 
 #time.sleep(0.06)# for 60ms  1000 
 #time.sleep(0.03)# for 30ms  2000 
# time.sleep(0.015)# for 15ms  3000 

current_time = now.strftime("%H:%M:%S")  
current_time_seconds = time.time() 
mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)
result1 = mc.liststreamkeyitems('GlobalRule','key1',False,1)
print(result1)
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
#host = socket.gethostname()  # as both code is running on same pc
#port = 5002# socket server port number

#client_socket = socket.socket()  # instantiate
#client_socket.connect((host, port))  # connect to the server
	message =result1[0]['txid']  # take input    
	print( message)
	while (True):
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
	# print("dssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",file3)

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
		print("Shahbaz",data[4])

	##GlobalPolicy Increase   
		data[-1]["CollaborativeService"] =data[-1]["CollaborativeServiceCTrust"]
		data[-1]["CollaborativeServiceCTrust"] =data[-1]["CollaborativeServiceCTrust"]+0.1

		with open('Application/Application/Node'+str(node)+'.json', "w") as file:
			json.dump(data, file, indent=4)
	 #print("ffffffffffffffffffffffffff",data[0]["LocalRuleHash"],data[1]["LocalpolicyHash"])


	#        client_socket.send(message.encode())  # 1.Send Txid of Blockchain
	#  data = client_socket.recv(2024).decode()  # 2.receive Ack From Server 
	#   print('Received-0 from server: ' + data+''+str(node))  # show in terminal


	 
	#      client_socket.send(message1.encode())  # 3.send Role to Server  
	#     data = client_socket.recv(2024).decode()  # 4.Receivied Ack 
	#  print('Received-1 from server: ' + data+''+str(node))  # show in terminal


	#    client_socket.send(message2.encode())  # 5.Send Node number forSearching 

	#   data = client_socket.recv(2024).decode()  # 6. receive Ack
	#    print('Received-2 from server: ' + data+''+str(node))  # show in terminal
		p1 = Thread(target = one)
		p2 = Thread(target = two)
		p3 = Thread(target = three)

		ServiceLoad=random.uniform(0.3,0.5)

		p1.start()
		p1.join()
		time.sleep(6.6)
		sleep=6.6
		p2.start()
		time.sleep(1.2)
		p3.start()
		
		p2.join()
		p3.join()
		now2 = datetime.now()
		recieve_time = now2.strftime("%H:%M:%S")  
		time.sleep(sleep+ServiceLoad)
		list31b.append(sleep+ServiceLoad)
		recieve_time_seconds = time.time()



		tuple_ind2 = (str(current_time), str(recieve_time), str(((recieve_time_seconds - current_time_seconds))))
	#Access Formula explain in File# 

		str_file='/home/ubuntu/Desktop/Shahbaz_Final_Project/TestBedNewExperiment/Throughput.txt'
		f=open(str_file,"a")
		f.write(str(tuple_ind2)+'\n')
	      ##################################We take This snapshot as throughput of system(End)#######################################
		
		
		node=node+1
	#      print(node,"asdsddsdasadsdasdasdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddds")
		if node==50:
		   node=1
	   
#    client_socket.close()  # close the connection
		s = socket.socket()        

# Define the port on which you want to connect
		port = 12345               

# connect to the server on local computer
		s.connect(('127.0.0.1', port))

# receive data from the server and decoding to get the string.
		print (s.recv(1024).decode())


if __name__ == '__main__':
    client_program()




