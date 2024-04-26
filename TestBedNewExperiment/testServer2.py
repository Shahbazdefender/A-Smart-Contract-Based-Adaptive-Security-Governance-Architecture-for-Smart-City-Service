import json
import random
import multichain
import hashlib
import socket
import time
from datetime import datetime

import socket            
 
# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 1365               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    

now = datetime.now()

current_time = now.strftime("%H:%M:%S")  
current_time_seconds = time.time() 

print ("socket is listening")           
 
# a forever loop until we interrupt it or
# an error occurs
while True:
 
# Establish connection with client.
	c, addr = s.accept()    
	now2 = datetime.now()
	recieve_time = now2.strftime("%H:%M:%S")  

	recieve_time_seconds = time.time()



 
	print ('Got connection from', addr )
 
	tuple_ind2 = (str(current_time), str(recieve_time), str(((recieve_time_seconds - current_time_seconds)*1000)))
#Access Formula explain in File# 
          
	str_file='/home/ubuntu/Desktop/Shahbaz_Final_Project/TestBedNewExperiment/Request_Response.txt'
	f=open(str_file,"a")
	f.write(str(tuple_ind2)+'\n')
	current_time=recieve_time
	current_time_seconds=recieve_time_seconds
  # send a thank you message to the client. encoding to send byte type.
	c.send('Thank you for connecting'.encode())

# Close the connection with the client
	c.close()

  # Breaking once connection closed
  
