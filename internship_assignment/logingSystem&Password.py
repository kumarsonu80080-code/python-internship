def loging():
    creatUserName = input("ENTER USERNAME : ")
    creatPassword = input("ENTER PASSWORD : ")
    print("\n")
    print("*** LOGING ***\n")
    

    
    i = 1
    
    while i<4 :
        userName = input("enter user name : ")
        password = input("enter password : ")
        
        if creatUserName == userName and creatPassword == password :
            print("loging successfully")
            break
            
        else:
            print("Incorrect Username & Password !")
            print(f"Attampts Remaining {3-i}")
            i+=1
        if i >3:
            print("----Account Locked----")
    
            
            
        



# logingSystem = loging()
# print(logingSystem)
loging()
