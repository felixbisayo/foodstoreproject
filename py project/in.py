#this file was used to insert the menu options initially, think of it as the admins inserting the possible options at first


import sqlite3

DATABASE = "MELIZZA STORES INVENTORY.db"

food_items = [
    (1, "EBA WITH EGUSI", 20, 1900),
    (2, "EBA WITH EFURIRO", 90, 1500),
    (3, "PEPPER SOUP", 90, 15000),
    (4, "SHARWAMA", 40, 1200),
    (5, "BREAD FAMILY SIZE", 90, 1500),
    (6, "BREAD CHOCOLATE FLVR", 90, 1500),
    (7, "BANANA", 97, 1500),
    (8, "CUCUMBER", 91, 1500),
    (9, "APPLE", 90, 1500),
    (10, "CANNED BEANS", 7, 5000),
    (11, "PIZZA SMALL SIZE", 9, 1500),
    (12, "PIZZA LARGE SIZE", 4, 10000),
    (13, "SPAGHETTI SMALL PLATE", 9, 1500),
    (14, "SPAGHETTI BIG PLATE", 9, 2000),
    (15, "MYSTERY FOOD", 3, 5000),
    (16, "RICE RAW", 7, 4000),
    (17, "BEANS RAW", 9, 3000),
    (18, "CHICKEN AND CHIPS", 4, 5000),
    (19, "JOLLOF RICE SMALL PLATE", 20, 1000),
    (20, "JOLLOF RICE BIG PLATE", 23, 2000),
    (21, "FRIED RICE SMALL PLATE", 21, 1200),
    (22, "FRIED RICE BIG PLATE", 23, 2500),
    (23, "MIXED JOLLOF RICE AND FRIED RICE", 9, 4000),
    (24, "CHICKEN WING", 40, 900),
    (25, "CHICKEN LAP", 20, 3000),
    (26, "TURKEY WING", 29, 1500),
    (27, "TURKEY LAP", 19, 3700),
    (28, "WHITE RICE SMALL PLATE", 9, 1000),
    (29, "WHITE RICE BIG PLATE", 7, 1900),
    (30, "BEANS SMALL PLATE", 10, 900),
    (31, "BEANS BIG PLATE", 10, 1600),
    (32, "MIXED RICE AND BEANS", 10, 2000),
    (33, "OK POP", 500, 100),
    (34, "MENTOS RAINBOW FRUIT", 40, 200)
]

with sqlite3.connect(DATABASE) as con:
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS INVENTORY (
            ID INTEGER PRIMARY KEY,
            GOODS TEXT,
            QUANTITY_AVAILABLE INTEGER,
            UNIT_PRICE_NGN INTEGER
        )
    """)

    cur.execute("SELECT COUNT(*) FROM INVENTORY")

    if cur.fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO INVENTORY VALUES (?, ?, ?, ?)",
            food_items
        )
        print("Inventory successfully populated!")
    else:
        print("Inventory already contains data. No duplicate entries added.")

print("Database setup complete.")
