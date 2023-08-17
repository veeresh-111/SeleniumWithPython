# select

select_query="select * " \
             "from student " \
             "where sno=1"

import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="vskroot", database="mydb")
    curs = con.cursor()  # create curser for temparary memory
    curs.execute(select_query)  # execute query through curser

    for row in curs:
        print(row[0],row[1],row[2])
    con.close()  # close connection

except:
    print("Connection unsuccessful....")


print("Finished........")