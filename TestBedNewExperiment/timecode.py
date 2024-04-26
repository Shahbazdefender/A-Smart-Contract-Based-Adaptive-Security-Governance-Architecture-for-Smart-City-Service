import json
import random
import multichain
import hashlib
import socket
import time
from datetime import datetime

##################################################################
##Rememberformula 

###1000ms-----------------1s
####600ms------------------1x600/1000  ====0.6Second Delay 


####for throughput 60sec----------------92
####################1 sec-------------92*1/60
##Taken Delay 0.6,0.1,0.06,0.004,0.0015 for(600,120,60,40,15)ms   Thread3 main 0.6 hiSub main Ralhna hai , don't change Serviceload 
##For ExecutionEngine 


#######################################################Execution Engine #######################################
# for 100 take the average value  Do not distrube the setting code  
# for 500 take the average value 
# for 1000 take the average value 
# for 2000 take the average value 
# for 5000 take the average value 

##############################################################################################################


##Add the Service Delay with Increase number of Services For 3 Add 0.06+0.06+0.06 in the position where thread code is written 


##600    0.6ms #####For service 1 delay start with 0.5-0.7 Service 2 1.0-1.5  delay start Servicer 3 2.0-2.4
##120     0.12 ##For service 1 delay start with 0.14-0.15 Service 2 0.24-0.25 delay start Servicer 3 0.45---0.48
##60      0.06 ##For service 1 delay start with 0.08-0.10 Service 2 0.16--0.19 delay start Servicer 3 0.32---0.35
##30      0.03 ##For service 1 delay start with 0.03-0.08 Service 2 0.10--0.15 delay start Servicer 3 0.28---0.32
##1ms      0.0015 ##For service 1 delay start with0.008-0.012 Service 2 0.012--0.018 delay start Servicer 3 0.12---0.18
###one more pint important 60 sec ----100 keys sendkarain but recieve hoeian 98 this is basically throughputformula



####for throughput 60sec----------------92
####################1 sec-------------92*1/60



now = datetime.now()
current_time = now.strftime("%H:%M:%S")  
current_time_seconds = time.time()#now.strftime("%H:%M:%S")     
print(current_time_seconds ) 
time.sleep(5)# for 600ms  mean 0.600second

now2 = datetime.now()
recieve_time = now2.strftime("%H:%M:%S")  

recieve_time_seconds = time.time()#now.strftime("%H:%M:%S") 
###for second conversion
print(recieve_time_seconds ) 
time.sleep(5)
print(recieve_time_seconds - current_time_seconds)






now = datetime.now()
current_time = now.strftime("%H:%M:%S")  
current_time_seconds = time.time()#now.strftime("%H:%M:%S")      
time.sleep(5)# for 600ms  100
now2 = datetime.now()

recieve_time = now2.strftime("%H:%M:%S")  
recieve_time_seconds = time.time()#now.strftime("%H:%M:%S") 
###for milliscond second conversion
 
print((recieve_time_seconds - current_time_seconds)*1000)

sleep=time.sleep(0.7)
Service=(round(random.uniform(0.5,0.6),2))
print(sleep,Service)
a=0.6
b=10
print(sleep+Service)




