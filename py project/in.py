import sqlite3

con = sqlite3.connect("MELIZZA STORES INVENTORY.db")
cur = con.cursor()

def createtable():
    cur.execute('CREATE TABLE IF NOT EXISTS INVENTORY (ID INTEGER PRIMARY KEY , GOODS TEXT, QUANTITY_AVAILABLE INTEGER, UNIT_PRICE_NGN INTEGER)')
    con.commit()
    # con.close()
    print("table created")

# createtable()
def inputdata(id,good_name,quantity,unit_price):
    cur.execute('INSERT INTO INVENTORY VALUES(?,?,?,?)',(id,good_name,quantity,unit_price))
    con.commit()
    # con.close()
    print("data inserted")
    
# cur.execute("DELETE FROM INVENTORY WHERE ID = 22")
# cur.execute(f"UPDATE INVENTORY SET QUANTITY_AVAILABLE=202 WHERE ID = 33")
# cur.execute(f"UPDATE INVENTORY SET GOODS='POUNDO WITH EFURIRO' WHERE ID = 2")
# cur.execute(f"UPDATE INVENTORY SET GOODS='POUNDO WITH EGUSI' WHERE ID = 1")


con.commit()


# inputdata(1,"EBA WITH EGUSI",20,1900)
# inputdata(2,"EBA WITH EFURIRO",90,1500)
# inputdata(3,"PEPPER SOUP",90,15000)
# inputdata(4,"SHARWAMA",40,1200)
# inputdata(5,"BREAD FAMILY SIZE",90,1500)
# inputdata(6,"BREAD CHOCOLATE FLVR",90,1500)
# inputdata(7,"BANANA",97,1500)
# inputdata(8,"CUCUMBER",91,1500)
# inputdata(9,"APPLE",90,1500)
# # # inputdata(20,"SARDINE BREAD",9,1500)
# # inputdata(21,"SARDINE",9,1000)
# inputdata(10,"CANNED BEANS",7,5000)
# inputdata(11,"PIZZA SMALL SIZE",9,1500)
# inputdata(12,"PIZZA LARGE SIZE", 4 ,10000)
# inputdata(13,"SPAGHETTI SMALL PLATE",9,1500)
# inputdata(14,"SPAGHETTI BIG PLATE",9,2000)
# inputdata(15,"MYSTERY FOOD",3,5000)
# inputdata(16,"RICE RAW ",7,4000)
# inputdata(17,"BEANS RAW ",9,3000)
# inputdata(18,"CHICKEN AND CHIPS",4,5000)
# inputdata(19,"JOLLOF RICE SMALL PLATE",20,1000)
# inputdata(20,"JOLLOF RICE BIG PLATE",23,2000)
# inputdata(21,"FRIED RICE SMALL PLATE",21,1200)
# inputdata(22,"FRIED RICE BIG PLATE",23,2500)
# inputdata(23,"MIXED JOLLOF RICE AND FRIED RICE",9,4000)
# inputdata(24,"CHICKEN WING",40,900)
# inputdata(25,"CHICKEN LAP",20,3000)
# inputdata(26,"TURKEY WING",29,1500)
# inputdata(27,"TURKEY LAP",19,3700)
# inputdata(28,"WHITE RICE SMALL PLATE",9,1000)
# inputdata(29,"WHITE RICE BIG PLATE",7,1900)
# inputdata(30,"BEANS SMALL PLATE",10,900)
# inputdata(31,"BEANS BIG PLATE",10,1600)
# inputdata(32,"MIXED RICE AND BEANS",10,2000)
# inputdata(33,"OK POP",500,100)
# inputdata(34,"MENTOS RAINBOW FRUIT",40,200)




