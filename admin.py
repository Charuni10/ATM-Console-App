
def admin(atm):
    print("enter the password :")
    pas=int(input())
    if(pas==atm.password):
        print("Entered password is right")
        print("Select any one option\n  1.Load amount\n  2.Check ATM Cash\n  3.Exit")
        ad=int(input())
        
        if(ad==1):
            deno_2000=int(input("Enter the number of 2000 rupees notes to be loaded: "))
            deno_500=int(input("Enter the number of 500 rupees notes to be loaded: "))
            deno_200=int(input("Enter the number of 200 rupees notes to be loaded: "))
            deno_100=int(input("Enter the number of 100 rupees notes to be loaded: "))
            print(atm.deno)

            if(atm.deno[2000]+deno_2000>=100):
                print("The notes loaded can be only 100, so remove ",deno_2000-100,"notes")
                
            elif(atm.deno[500]+deno_500>=100):
                print("The notes loaded can be only 100, so remove ",deno_500-100,"notes")
               
            elif(atm.deno[200]+deno_200>=100):
                print("The notes loaded can be only 100, so remove ",deno_200-100,"notes")
                
            elif(atm.deno[100]+deno_100>=100):
                print("The notes loaded can be only 100, so remove ",deno_100-100,"notes")
                
            else:
                atm.deno[2000]+=deno_2000
                atm.deno[500]+=deno_500
                atm.deno[200]+=deno_200
                atm.deno[100]+=deno_100
                print(atm.deno)
                print("The amount is successfully loaded")
        elif(ad==2):
            atm.bal=atm.deno[2000]*2000+atm.deno[500]*500+atm.deno[200]*200+atm.deno[100]*100
            print("The amount present in the ATM is ",atm.bal)
        elif(ad==3):
            print('Exit')
        else:
            print("Provide a valid input")
    else:
        print("The password is not correct")
        