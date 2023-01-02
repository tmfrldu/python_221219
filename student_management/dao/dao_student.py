from student_management.dao.dao_set import DaoSet as dao


class StudentDao(dao):   # dao_set의 dao를 상속
  def __init__(self):
    self.conn = dao.connect(self)
    self.cursor = self.conn.cursor()

  def __del__(self):
    try:
      if self.conn != None:
        self.conn.close()
      if self.cursor != None:
        self.cursor.close()
    except Exception as e:
      print(e)

  def get_all(self):
    rs = self.cursor.execute("select * from student ")
    return rs.fetchall()

  def insert_one(self, std):
    self.cursor.execute(f"insert into student (id, name, pass) "
                        f"values('{std.id}', '{std.name}', '{std.pw}' )")
    self.conn.commit()
    return self.cursor.lastrowid

  def login_check(self, std):
    rs = self.cursor.execute(f"select  * from student "
                   f"where id ='{std.id}' and pass='{std.pw}'")
    return rs.fetchone()

