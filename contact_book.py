print("**Welcome to the contact book***")
print("1.ADD A NEW CONTACT\n2.VIEW CONTACTS\n3.SEARCH CONTACT\n4.UPDATE CONTACT\n5.DELETE CONTACT\n6.EXIT")
data=[]
contact={}
choice=1
while(choice<=6):
    choice=int(input("enter your choice:"))
    if(choice==1):
        name=input("enter the name:")
        phone_no=int(input("enter the phone number:"))
        email_id=input("enter the EMAIL ID:")
        address=input("enter your address:")
        if(len(data)==0):
            contact={"name":name,"phone_no":phone_no,"email id":email_id,"address":address}
            data.append(contact)
    elif(choice==2):
         for i in data:
             for key,value in i.items():
                 print(key,":",value)
    elif(choice==3):
        c=0
        search=input("ENTER THE SEARCH NAME:")
        for i in data:
            x=i["name"]
            #x=i.get("name")
            if(search==x):
                for key,value in i.items():
                    print(key,":",value)
                    c+=1
        if(c==0):
            print("not found")
    elif(choice==4):
        c=0
        search=input("ente the contact name to update:")
        for i in data:
            x=i["name"]
            if(x==search):
                update=input("enter the feild to update:")
                c+=1
                for key,value in i.items():
                    if(key==update):
                        v=input("enter the value:")
                        i[key]=v
                        break
                else:
                    print("there is no such key in the contact book")
        if(c==0):
            print("not found")
    elif(choice==5):
        delete=input("enter the contact you want to delete:")
        for i in data:
            x=i.get("name")
            if(delete==x):
                data.remove(i)
                break
        else:
            print("not found")
    elif(choice==6):
        exit()
    
            
                    
                        

        
