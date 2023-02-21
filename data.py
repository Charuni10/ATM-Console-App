from admin import admin
from usr import usr

class ATM:
    def __init__(self):
        self.min_bal=1000
        self.user=['charu','sam','ammu']
        self.pin=[2345,9753,4284]
        self.amount=[5000,18765,45672]
        self.password=5234
        self.deno={2000:0,500:0,200:0,100:0}

atm = ATM()



while True:
    
    print("Welcome to ATM")
    print("Select any one option\n  1.Admin\n  2.User\n  3.Exit")
    sel=int(input())
    if(sel==1):
        admin(atm)
    elif(sel==2):
        usr(atm)
    elif(sel==3):
        break
    else:
        print('Please enter a valid input')
