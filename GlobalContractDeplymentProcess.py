import json
import os
import hashlib
import multichain
import time 
from datetime import datetime


data1=[]
data2=[]

def encode_json(data):
    return json.dumps(data, indent=4)

def decode_json(json_data):
    return json.loads(json_data)

# Check if the file exists, and if so, read the existing data
if os.path.exists("/home/ubuntu/Desktop/Shahbaz_Final_Project/GlobalContract/Rule.json"):
    with open("GlobalContract/Rule.json", "r") as f:
        data1= decode_json(f.read())
        
else:
    SensorContract1 = []
    


if os.path.exists("/home/ubuntu/Desktop/Shahbaz_Final_Project/GlobalContract/Policy.json"):
    with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/GlobalContract/Policy.json", "r") as f:
        data2 = decode_json(f.read())
        
else:
   ApplicationContract2=[]

hash1=hashlib.sha256(b"Rule").hexdigest()
hash2=hashlib.sha256(b"PolicyContract").hexdigest()
# Input the new data

def GlobalAuthorizedUnit():


	while True:
	    breakstatement = input("Enter the Sensor Threshould: ")
	    if not breakstatement=="commit":
	        break
    
	    now = datetime.now()
	    current_time = now.strftime("%H:%M:%S")  

	    data1.append({
        "Contract": "Global",
        "GlobalRuleHash":hash1,
        "Servicerthreshould":0.0,
        "PreviousTrust":0,
        "ServiceTrust": 0.0,
        "Time":current_time
           })
    
    
	    data2.append({
        "GlobalpolicyHash":hash2,
        "Subject":"Service1",
        "object":"Service2",
        "CollaborativeServiceTrust":0.0,
        "CollaborativeServicePTrust":0.0,
        "CollaborativeServiceCTrust":0.0,
        "Time":current_time
                 
    })


    # Encode the data as a JSON string
	json_data1 = encode_json(data1)
#print("Encoded JSON data:")
#print(json_data1)

	json_data2 = encode_json(data2)
#print("Encoded JSON data:")
#print(json_data2)

# Store the JSON data in the file
	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/GlobalContract/Rule.json", "w") as f:
	    f.write(json_data1)

	with open("GlobalContract/Policy.json", "w") as f:
	    f.write(json_data2)

# Read the JSON data from the file
	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/GlobalContract/Rule.json", "r") as f:
	    decoded_data1 = decode_json(f.read())
#print("\nDecoded data:")
#print(decoded_data1)

	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/GlobalContract/Policy.json", "r") as f:
	    decoded_data2 = decode_json(f.read())
#print("\nDecoded data:")
#print(decoded_data2)

#######################################Store rule in Multichain(Global Administration Application)#############
	rpcuser = "multichainrpc"
	rpcpassword = "BQhpwCy7mHLfi3MFaUx4kCHM8zrC6VQoL5i1FCyHD11h"
	rpchost = "127.0.0.1"
	rpcport = "4763"
	chainname = "server"

	mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)

#print(mc.getinfo())
	txid1 = mc.create('stream', 'GlobalRule', True) # open to all to write

#result = mc.getstreaminfo('Localrule')
#result = mc.liststreams() # all streams


#result = mc.liststreams('LocalRule') # one specific stream
	txid1 = mc.publish('GlobalRule', 'key1', {'json' : {
        "Contract": "GLobal",
        "GlobalRuleHash":hash1,
        "Servicerthreshould":0.1,
        "PreviousTrust":0,
        "ServiceTrust": 0.0,
        "Service Value":0.0,
        "Time":current_time

           }}) # JSON data
	mc.subscribe('GlobalRule') # one asset or streamfrom datetime import datetimevurre
#result = mc.liststreamitems('LocalRule')
	result = mc.liststreamkeyitems('GlobalRule', 'key1',False,1)
#	print(result)
#result = mc.liststreamkeys('LocalRule') # all keys in stream
#result = mc.liststreamkeys('LocalRule', 'key1')
#result = mc.getstreamkeysummary('GlobalRule', 'key1', 'jsonobjectmerge')
#print(result)


#######################################Store policies in Multichain################

	txid2 = mc.create('stream', 'GlobalPolicies', True) # open to all to write

#result = mc.getstreaminfo('Localrule')
#result = mc.liststreams() # all streams
        

#result = mc.liststreams('LocalRule') # one specific stream
	txid2 = mc.publish('GlobalPolicies', 'key1', {'json' : {
        "GlobalpolicyHash":hash2,
        "Subject":"Application",
        "object":"School",
        "CollaborativeServiceTrust":0.1,
        "CollaborativeServicePTrust":0.0,
        "CollaborativeServiceCTrust":0.0,
        "Time":current_time
         
    }}) # JSON data
	mc.subscribe('GlobalPolicies') # one asset or stream
#result = mc.liststreamitems('GlobalPolicies')
#result = mc.liststreamkeys('LocalRule') # all keys in stream
#result = mc.liststreamkeys('LocalRule', 'key1')

###################################SAmple Code inorder to Search the ItemFrom the Blockchain#######
	import json
	result1 = mc.liststreamkeyitems('GlobalPolicies', 'key1',False,1)
#print(result)
	print(result1[0]['txid'])

#my_dict = {}  # create an empty dictionary

# add key-value pairs to the dictionary

#my_dict['txid'] = result[0]['txid']
#my_dict['publisherid'] = result[0]['publishers']
#print(my_dict)  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

########################Security Contract Deployment Proceess ##############################
	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application.txt", "r") as f:
	  #  print("Application1 Transaport Start")
	    data = f.read()    
	    data32 =json.loads(data)
	data32['BLockchainGlobalRule-1txid'] = result[0]['txid']
	data32['BLockchainGlobalRule-1publisherid'] = result[0]['publishers']
	data32['BLockchainGlobalPolicies-1txid'] = result1[0]['txid']
	data32['BLockchainGlobalPolicies-1publisherid'] = result1[0]['publishers']
	data32['GContract'] = data1[0]['Contract']
	#data32.update(data2[-1])
	#data32.update(data1[-1])

	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application.txt", 'w') as f:
	    json.dump(data32, f,indent=4)    


#print(result[0]['txid'])
 # 10 most recent items
###################################################################################################### 
	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application2.txt", "r") as f:
	    print("Application1 Transaport Start")
	    data = f.read()    
	    data32 =json.loads(data)
	data32['BLockchainGlobalRule-2txid'] = result[0]['txid']
	data32['BLockchainGlobalRule-2publisherid'] = result[0]['publishers']
	data32['BLockchainGlobalPolicies-2txid'] = result1[0]['txid']
	data32['BLockchainGlobalPolicies-2publisherid'] = result1[0]['publishers']
	data32['GContract'] = data1[0]['Contract']
	print(data32['BLockchainGlobalRule-2txid'])
	#data32.update(data2[-1])
	#data32.update(data1[-1])

	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application2.txt", 'w') as f:
	    json.dump(data32, f,indent=4)    


#print(result[0]['txid'])
 # 10 most recent items
 
#####################################################################################  
 

 
GlobalAuthorizedUnit()
