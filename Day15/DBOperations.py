# insert , update, delete

insert_query="insert into student values(108,'kim',80)"
update_query="update student set sname='Mary' where sno=108"
delete_query="delete from Student where sno=108"

import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", port=3307, user="root", passwd="vskroot", database="mydb")
    curs = con.cursor()  # create curser for temparary memory
    curs.execute(delete_query)  # execute query through curser
    con.commit()  # commit transaction
    con.close()
except:
    print("Connection unsuccessful....")


print("Finished........")
