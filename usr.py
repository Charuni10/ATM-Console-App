
import io


def usr(atm):
    username=input("Enter the username : ")
    s=[]
    if(username not in atm.user):
        print("Incorrect username")
    else:
        if(username==atm.user[0]):
            n=0
        elif(username==atm.user[1]):
            n=1
        elif(username==atm.user[2]):
            n=2
        global amount,stmt,pin 

        pwd=int(input("Enter the pin : ")) 
        if(pwd==atm.pin[n]):
            while True:
                print("Welcome!! Select any one option\n  1.Check balance\n  2.Withdrawal\n  3.Mini Statement\n  4.Deposit\n  5.Transfer\n  6.Pin change\n  7.Exit")
                us=int(input())
                
                if(us==1):
                    print("The balance amount in the account is ",atm.amount[n])

                elif(us==2):
                    withd=int(input("Enter the amount to be withdrawn : "))
                    copy_withd=withd
                    copy_deno=atm.deno.copy()
                    copy_amount=atm.amount.copy()
                    if copy_withd<=(atm.amount[n]-atm.min_bal) and copy_withd%100==0:
                        for i in copy_deno.keys():
                            c=copy_withd//i
                            if(c<=copy_deno[i]):
                                copy_withd=copy_withd%i
                                copy_deno[i]-=c
                                copy_amount-=copy_deno[i]*c
                        if(copy_withd==0):
                            atm.deno=copy_deno
                            atm.amount[n]=copy_amount
                            atm.bal-=withd
                            print("The amount is successfully withdrawed")
                            print("The account balance is ",atm.amount[n])
                            pri="The amount is successfully withdrawed is",withd
                            s.append(pri)
                        else:
                            print("The amount you have entered is not available in the ATM")           
                    else:
                        print("The amount you have entered exceeds the main balance ")
                elif(us==3):
                    print("Mini Statement for ",username)
                    print("User name : ",atm.user[n])
                    print("Balance : ",atm.amount[n])
                    print(s[:5])

                elif(us==4):
                    dep_2000=int(input("Please enter the 2000 rupees notes you need to deposit :"))
                    dep_500=int(input("Please enter the 500 rupees notes you need to deposit :"))
                    dep_200=int(input("Please enter the 200 rupees notes you need to deposit :"))
                    dep_100=int(input("Please enter the 100 rupees notes you need to deposit :"))
                    dep=dep_2000*2000+dep_500*500+dep_200*200+dep_100*100
    #                 print(dep)
                    if(atm.deno[2000]+dep_2000>100):
                        print("Only ",100-atm.deno[2000]," notes can be added")
                    elif(atm.deno[500]+dep_500>100):
                        print("Only ",100-atm.deno[500]," notes can be added")
                    elif(atm.deno[200]+dep_200>100):
                        print("Only ",100-atm.deno[200]," notes can be added")
                    elif(atm.deno[100]+dep_100>100):
                        print("Only ",100-atm.deno[100]," notes can be added")
                    else:   
                        atm.deno[2000]+=dep_2000
                        atm.deno[500]+=dep_500
                        atm.deno[200]+=dep_200
                        atm.deno[100]+=dep_100
                        atm.amount[n]+=dep
                        atm.bal+=dep
                        print("The amount is successfully deposited")
                        print("The account balance is ",atm.amount[n])
                        pri="The amount is successfully deposited is",dep
                        s.append(pri)

                elif(us==5):

                    u=input("The user you need to transfer money : ")
                    if(u==atm.user[0]):
                        if(u==atm.user[n]):
                            print("The account name are same")
                        else:
                            amt=int(input("The amount you need to transfer is :"))
                            if(atm.amount[n]-atm.min_bal<=amt):
                                print("There is no sufficient amount in the account")
                            else:
                                atm.amount[n]-=amt
                                atm.amount[0]+=amt
                                print("Amount successfully transferred")
                                pri="The amount transferred is",amt
                                s.append(pri)
                    if(u==atm.user[1]):
                        if(u==atm.user[n]):
                            print("The account name are same")
                        else:
                            amt=int(input("The amount you need to transfer is :"))
                            if(atm.amount[n]-atm.min_bal<=amt):
                                print("There is no sufficient amount in the account")
                            else:
                                atm.amount[n]-=amt
                                atm.amount[1]+=amt
                                print("Amount successfully transferred")
                                pri='The amount transferred is ',amt
                                s.append(pri)
                    elif(u==atm.user[2]):
                        if(u==atm.user[n]):
                            print("The account name are same")
                        else:
                            amt=input("The amount you need to transfer is :")
                            if(atm.amount[n]-1000<=amt):
                                print("There is no sufficient amount in the account")
                            else:
                                atm.amount[n]-=amt
                                atm.amount[2]+=amt
                                print("Amount successfully transferred")
                                s.append("The amount transferred is",amt)
                    else:
                        print("Enter a valid user name")

                elif(us==6):

                    print("Do you want to change your pin? \n 1.Yes \n 2.No")
                    p=int(input("Enter the new pin"))
                    if(len(str(p))!=4):
                        print("Please enter a 4 digit pin")
                    elif(p==atm.pin[n]):
                        print("Please provide a new pin, it is the same as the old pin")
                    else:
                        atm.pin[n]=p
                        print("New pin is successfully updated")
                elif(us==7):
                    break

        elif(pwd!=atm.pin[n]):
            print("Incorrect pin")
    
    
        
    
   