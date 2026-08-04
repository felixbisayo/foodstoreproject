import sqlite3
import pandas as pd

def view():
    con = sqlite3.connect("MELIZZA STORES INVENTORY.db")
    cur = con.cursor()
    # cur.execute("SELECT * FROM INVENTORY")
    rec = cur.fetchall()
    table = pd.read_sql_query("SELECT * FROM INVENTORY", con)
    # table = pd.DataFrame({'ID': [item[0] for item in rec], 'GOODS': [item[1] for item in rec]})
    # table.index = table.index + 1
    con.close()
    print(table)
    
view()