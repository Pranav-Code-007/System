import cx_Oracle

# username/password@//localhost:1521/XEPDB1
# system/root@//localhost:1521/XEPDB1
conn = cx_Oracle.connect("system/root@//localhost:1521/XEPDB1")
cur = conn.cursor()
print(conn.version)
print("After conn.version")

def insertIntoUser(firstname, lastname, mobnum, email, passwd, timest):
    query = f"insert into usr values('{firstname}','{lastname}','{mobnum}','{email}','{passwd}','{timest}')"
    try:
        cur.execute(query)
        conn.commit()
    except cx_Oracle.DatabaseError as e:
        print("insertIntoUser Error:-", e)
        if cur:
            cur.close()
        if conn:
            conn.close()
    # finally:
    #     if cur:
    #         cur.close()
    #     if conn:
    #         conn.close()


def updateTime(email, timest):
    query = f"update usr set timest='{timest}' where email='{email}'"
    try:
        cur.execute(query)
        conn.commit()
    except cx_Oracle.DatabaseError as e:
        print("updateTime Error:-", e)
        if cur:
            cur.close()
        if conn:
            conn.close()


def updatePasswd(email, passwd):
    query = f"update usr set passwd='{passwd}' where email='{email}'"
    try:
        cur.execute(query)
        conn.commit()
    except cx_Oracle.DatabaseError as e:
        print("updatePasswd Error:-", e)
        if cur:
            cur.close()
        if conn:
            conn.close()

def getPasswd(email):
    query = f"select passwd from usr where email='{email}'"
    try:
        cur.execute(query)
        res = ''
        for result in cur:
            res = result[0]
        # conn.commit()
        return res
    except cx_Oracle.DatabaseError as e:
        print("getPasswd Error:-", e)
        if cur:
            cur.close()
        if conn:
            conn.close()

def getEmail(email):
    query = f"select email from usr where email='{email}'"
    try:
        cur.execute(query)
        res = ""
        for result in cur:
            res = result[0]
            # print("Didn't reach")
            # print("type ",type(res))
        # conn.commit()
        return res
    except cx_Oracle.DatabaseError as e:
        print("getEmail Error:-", e)
        if cur:
            cur.close()
        if conn:
            conn.close()

def getTimest(email):
    query = f"select timest from usr where email='{email}'"
    try:
        cur.execute(query)
        res=""
        for result in cur:
           res = result[0]
        return res
    except cx_Oracle.DatabaseError as e:
        print("getTimest Error:-", e)
        if cur:
            cur.close()
        if conn:
            conn.close()
# insertIntoUser("maza","naav","1237676","hgasdg@bsd.com","qwdiugiqw","11:12 PM");
# updatePasswd("hgasdg@bsd.com", "qwdiugiqwu")
# updateTime("hgasdg@bsd.com","11:12:01 PM")
# print(getPasswd("hgasdg@bsd.com"))
# print(getEmail("hgasdg@bsd.com"))
# print(getEmail("jghhvjhvj@fab.com"))
# print(getEmail("eanm@email.com"))
# print(type(getEmail("kjbkdg@jnak")))
# print(getPasswd("kjbkdg@jnak"))
# print(type(getPasswd("kjbkdg@jnak")))
# print(getTimest("kjbkdg@jnak"))
print(type(getTimest("kjbkdg@jnak")))