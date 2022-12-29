import sqlite3

conn = sqlite3.connect('../db.sqlite', isolation_level=None)

c = conn.cursor()

def get_all():
  rs = c.execute("select * from 'student' ")
  return rs.fetchall()
def insert_one(std):
  c.execute(f"insert into student (id, name, pass) "
            f"values('{std.id}', '{std.name}', '{std.pw}' )")
  conn.commit()
  return c.lastrowid

def login_check(std):
  rs = c.execute(f"select  * from student "
            f"where id ={std.id} and pass={std.pw}")
  return rs.fetchone()

