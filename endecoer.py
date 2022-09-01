import random

print(""" 
.                   _                                     
  ___   _ __     __| |   ___    ___    ___     ___   _ __ 
 / _ \ | '_ \   / _` |  / _ \  / __|  / _ \   / _ \ | '__|
|  __/ | | | | | (_| | |  __/ | (__  | (_) | |  __/ | |   
 \___| |_| |_|  \__,_|  \___|  \___|  \___/   \___| |_|   


""")

def encoder(message):
    alphabet=[]
    for i in range(65,91):
        alphabet.append(chr(i))
        
    message= message.upper()
    length=(len(message))
    a=[]
    for i in range(length):
       a.append([])
    
    for j in range(length):
       a[j].append(message[j])
    
    for i in range(length):
      for j in range(length):
         a[i].append(random.choice(alphabet))
        
    for i in range(length):
        for j in range(length):
            print(a[i][j], end="")

def decoder(enmessage):
    
    y=int((len(enmessage))**0.5)
    print(enmessage[0::y])

x=int(input("1.encode\n2.decode\n enter your choice \n"))

if x==1:
    message=input("enter your message \n")
    encoder(message)
    
elif x==2:
    enmessage=input("enter the encoded text\n")
    decoder(enmessage)
    
else:print("wrong choice")
