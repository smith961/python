import string 
import random

def get_details():
    first_name=input("Enter your First Name below\n")
    second_name=input("Enter your Second Name below\n")
    user_email=input("Enter your Email address below\n")
    details=[first_name,second_name,user_email]
    return details
   
def gen_password(details):
    
    characters = string.ascii_letters
    length=5
    random_password = ''.join(random.choice(characters)for i in range (length))
    
    password = str(details[0][0:2]+details[1][-2:]+random_password)
    
    return password
        
status = True
container = []
while status:
    
        details = get_details()
        password = gen_password(details)
        print("Your password is: "+ str(password))
        
        password_like=input("do you like the generated password. if yes enter Yes if no, enter No and supply your password")

        password_loop = True

        while password_loop:
            if password_like == "Yes":
                details.append(password) 
                container.append(details)
                
                password_loop=False
            else:
                user_password=input("Enter password longer than or equal to 7 ")
            
                pass_len=True
           
                while pass_len:
                
                 if len(user_password) >= 7:
                    details.append(user_password)
                    container.append(details)
                    pass_len = False

                    password_loop = False   
                else:
                    print("Your password is less than 7")
                    user_password=input("Enter password longer than or equal to 7")
new_user=input("Would you like to enter a new user? Yes or No")
if (new_user == "No"):
                
    status=False 
    for item in container:
        print(item)
else:
    status= True

                