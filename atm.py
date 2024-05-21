import time 
print("PLEASE INSERT YOUR CARD")
time.sleep(5)
pin=2003
balance=20000
pin1=int(input("PLEASE ENTER YOUR PIN"))
if pin1==pin:
    while True:
        print("""
                  1==BALANCE
                  2==WITHDRAW
                  3==DEPOSIT
                  4==EXIT""")
        try:
            option=int(input("ENTER YOUR OPTION"))
            print("=================================================")
            print("=================================================")
        except:
            print("INVALID")
        if option==1:
            print(f"YOUR CURRENT BALANCE IS {balance}")
            print("=================================================")
            print("=================================================")
            print("=================================================")
            break
        if option==2:
            withdraw=int(input("ENTER WITHDRAW AMOUNT"))
            print("=================================================")
            print("=================================================")
            balance=balance-withdraw
            print(f"{withdraw} IS DEBITED FROM YOUR ACCOUNT")
            print("=================================================")
            print("=================================================")
            print(f"YOUR CURRENT BALANCE IS {balance}")
            print("=================================================")
            print("=================================================")
            print("=================================================")
            break
        if option==3:
            deposit=int(input("ENTER DEPOSIT AMOUNT"))
            print("=================================================")
            print("=================================================")
            balance=balance+deposit
            print(f"{deposit} IS CREDITED TO YOUR ACCOUNT")
            print("=================================================")
            print("=================================================")
            print(f"YOUR CURRENT BALANCE IS {balance}")
            print("=================================================")
            print("=================================================")
            print("=================================================")
            break
        if option==4:
            break
else:
    print("INVALID PIN\n PLEASE TRY AGAIN")
