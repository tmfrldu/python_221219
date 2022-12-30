import sqlite3


class DaoSet:
  def conn_db(self):  # sqlite를 연결하는 객체 def conn_db
    self.conn = sqlite3.connect('d:/classPython/workspace/python_221219/db.sqlite', isolation_level=None)
    return self.conn

  def conn_close(self):  # database의 커넥션을 끊어주는 객체(?)
    try:
      if self.conn != None:   # 무조건 끄는게 아니라 값이 있을때 close 되도록 조건문
         self.conn.close()
      if self.cursor != None:
        self.cursor.close()
    except Exception as e:
      print(e)