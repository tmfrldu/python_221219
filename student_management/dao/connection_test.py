import sqlite3
# print(sqlite3.version)
# print(sqlite3.sqlite_version)

conn = sqlite3.connect('../../db.sqlite', isolation_level=None)

c = conn.cursor()

c.execute("delete from student ")
conn.commit()

c = conn.cursor()
sql = "update sqlite_sequence set seq=? where name=? "
d = (0, 'student')
c.execute(sql, d)
conn.commit()

# try:
#   ex = c.execute(f"insert into student(id, name, pass) "
#             f"values('user2','사용자2','1' )")
#   print(type(ex))
# except Exception as e:
#   print('>>>',c.lastrowid)
# finally:
#   print('>>>', c.lastrowid)
# conn.commit()
#
# c = conn.cursor()
c.execute("select * "
          "from student")
print(c.lastrowid)
# print(type(c.fetchall())) # list
print(c.fetchall())

# result = c.execute(f"select  * from student "
#                    f"where id='user2' and pass='1' ")
# print(result.fetchone())