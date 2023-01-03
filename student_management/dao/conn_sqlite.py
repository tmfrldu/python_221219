# module 방식으로 데이터베이스 연결하는 방식
import sqlite3

conn = sqlite3.connect(
  '/db.sqlite'
  , isolation_level=None)

def get_all():
  c = conn.cursor()
  rs = c.execute("select * from student ")
  return rs.fetchall()

def insert_one(std):
  c = conn.cursor()
  c.execute(f"insert into student (id, name, pass) "
            f"values('{std.id}','{std.name}','{std.pw}' )")
  conn.commit()
  return c.lastrowid

def login_check(std):
  c = conn.cursor()
  rs = c.execute(f"select  * from student "
            f"where id={std.id} and pass={std.pw}")
  return rs.fetchone()
