import json
import random
import multichain

#######################Application-1 Blockchain Hai#####################################################
rpcuser = "multichainrpc"
rpcpassword = "J7csxdmUpgeCM39VXLrUFCWvANbYhiK5UQamXADrnhyv"
rpchost = "127.0.0.1"
rpcport = "9540"
chainname = "shahbaz"

mc=multichain.MultiChainClient(rpchost, rpcport, rpcuser, rpcpassword)

result = mc.liststreamkeyitems('LocalRule', 'key1',False,1)
result2 = mc.liststreamkeyitems('LocalPolicies', 'key1',False,1)
result3 = mc.liststreamkeyitems('GlobalRule', 'key1',False,1)
result4 = mc.liststreamkeyitems('GlobalPolicies', 'key1',False,1)
print("Chutia",result4[0]['txid'])
print("Chutia",result3[0]['txid'])

print("Chutia",result[0]['txid'])
print("Chutia",result2[0]['txid'])
#################################################Multichain LocalConnection LocalRule ######


with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Rule.json", "r") as file:
    data = json.load(file)


with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/LocalContract/Policy.json", "r") as file:
    data2 = json.load(file)

latest_data1 = data[-1]
latest_data2 = data2[-1]


#################################################Multichain LocalConnection GlobalRule ######

with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/GlobalContract/Rule.json", "r") as file:
    data3 = json.load(file)


with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/GlobalContract/Policy.json", "r") as file:
    data4 = json.load(file)

latest_data3 = data3[-1]
latest_data4 = data4[-1]
concatenated_data2 = [latest_data1,latest_data2,latest_data3, latest_data4]
"""
####################(Load LocalRule Create Loop to Create 100 Nodes Data)#################################
for i in range (100):

     file2='/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application/Node'+str(i)+'.json'
     with open(file2,'w') as file1:
  
       #List23=y.keys()
       #Apllicationdata={"Ambulance":[{i:"" for i in List23}]}
       json.dump(concatenated_data2,file1,indent=4)
       file1.close()

"""
def GLobalAdaptiveEngine():
  with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application.txt", "r") as f:
    print("Application1 Transaport Start")
    Applicationdata = f.read()    
    Applicationdata1 =json.loads(Applicationdata)
    print(result3[0]['txid'],Applicationdata1['BLockchainGlobalRuletxid'])
    #####First Step Blockchain Verification 
  if (result3[0]['txid']==Applicationdata1['BLockchainGlobalRuletxid'] and result4[0]['publishers']==Applicationdata1['BLockchainGlobalPoliciestxid'] )  :
      print("ZAlil1")
    #####Second Step RuleVoilationCheck
    
def LocalAdaptiveEngine(i,nodes,a,b):
 with open("/home/ubuntu/Desktop/Shahbaz_Final_Project/Application/Application.txt", "r") as f:
    print("Application1 Transaport Start")
    Applicationdata = f.read()    
    Applicationdata1 =json.loads(Applicationdata)
 #print("Abey Kuttey ",Applicationdata1["LocalRuleHash"])
 print(data[-1]['CollaborativeServiceCTrust'])
 print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkk",Applicationdata1['BLockchainLocalRuletxid'],result[0]['txid'],Applicationdata1['BLockchainLocalRulepublisherid'],result[0]['publishers'])
    ##############Verification Start ###########################
 if (Applicationdata1['BLockchainLocalRuletxid']==result[0]['txid'] and Applicationdata1['BLockchainLocalRulepublisherid']==result[0]['publishers'] and Applicationdata1['CollaborativeServiceTrust']<data[-1]['CollaborativeServiceCTrust']):
     #######After Local Verification Global Adaptive Engine Call ######### Check Only Local and Global Rule and Policiy Voilation 
     
    GLobalAdaptiveEngine() 
    print("Yes")
     #####"Service 2 ki data access hoga "
    print(Applicationdata1['Subject'])
    print(Applicationdata1['object']) 
    objectname=Applicationdata1['object']           
    with open("Application/School.txt", "r") as f:
      print("Application2 School Start")
      Applicationdata = f.read() 
      Applicationdata1 =json.loads(Applicationdata)
      print(Applicationdata1["AlertMessage"]) 
      

###############################################################################################
Sensorvalue=[i for i in range (10)]
sensorvalue=random.choice(Sensorvalue)
print(sensorvalue)
########################################
w=0
for i in range (10):
     w=w+1   
     application=["Application"]
     applications=random.choice(application)
     node=[str(i) for i in range (100)]    
     nodes=random.choice(node)
     print("AOye hey",w,applications)
     with open('Application/'+applications+'/Node'+str(w)+'.json', "r") as file:
      data = json.load(file)
#     This Line Just For Checking Purpose 
      print(data[0])
      print("/n")
      print(data[1])
      print("/n")
      print(data[-2])
      print("/n")
      print(data[-1])
      if "Contract" in data[-2]:
       print("Shahbaz2")
#####Cases for Message Printing##########################################
    ##Local Values Increase    
       data[0]["PreviousTrust"] =data[0]["ServiceTrust"]
       data[0]["ServiceTrust"] =data[0]["ServiceTrust"]+0.01

       data[1]["CollaborativeService"] =data[1]["CollaborativeServiceCTrust"]
       data[1]["CollaborativeServiceCTrust"] =data[1]["CollaborativeServiceCTrust"]+0.1
       
    ##GlobalContext Increase    
       data[-2]["PreviousTrust"] =data[-2]["ServiceTrust"]
       data[-2]["ServiceTrust"] =data[-2]["ServiceTrust"]+0.01
       #print("Shahbaz",data[-2])
   
      
       data[-1]["CollaborativeService"] =data[-1]["CollaborativeServiceCTrust"]
       data[-1]["CollaborativeServiceCTrust"] =data[-1]["CollaborativeServiceCTrust"]+0.1

     with open('Application/'+applications+'/Node'+str(w)+'.json', "w") as file:
       json.dump(data, file, indent=4)
       print("ffffffffffffffffffffffffff",data[0]["LocalRuleHash"],data[1]["LocalpolicyHash"])
     LocalAdaptiveEngine(w,sensorvalue,data[0]["LocalRuleHash"],data[1]["LocalpolicyHash"])  
 


######################################

# Update the value of the key "key1"
# Write the updated data back to the file


#################Case For Push Messsage######################################################

