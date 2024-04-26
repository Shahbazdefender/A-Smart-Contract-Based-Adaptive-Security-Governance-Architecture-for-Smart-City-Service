# Presentation of Programmable Script

Please Read the help file that will help you to undertand the Usecase and Installation of the core technolgies 

# Key Generation Contract
#!/bin/bash
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 
do
echo "Shahbaz"
openssl ecparam -name prime128v1 -genkey -noout -out private-key$i.pem > /home/ubuntu/Desktop/Shahbaz_Final_Project/Ada-Framework-Shahbaz1/01-GetStarted/Keys/keto$i.key

openssl ec -in private-key$i.pem -pubout -out public-key$i.pem
openssl dgst -sha256 -binary private-key$i.pem > /home/ubuntu/Desktop/Shahbaz_Final_Project/Ada-Framework-Shahbaz1/01-GetStarted/Keys/hash$i.txt
#openssl pkeyutl -sign -inkey private-key$i.pem -in hash$i.txt > /home/ubuntu/Desktop/Shahbaz_Final_Project/Ada-Framework-Shahbaz1/01-GetStarted/Keys/sig$i.txt
openssl pkeyutl -sign -inkey private-key$i.pem -in private-key$i.pem > /home/ubuntu/Desktop/Shahbaz_Final_Project/Ada-Framework-Shahbaz1/01-GetStarted/Keys/sig$i.txt

done

file="$1"
echo $file

openssl pkeyutl -verify -in $file -sigfile sig1.txt -inkey private-key1.pem
echo shahbaz
echo $verify


# This code Generate the Keys pairs For Decentralized Application 




import sys
import hashlib
def hashfile(file):
  
    # A arbitrary (but fixed) buffer
    # size (change accordingly)
    # 65536 = 65536 bytes = 64 kilobytes
    BUF_SIZE = 65536
  
    # Initializing the sha256() method
    sha256 = hashlib.sha256()
  
    # Opening the file provided as
    # the first commandline argument
    with open(file, 'rb') as f:
         
        while True:
             
            # reading data = BUF_SIZE from
            # the file and saving it in a
            # variable
            data = f.read(BUF_SIZE)
  
            # True if eof = 1
            if not data:
                break
      
            # Passing that data to that sh256 hash
            # function (updating the function with
            # that data)
            sha256.update(data)
  
      
    # sha256.hexdigest() hashes all the input
    # data passed to the sha256() via sha256.update()
    # Acts as a finalize method, after which
    # all the input data gets hashed hexdigest()
    # hashes the data, and returns the output
    # in hexadecimal format
    return sha256.hexdigest()
 
# Calling hashfile() function to obtain hashes
# of the files, and saving the result
# in a variable
f1_hash = hashfile(sys.argv[1])
f2_hash = hashfile(sys.argv[2])
  
# Doing primitive string comparison to
# check whether the two hashes match or not
if f1_hash == f2_hash:
    print("Both files are same")
    print(f"Hash: {f1_hash}")
 
else:
    print("Files are different!")
    print(f"Hash of File 1: {f1_hash}")
    print(f"Hash of File 2: {f2_hash}")





# Contract-2

import json


with open("inputJSON.txt", "r") as json_file:

data = json.load(json_file)

totalNumberOfKeysFetched = len(data.keys())

print(totalNumberOfKeysFetched)
engine.declare(Light(numberOfKeysExpected=str(totalNumberOfKeysFetched)))
        
engine.run()

engine.declare(Light(firstKeyData=str(firstKeyDataInput), secondKeyData=str(secondKeyDataInput)))
        
engine.run()



# Contract-3


import json


with open("inputJSON.txt", "r") as json_file:

data = json.load(json_file)

totalNumberOfKeysFetched = len(data.keys())

print(totalNumberOfKeysFetched)

engine.declare(Light(numberOfKeysExpected=str(totalNumberOfKeysFetched)))
