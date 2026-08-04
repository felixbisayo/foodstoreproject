import csv
import sqlite3
import pandas as pd

con = sqlite3.connect("MELIZZA STORES INVENTORY.db")
cur = con.cursor()
cart = []
food_no = []
Pt = []
hed = ["FOOD","UNIT PRICE(NGN)","QUANTITY BOUGHT","PRICE(NGN)"]
no = []
dt = []


cur.execute("SELECT * FROM INVENTORY") 
fetchzero = cur.fetchall()

def fetch():
    cur.execute("SELECT * FROM INVENTORY")  

def jj():
    while True:
            ex1 = input("ENTER '1' TO RETURN TO MENU: ")
            if ex1 == '1':
                break
            else:
                print("WRONG INPUT!")
                
def cartfunc():
    # fetch()
    cart_inner = []
    total = 0
    total_1 = 0
    total_2 = 0
    indx = 0
    print(f"\nITEMS IN CART: ")
    if len(cart)==0:
        print('NULL')
    else:
        for w in cart:
            for hu in fetchzero:
                if cart.count(w) > 1 and w == str(hu[1]):
                    val = cart.count(w) * hu[3]
                    asd = f"{cart.count(w)} {str(w).upper()} | {val}NGN"
                    if asd not in cart_inner:
                        cart_inner.append(asd)
                        total_1= total_1+ val
                else:
                    indx += 1
                    val = hu[3]
                    print(f"{indx}. 1 {str(w).upper()} | {hu[3]}NGN")
                    total_2 = total_2 + val
                total = total_1 + total_2
        for o in cart_inner:
            indx += 1
            print(f"{indx}. {o}")
        print(f"TOTAL: {total}NGN\n")
                                                
    jj()

def conti():
    while True:
        ff = input("\n1.RETURN TO MENU\n2.REMOVE ANOTHER ITEM\n").strip()
        if ff == "1":
            break
        elif ff == "2":
            continue
        else:
            print("ENTER 1 OR 2!")
qwert = 0
def tryagain(qwert):
    while True:
        ff = input("\n1.RETURN TO MENU\n2.TRY AGAIN\n").strip()
        if ff == "1":
            break
        elif ff == "2":
            return qwert + 1
        else:
            print("ENTER 1 OR 2!")
    

def removecart():
    fetch()
    fetchzero = cur.fetchall()
    remlist = []
    mullist = []
    indx = 0

    print(f"\nITEMS IN CART: ")
    if len(cart)==0:
        print('NULL')
    else:
        cart_inner = []
        for w in cart:
            for hu in fetchzero:
                if w == str(hu[1]):
                        if cart.count(w) > 1:
                            asd = f"{cart.count(w)} {str(w).upper()} | {(cart.count(w)) * hu[3] }NGN"
                            asf = f"{str(w).upper()}"
                            if asd not in cart_inner:
                                cart_inner.append(asd)
                                mullist.append(asf)
                        else:
                            indx += 1
                            print(f"{indx}. 1 {str(w).upper()} | {hu[3]}NGN")
                            remlist.append(f"{str(w).upper()}")
        for o in cart_inner:
            indx +=1
            print(f"{indx}. {o}")
            for e in mullist:
                remlist.append(e)
        while True:     #loop 1
            remove_option = input("\n1.CHOOSE ITEM TO BE REMOVED\n2.CLEAR ALL ITEMS\n3.RETURN TO MENU\n").strip()
            if remove_option == "2":
                for w in cart:
                    fetch()
                    fetchzero = cur.fetchall()
                    for i in fetchzero: #floop 3
                        if i[1] == w:
                            cur.execute(f"UPDATE INVENTORY SET QUANTITY_AVAILABLE={int(i[2]+1)} WHERE ID={i[0]}")
                            con.commit()
                            # break   #out of floop 3
                cart.clear()
                print("CART CLEARED!!")
                break   #out of loop 1
            
            elif remove_option == "3":
                break   #out of loop 1
            elif remove_option == "1":
                while True:     #loop 2
                    cartremoveoption = input("CHOOSE ITEM TO BE REMOVED: ").strip()
                    if cartremoveoption.isdigit() and cartremoveoption != "0":
                        if int(cartremoveoption) in range(1,len(remlist) + 1):
                            while True:     #loop 3
                                quan1 = input(f"\n1.ENTER QUANTITY OF '{remlist[int(cartremoveoption) - 1]}' TO BE REMOVED\n2.REMOVE ALL '{remlist[int(cartremoveoption) - 1]}'\n3.RETURN TO MENU\n").strip()
                                if quan1 == "3":
                                    break #out of loop 3
                                elif quan1 == "2":
                                    while remlist[int(cartremoveoption) - 1] in cart:   #loop 5
                                        cart.remove(remlist[int(cartremoveoption) - 1])
                                        fetch()
                                        fetchzero = cur.fetchall()
                                        for i in fetchzero:   #floop 1
                                            if i[1] == remlist[int(cartremoveoption) - 1]:
                                                cur.execute(f"UPDATE INVENTORY SET QUANTITY_AVAILABLE={int(i[2]+1)} WHERE ID ={i[0]}")#have to use the primary key which is id to edit it
                                                con.commit()
                                                break #out of floop 1
                                    print(f"ALL {remlist[int(cartremoveoption) - 1]} REMOVED FROM YOUR CART")
                                    break   #out of loop 3
                                elif quan1 == "1":
                                    while True:      #loop 4
                                        quan2 = input(f"ENTER QUANTITY OF {remlist[int(cartremoveoption) - 1]} TO BE REMOVED: ").strip()
                                        if quan2.isdigit() and quan2 != "0":
                                            if int(quan2) <= cart.count(remlist[int(cartremoveoption) - 1]):
                                                for jh in range(int(quan2)):
                                                    ind = cart.index(remlist[int(cartremoveoption) - 1])
                                                    cart.pop(ind)
                                                    fetch()
                                                    fetchzero = cur.fetchall()
                                                    for i in fetchzero:   #floop 2
                                                        if i[1] == remlist[int(cartremoveoption) - 1]:
                                                            cur.execute(f"UPDATE INVENTORY SET QUANTITY_AVAILABLE={int(i[2]+1)} WHERE ID ={i[0]}")
                                                            con.commit()
                                                            break #out of floop 2
                                                print(f"{quan2} {remlist[int(cartremoveoption) - 1]} REMOVED FROM CART!")
                                                break #OUT OF LOOP 4
                                            else:
                                                print(F"YOU DON'T HAVE '{quan2}' {remlist[int(cartremoveoption) - 1]} IN YOUR CART")
                                        else:
                                            print("ENTER A POSITIVE INTEGER!")        
                                       
                                    break #out of loop 3
                                else:
                                    print(f"ENTER BETWEEN 1-3!")    
                            break #out of loop 2
                        else:
                            print(f"\nTHERE IS NO ITEM NUMBERED '{cartremoveoption}'")
                            if tryagain(qwert) == 1:
                                continue #top of loop 2
                            else:
                                break# out of loop 2
                    else:
                        print("ENTER AN ITEM NO. IN THE LIST!")
                        if tryagain(qwert) == 1:
                            continue #top of loop 2
                        else:
                            break# out of loop 2
                        
                break #out of loop 1            
            else:
                print(f"ENTER BETWEEN 1-3!")  
                continue # to the beginning of loop 1                    
            
    jj()
    
def receipt(bie = [], kie = [],tot = [],cart_inner = [],disco = [],br=0):   #csv file
    while True:
            card = input("ENTER YOU CARD NUMBER (8 DIGITS) OR 'E' TO EXIT: ")
            if card.isdigit() and len(card) == 8:
                print("THANK YOU, TRANSACTION SUCCESFUL")
                with open('receipt.csv','w',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(hed)
                    writer.writerows(bie)
                    writer.writerows(kie)
                    writer.writerow(tot)
                    writer.writerow(disco)
                cart.clear()
                cart_inner.clear()
                break
            elif card.lower() == "e":
                return br + 1
            else:
                print("CARD INFO MUST BE 8 DIGITS!")
            
def receipt_view():
    while True:              
            receipt_option = input("ENTER 1 TO VIEW RECEIPT, 2 TO RETURN TO MENU: \n").strip()
            if receipt_option == "1":
                print("\n")
                rec = pd.read_csv('receipt.csv')
                rec.index = rec.index + 1 
                print(f"{rec}\n")
                break
            elif receipt_option == "2":
                print("\n")
                print("THANKS FOR USING OUR PLATFORM :)")
                break
            else:
                print("WRONG INPUT, TRY AGAIN")
                          
def payin():
    indx = 0
    total = 0
    total_1 = 0
    total_2 = 0
    print(f"ITEMS IN CART: ")
    if len(cart)==0:
        print('CART IS EMPTY!!')
    else:
        dt=[]
        kie = []
        bie = []
        cart_inner = []
        for w in cart:
            for li in fetchzero:
                if w == str(li[1]).upper():
                    if cart.count(w)> 1:
                        val = cart.count(w) * li[3]
                        asd = f"{cart.count(w)} {str(w).upper()} | {val}NGN"
                        if asd not in cart_inner:
                            cart_inner.append(asd)
                            dt = [f"{str(w).upper()}",li[3],cart.count(w),val]
                            bie.append(dt)
                            
                            total_1= total_1+ val

                    else:
                        val = li[3]
                        indx += 1
                        Pt = [f"{str(w).upper()}",li[3],cart.count(w),val]
                        kie.append(Pt)
                        print(f"{indx}. {cart.count(w)} {str(w).upper()} | {li[3]}NGN")
                        total_2 = total_2 + val
                    total = total_1 + total_2
                    tot = ["TOTAL(NGN)","...","...",total]
                    
        for o in cart_inner:
            indx += 1
            print(f"{indx}. {o}")
        print(f"TOTAL : {total}NGN\n")
                    
        while True:
            br = 0
            #discounts            
            if total >= 5000:
                print(f"YOU HAVE A 12% DISCOUNT BECAUSE YOU ORDERED GOODS WORTH MORE THAN 4999NGN!!")
                discount = total - ((12/100)*total)
                disc = input(f"YOU ARE ABOUT TO BUY THE ABOVE ITEMS FOR {discount}NGN\nENTER 1 TO CONFIRM OR 2 TO EXIT: ").strip()
                if disc == "1":
                    disco = ["DISCOUNT","12%","...",discount]
                    if receipt(bie,kie,tot,cart_inner,disco,br) == 1:
                        break
                    receipt_view()
                    break
                elif disc == "2":
                    break
                else:
                    print("WRONG INPUT, TRY AGAIN")
        
            elif total == 3500:
                print(f"YOU HAVE A 10% DISCOUNT BECAUSE YOU ORDERED GOODS WORTH 3500NGN!!")
                discount = total - ((10/100)*total)
                disc = input(f"YOU ARE ABOUT TO BUY THE ABOVE ITEMS FOR {discount}NGN\n1.CONFIRM \n2.EXIT\n").strip()
                if disc == "1":
                    disco = ["DISCOUNT","10%","...",discount]
                    if receipt(bie,kie,tot,cart_inner,disco,br) == 1:
                        break
                    receipt_view()
                    break     
                elif disc == "2":
                    break
                else:
                    print("WRONG INPUT, TRY AGAIN")
                    
            elif total > 2000 and total < 3500:
                print(f"YOU HAVE A 5% DISCOUNT BECAUSE YOU ORDERED GOODS WORTH BETWEEN 2000NGN AND 3500NGN!!")
                discount = total - ((5/100)*total)
                disc = input(f"YOU ARE ABOUT TO BUY THE ABOVE ITEMS FOR {discount}NGN\nENTER 1 TO CONFIRM OR 2 TO EXIT\n").strip()
                if disc == "1":
                    disco = ["DISCOUNT","5%","...",discount]
                    if receipt(bie,kie,tot,cart_inner,disco,br) == 1:
                        break
                    receipt_view()
                    break
                elif disc == "2":
                    break
                else:
                    print("WRONG INPUT, TRY AGAIN")  
                                                                    
            else:
                disc = input(f"YOU ARE ABOUT TO BUY THE ABOVE ITEMS FOR {total}NGN\nENTER 1 TO CONFIRM OR 2 TO EXIT\n").strip()
                if disc == "1":
                    disco = []
                    if receipt(bie,kie,tot,cart_inner,disco,br) == 1:
                        break
                    receipt_view()
                    break
                elif disc == "2":
                    break
                else:
                    print("WRONG INPUT, TRY AGAIN") 
    jj()

print("------------------------------------------------------------\n                WELCOME TO MELIZZA STORES \n                 PLEASE MAKE YOUR ORDER\n------------------------------------------------------------")
def maincode():
    
    #customer can order as many items as possible
    while True:
        try:
            print("                         ---MENU---")
            print("")
            
            cur.execute("SELECT * FROM INVENTORY WHERE QUANTITY_AVAILABLE > 0")
            fetchnozero = cur.fetchall()
            #displaying of the datbase/stock
            table = pd.DataFrame({"ID NO.":[i[0] for i in fetchnozero],"FOOD NAME": [i[1] for i in fetchnozero],"UNIT PRICE": [i[3] for i in fetchnozero],"QUANTITY IN STOCK": [i[2] for i in fetchnozero]})
            table.index = table.index + 1
            table.set_index('ID NO.', inplace=True)
            print(table)
            
            for p in fetchnozero:
                no.append(str(p[0]))
                #prompting the user for what he/she wants to order   
            option1 = input("\nENTER ID NO. OF DESIRED FOOD \nENTER 'E' TO EXIT | ENTER 'C' TO VIEW CART\nENTER 'R' TO REMOVE FROM CART | ENTER 'P' TO PAY\n").strip() 
            if option1.lower() == "e":
                print("THANKS, SEE YOU NEXT TIME")
                while len(cart) != 0:   
                    fetch()
                    fetchzero = cur.fetchall()
                    for l in cart:
                        for i in fetchzero:   
                            if i[1] == l:
                                cur.execute(f"UPDATE INVENTORY SET QUANTITY_AVAILABLE={int(i[2]+1)} WHERE ID ={i[0]}")#
                                con.commit()
                                indx = cart.index(l)
                                cart.pop(indx)
                                break #out of floop 1                    
                break        
            elif option1.lower() == "c":
                cartfunc()
            elif option1.lower() == "r":
                removecart()
            elif option1.lower() =="p":
                payin()
                
            elif (option1) in no:
                cur.execute("SELECT * FROM INVENTORY")
                n = cur.fetchall()
                for p in n:
                    if int(option1) == p[0]:
                        
                        print(f"{p[1]}")
                        G = 0
                        while True:
                            if G != 0:
                                break       
                            #requesting what quantity the user wants to order
                            num_option =  input(f"ENTER QUANTITY NEEDED OR ENTER 'R' TO RETURN TO MENU: ").strip()
                            if num_option.lower() == "r":
                                break
                            elif num_option.isdigit():
                                if int(num_option) <= p[2] and int(num_option) > 0:
                                    #final confirmation
                                    print(f"ARE YOU SURE YOU WANT TO PUT {num_option} {p[1]} IN YOUR CART? \nPRICE: {int(p[3])*int(num_option)}NGN\n1. YES\n2. NO")
                                    sure_option =  input().strip()
                                    if sure_option == "1":
                                        for k in range(int(num_option)):
                                            cart.append(str(p[1]))      #appending the item the number of times specified
                                        print(f"{num_option} {p[1]} ADDED TO CART!")
                                        print(f"THERE ARE {int(p[2])-int(num_option)} {p[1]} LEFT IN STOCK")
                                        #reducing the quantity in the database
                                        cur.execute(f"UPDATE INVENTORY SET QUANTITY_AVAILABLE={int(p[2])-int(num_option)} WHERE ID={p[0]}")
                                        con.commit()
                                        break
                                    elif sure_option == "2":
                                        print("ORDER CANCELLED!!")
                                        jj()
                                        break
                                    else:
                                        print("WRONG INPUT, TRY AGAIN")
                                        continue
                                elif int(num_option) > p[2]:
                                    print(f"WE DON'T HAVE UP TO {num_option} IN STOCK!")
                                elif int(num_option) == 0:
                                    print(f"YOU CAN'T ORDER ZERO {p[1]}, TRY AGAIN")
                            else:
                                print(f"WE DONT HAVE '{num_option}' {p[1]} IN STOCK")
                                h = 0
                                while True:
                                    if h!=0:
                                        break
                                    exit0 = input("ENTER 1 TO RETURN TO MENU\nENTER 2 TO TRY AGAIN\n").strip()
                                    if exit0 != "2":
                                        if exit0 == "1":
                                            G += 1
                                            break
                                        else:
                                            print("WRONG INPUT,TRY AGAIN")
                                    else:
                                        h+=1
                                        continue
            else:
                print(f"\n'{option1}' is not an ID NO. IN THE MENU")
                while True:
                    option_4 = input("ENTER 1 TO CONTINUE: ").strip()
                    if option_4 == "1":
                        break
        except ValueError as e:
            print("WRONG INPUT, TRY AGAIN")
            while True:
                option_4 = input("ENTER 1 TO CONTINUE: ").strip()
                if option_4 == "1":
                    break
maincode()
con.close()