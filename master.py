import sqlite3
a=sqlite3.connect("database.db")
b=a.cursor()
b.execute(   """
CREATE TABLE IF NOT EXISTS kompyuter(
    nomi TEXT
    narxi TEXT
    xotirasi TEXT
)
"""
)

b.execute(   """
CREATE TABLE IF NOT EXISTS odam(
    ismi TEXT
    fan TEXT
    yosh TEXT
)
"""
)


b.execute(   """
CREATE TABLE IF NOT EXISTS hayvon(
    nomi TEXT
    turi TEXT
    yashash_joyi TEXT
)
"""
)

b.execute(   """
CREATE TABLE IF NOT EXISTS transport(
    nomi TEXT
    turi TEXT
    yili TEXT
)
"""
)

