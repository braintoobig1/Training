username = ""
password = ""
reqp = ""
requ = ""
hold = 0

#Checks to see that password is right
def checkpassword(pas): 
    if pas == reqp:
        print("Password is correct")
        hold = 1
    else:
        print("Password is incorrect please try again")
        hold = 0
        

    
#checks to see that username is right
def checkusername(user):
    if requ == user:
        print("Username is Correct")
        hold = 1
    
    else:
        print("Username is incorrect please try again")
        hold = 0

print("Hello, Welcome to Invictus")
print("PLEASE ENTER YOUR USER NAME AND PASSWORD")

#sets the correct username and password requirements 
requ = "bcozart"
reqp = "cozart"

# will repeat if the user name or password is incorrect
while hold == 0: 

    username = input("username:")
    password = input("password:")

    checkpassword(password)
    checkusername(username)





    

