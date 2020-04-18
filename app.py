di = {}
while(True):
    key = input("Enter your id: ")
    
    if(key == "q"):
        break
    else:
        value = input("Enter your name: ")
        di[key] = value 

        
print(di)
for i in sorted(di.keys()):
        print("Key is " + i + " and the value is " + di[i])
