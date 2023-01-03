import sqlite3

class DaoSet:
  def connect(self):
    self.conn = sqlite3.connect(
      'd:/classPython/workspace/python_221219/student_management/db.sqlite'
      , isolation_level=None)
    return self.conn

  def disconnect(self):
    try:
      if self.conn != None: self.conn.close()
      if self.cursor != None: self.cursor.close()
    except Exception as e:
      print(e)

