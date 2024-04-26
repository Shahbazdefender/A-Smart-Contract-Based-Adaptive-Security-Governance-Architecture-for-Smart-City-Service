import json
import os
import hashlib
import multichain
from datetime import datetime
data1=[]
data2=[]
data3=[]
data4=[]
#######################################data1, data2.....added accordinlinh###############################
def encode_json(data):
    return json.dumps(data, indent=4)

def decode_json(json_data):
    return json.loads(json_data)

# Check if the file exists, and if so, read the existing data
if os.path.exists("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Rule.json"):
    with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Rule.json", "r") as f:
        data1= decode_json(f.read())
        print('Yes')
        
else:
    SensorContract1 = []
    


if os.path.exists("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Policy.json"):
    with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Policy.json", "r") as f:
        data2 = decode_json(f.read())
        

if os.path.exists("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Rule1.json"):
    with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Rule1.json", "r") as f:
        data3= decode_json(f.read())
        print('Yes')
        
else:
    SensorContract1 = []
    


if os.path.exists("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Policy1.json"):
    with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Policy1.json", "r") as f:
        data4 = decode_json(f.read())
        

else:
   ApplicationContract2=[]
#########################################Hash values of Rule and Policie##############################################
hash1=hashlib.sha256(b"Rule").hexdigest()
hash2=hashlib.sha256(b"PolicyContract").hexdigest()
# Input the new data
##################################Adaptive Engine Module################################################################
def LocalAdaptiveEngine():

	while True:
	    breakstatement = input("Enter commit For Rule ad : ")
	    if not breakstatement=="commit":
	        break
	    now = datetime.now()
	    current_time = now.strftime("%H:%M:%S")   
	    data1.append({
	        "Serviceid":"Service1",
	        "Contract": "Local",
	        "LocalRuleHash":hash1,
	        "Servicerthreshould":0.0	,
	        "PreviousTrust":0,
	        "ServiceTrust": 0.0,
	        "Role":"Admin",
	        "Authorization":["Create","Add","delete","Display"],
                "Role1":"User",
	        "Authorization":["display"],
	         "Time":current_time        
  	        
	           })
    
    
	    data2.append({
	        "LocalpolicyHash":hash2,
	        "Subject":"Service1",
	        "object":"Service2",
	        "CollaborativeServiceTrust":0.0,
	        "CollaborativeServicePTrust":0.0,
	        "CollaborativeServiceCTrust":0.0,
	        "Time":current_time         
	    })


	    data3.append({
	        "Serviceid":"Service2",
	        "Contract": "Local",
	        "LocalRuleHash":hash1,
	        "Servicerthreshould":0.0,
	        "PreviousTrust":0,
	        "ServiceTrust": 0.0,
	        "Role":"Admin",
	        "Authorization":["Create","Add","delete","Display"],
                "Role1":"User",
	        "Authorization":["display"],
  	        "Time":current_time
	           })
    
    
	    data4.append({
	        "LocalpolicyHash":hash2,
	        "Subject":"Service1",
	        "object":"Service2",
	        "CollaborativeServiceTrust":0.0,
	        "CollaborativeServicePTrust":0.0,
	        "CollaborativeServiceCTrust":0.0,
	        "Time":current_time         
	    })

######################Data1, data3 are represent the Rule of Service1 and Service2,Data2 and Data4 are the policies with each other

	    # Encode the data as a JSON string
	json_data1 = encode_json(data1)
	#print("Encoded JSON data:")
	#print(json_data1)

	json_data2 = encode_json(data2)
	#print("Encoded JSON data:")
	#print(json_data2)
	json_data3 = encode_json(data3)
	#print("Encoded JSON data:")
	#print(json_data1)
	json_data4 = encode_json(data4)
	#print("Encoded JSON data:")
	#print(json_data2)

	# Store the JSON data in the file
	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Rule.json", "w") as f:
	    f.write(json_data1)

	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Policy.json", "w") as f:
	    f.write(json_data2)
	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Rule1.json", "w") as f:
	    f.write(json_data3)
	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Policy1.json", "w") as f:
	    f.write(json_data4)




	# Read the JSON data from the file
	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Rule.json", "r") as f:
	    decoded_data1 = decode_json(f.read())
	#print("\nDecoded data:")
	#print(decoded_data1)

	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Policy.json", "r") as f:
	    decoded_data2 = decode_json(f.read())
	#print("\nDecoded data:")
	#print(decoded_data2)

	#######################################Store rule in Multichain Application-1################
	rpcuser = "multichainrpc"
	rpcpassword = "3yCd7Ah7KC9rAUHrKNM694Lpq15dAPT7cJ6sgvPUKg9y"
	rpchost = "127.0.0.1"
	rpcport = "2652"
	chainname = "server"

	mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)

	#print(mc.getinfo())
	txid1 = mc.create('stream', 'Localrule', True) # open to all to write
	
	#result = mc.getstreaminfo('Localrule')
	#result = mc.liststreams() # all streams


	#result = mc.liststreams('LocalRule') # one specific stream
	txid1 = mc.publish('LocalRule', 'key1', {'json' : {
	        "Serviceid":"Service1",
	        "Contract": "Local",
	        "LocalRuleHash":hash1,
	        "Servicerthreshould":0.1,
	        "PreviousTrust":0,
	        "ServiceTrust": 0.0,
	        "Service Value":0.0,
	        "Time":current_time         
	           }}) # JSON data
	mc.subscribe('LocalRule') 


	# one asset or stream
	#result = mc.liststreamitems('LocalRule')
	#result = mc.liststreamkeys('LocalRule') # all keys in stream
	#result = mc.liststreamkeys('LocalRule', 'key1')
	#result = mc.getstreamkeysummary('LocalRule', 'key1', 'jsonobjectmerge')
	result = mc.liststreamkeyitems('LocalRule', 'key1',False,1)

	#print(result)
	txid12 = mc.publish('LocalServiceAgreement', 'key1', {'json' : {
	        "TransactionalHash":txid1        
	           }}) # JSON data
	mc.subscribe('LocalServiceAgreement') 


	#######################################Store policies in Multichain################

	txid2 = mc.create('stream', 'LocalPolicies', True) # open to all to write

	#result = mc.getstreaminfo('Localrule')
	#result = mc.liststreams() # all streams


	#result = mc.liststreams('LocalRule') # one specific stream
	txid2 = mc.publish('LocalPolicies', 'key1', {'json' : {
	        "Serviceid":"Service1",  
	        "LocalpolicyHash":hash2,
	        "Subject":"Application",
	        "object":"School",
	        "CollaborativeServiceTrust":0.1,
	        "CollaborativeServicePTrust":0.0,
	        "CollaborativeServiceCTrust":0.0,
	        	        "Time":current_time                  
	    }}) # JSON data
	mc.subscribe('LocalPolicies') # one asset or stream
	#result = mc.liststreamitems('LocalRule')
	#result = mc.liststreamkeys('LocalRule') # all keys in stream
	#result = mc.liststreamkeys('LocalRule', 'key1')

	###################################SAmple Code inorder to Search the ItemFrom the Blockchain#######
	import json
	result1 = mc.liststreamkeyitems('LocalPolicies', 'key1',False,1)

	#print(result)


	#my_dict = {}  # create an empty dictionary

	# add key-value pairs to the dictionary

	#my_dict['txid'] = result[0]['txid']
	#my_dict['publisherid'] = result[0]['publishers']
	#print(my_dict)  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

	########################Adaptive Security Engine Recieve Security Tokens for Rule and Policy -1##############################
	
	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application.txt", "r") as f:
	    print("Security Contract For Service1")
	    data = f.read()    
	    data32 =json.loads(data)
	    ###Key Noticed result[0] only extract the Blockchain variable such as txid ,confirmation,publisherid not Application data
	data32['BLockchainLocalRule-1txid'] = result[0]['txid']
	data32['BLockchainLocalRule-1publisherid'] = result[0]['publishers']
	data32['BLockchainLocalPolicies-1txid'] = result1[0]['txid']
	data32['BLockchainLocalPolicies-1publisherid'] = result1[0]['publishers']
	data32['Contract'] = data1[0]['Contract']
	print(data32['BLockchainLocalRule-1txid'] )
	print(data32['BLockchainLocalRule-1publisherid'])
#	data32.update(data2[-1])
#	data32.update(data1[-1])
	print(data2[-1])

	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application.txt", 'w') as f:
	    json.dump(data32, f,indent=4)    


	#print(result[0]['txid'])
	 # 10 most recent items

####################################################################################################################################
	#######################################Store rule in Multichain Service-2(Local Contract Deployment Application)################
	rpcuser = "multichainrpc"
	rpcpassword = "2PZRJWQgycsQU6W6wKFJtPMjXcaXbdMqAu4QjmaDh6ZT"
	rpchost = "127.0.0.1"
	rpcport = "4780"
	chainname = "shahbaz"

	mc1=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)

	#print(mc.getinfo())
	txid1 = mc1.create('stream', 'Localrule', True) # open to all to write
	Agreement = mc1.create('stream', 'LocalServiceAgreement', True) # open to all to write

	#result = mc.getstreaminfo('Localrule')
	#result = mc.liststreams() # all streams


	#result = mc.liststreams('LocalRule') # one specific stream
	txid1 = mc1.publish('LocalRule', 'key1', {'json' : {
	        "Serviceid":"Service2",
	        "Contract": "Local",
	        "LocalRuleHash":hash1,
	        "Servicerthreshould":0.1,
	        "PreviousTrust":0,
	        "ServiceTrust": 0.0,
	        "Service Value":0.0,
	        "Time":current_time         
	           }}) # JSON data
	mc1.subscribe('LocalRule') 
	txid12 = mc1.publish('LocalServiceAgreement', 'key1', {'json' : {
	        "TransactionalHash":txid1        
	           }}) # JSON data
	mc1.subscribe('LocalServiceAgreement') 


	# one asset or stream
	#result = mc.liststreamitems('LocalRule')
	#result = mc.liststreamkeys('LocalRule') # all keys in stream
	#result = mc.liststreamkeys('LocalRule', 'key1')
	#result = mc.getstreamkeysummary('LocalRule', 'key1', 'jsonobjectmerge')
	result2 = mc.liststreamkeyitems('LocalRule', 'key1',False,1)

	#print(result)


	#######################################Store policies in Multichain################

	txid2 = mc.create('stream', 'LocalPolicies', True) # open to all to write

	#result = mc.getstreaminfo('Localrule')
	#result = mc.liststreams() # all streams


	#result = mc.liststreams('LocalRule') # one specific stream
	txid2 = mc.publish('LocalPolicies', 'key1', {'json' : {
	        "Serviceid":"Service2",  
	        "LocalpolicyHash":hash2,
	        "Subject":"Application",
	        "object":"School",
	        "CollaborativeServiceTrust":0.1,
	        "CollaborativeServicePTrust":0.0,
	        "CollaborativeServiceCTrust":0.0,
	        	        "Time":current_time                  
	    }}) # JSON data
	mc.subscribe('LocalPolicies') # one asset or stream
	#result = mc.liststreamitems('LocalRule')
	#result = mc.liststreamkeys('LocalRule') # all keys in stream
	#result = mc.liststreamkeys('LocalRule', 'key1')

	###################################SAmple Code inorder to Search the ItemFrom the Blockchain#######
	import json
	result3 = mc.liststreamkeyitems('LocalPolicies', 'key1',False,1)

	#print(result)


	#my_dict = {}  # create an empty dictionary

	# add key-value pairs to the dictionary

	#my_dict['txid'] = result[0]['txid']
	#my_dict['publisherid'] = result[0]['publishers']
	#print(my_dict)  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

	########################Adaptive Security Engine Recieve Security Tokens for Rule and Policy -2##############################
	
	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application2.txt", "r") as f:
	    print("Security Contract For Service2")
	    data = f.read()    
	    data32 =json.loads(data)
	    ###Key Noticed result[0] only extract the Blockchain variable such as txid ,confirmation,publisherid not Application data
	data32['BLockchainLocalRule-2txid'] = result2[0]['txid']
	data32['BLockchainLocalRule-2publisherid'] = result2[0]['publishers']
	data32['BLockchainLocalPolicies-2txid'] = result3[0]['txid']
	data32['BLockchainLocalPolicies-2publisherid'] = result3[0]['publishers']
	data32['Contract'] = data1[0]['Contract']
#	data32.update(data2[-1])
#	data32.update(data1[-1])

	with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application2.txt", 'w') as f:
	    json.dump(data32, f,indent=4)    


	#print(result[0]['txid'])
	 # 10 most recent items

##################################################################################### 


def DisastermanagentService() :
 LocalAdaptiveEngine() 

#######################################Server of Diasater Managemet Service#########################################################
DisastermanagentService()
