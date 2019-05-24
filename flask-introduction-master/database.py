import pymssql
conn = pymssql.connect(server='clientdev', user='TEAMBLR\SathishKumar', password='sa@123456', database='tempdb')  
cursor = conn.cursor()  
cursor.execute('SELECT * FROM samples')


def databases():
    for row in cursor:
     print(row)
