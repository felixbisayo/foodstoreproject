# lst = (2,3,3,4,5,5,5),(6,6,6,6,6),(9090,9),(0),(8989,666)
# if 4 in range(len(lst)):
#     print("jj")
# else:
#     print("nah")

# hello()
# def hello():
#     print("k")
# x = input()
# if x == "2":
#     y = 9
# if y != 9:
#     print("jklkjl")
# cart_inner = []

# v = 0
# while v < 3:
#     v +=1
#     asd = "kkk"
#     if asd not in cart_inner:
#         cart_inner.append(asd)
#         for o in cart_inner:
#             print(o)
# l = []
# v = 2
# for i in range(v):
#     l.append("jj")
# print(l)

# import pandas as pd

# dk
# r = "      jjjjjj      jjjjj jjjjjj jjjjj      "
# print(r.strip())

# rec = pd.read_csv('receipt.csv',index_col=0)
# print(rec)

# def yu(di = [],dk = []):
#     print(di)
#     print(dk)
    
# di = [2,2,2]
# yu(di,dk)
# i = "2"
# if i in range(5):
#     print("l")
# i = 2
# l = [1,2,2]
# if i in range(len(l)):
#     print("hj")


# t=0
# def ll():
#     t 

# for i in range(1,5+1):
#     print(i)

# w = input("ee: ")
# if w.isdigit():
# #     print("digits")
# def r(w):
#     while True:
#         print(w)
#         return w+1
# d=0
# if r(d) == 1:
#     print("hjk")


# C = ["WWW","WWW"]
# while "WWW" in C:
#     C.remove("WWW")
# print(C)

import sqlite3

con = sqlite3.connect("MELIZZA STORES INVENTORY.db")
cur = con.cursor()
def fumc():
    cur.execute("SELECT * FROM INVENTORY WHERE QUANTITY_AVAILABLE > 0")
fumc()
fetchnozero = cur.fetchall()

for i in fetchnozero:
    print(i)