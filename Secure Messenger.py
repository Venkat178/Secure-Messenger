list_of_users=[]
#To Store Paswords
pas={}
#To Store message requests 
req={}
#TO Store Messages
msg={}
class wapp:
    def addUser(self):
        list_of_users.append("user"+str(len(list_of_users)+1))
        print("Username   :   "+list_of_users[-1])
        p=input("Enter the password   :   ")
        r=input("Re-enter the password   :   ")
        if p==r:
            user=list_of_users[-1]
            pas[user]=p
            req[user]={}
            msg[user]={}
        else:
            print("Pasword did not match")
            list_of_users.pop()
            self.addUser()
            
            
    def login(self):
        if list_of_users!=[]:
            print("The list of users Registered are   :   "+str(list_of_users))
            user=input("Enter the username   :   ")
            if user in list_of_users:
                k=input("Enter the password   :   ")
                if k==pas[user]:
                    while True:
                        print("1. Send message to a friend .")
                        print("2. View Requests and Messages.")
                        print("3. View Password .")
                        print("4. Logout .")
                        print("5. Exit .")
                        choice=int(input("Enter your choice   :   "))
                        if choice==1:
                            self.send_msg(user)
                        elif choice==2:
                            self.view_req(user)
                        elif choice==3:
                            print(pas[user])
                        elif choice==4:
                            print(user+" Logged Out .")
                            self.logout()
                            break
                        elif choice==5:
                            break
                        else:
                            print("Enter Valid Choice .")
                else:
                    print("Your password is wrong .Please try again")
            else:
                print("There is no user registered with this username . ")
        else:
            print(" No users are Registered yet .")
                             
                             
    def send_msg(self,user):
        u=input("Enter the user you want to sent the message   :   ")
        if u not in list_of_users:
            print(" Message Sent Fail . User not Found ")
            return
        m=input("Enter the message you want to sent   :   ")
        req[u][user]=m
        
        
    def view_req(self,user):
        for i in req[user]:
            k=input(i+" sends message. Do you want accept it (yes/no)   :   ")
            if k=="yes":
                msg[user][i]=req[user][i]
        req[user]={}
        for i in msg[user]:
            print(" From "+i+" : "+msg[user][i])
        
        
    def logout(self):
        self.login()
        

    def display(self):
        if list_of_users!=[]:
            print(" You're Messages , Passwords Got Leaked .")
            print(" Users with their messages   :   "+str(msg))
            print(" Users with their repsective passwords   :   "+str(pas))
        else:
            print(" No DataBase Found .")
            
         
w=wapp()
while True:
    print("1. Add a User .")
    print("2. Login .")
    print("3. Display the Messages , Passwords and Users registered .")
    print("4. Exit from Application .")
    ch=int(input("Enter your choice   :   "))
    if ch==1:
        w.addUser()
    elif ch==2:
        w.login()
    elif ch==3:
        w.display()
    elif ch==4:
        print( " Have a great time with you .")
        break
    else:
        print( "Invalid Choice choosen .")