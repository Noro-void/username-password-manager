
def user():
    dictionary={"Mark" : "mark", "Sarah" : "sarah" , "Lucy" : "lucy"}

    while True:
        newuser=input("Enter your username: ")

        if newuser in dictionary:
            print(f"Username {newuser} not available \n")

        else:    
            newpassword=input("Enter your new password: ")
            dictionary[newuser]=newpassword

            print(f"\nYour new username is {newuser} and your new password is {newpassword}")
            print("\n \nUpdated dictionary:")
            for i in dictionary:

                print("Username: "+i+ "Password: "+dictionary[i])
            break
    
user()
