import tkinter.ttk
from student_management.dao.dao_student import StudentDao
from student_management.vo.student_vo import Student
from student_management.util import ui_util as tool
from student_management.ui.info_wd import UserInfo


class ListWindow:
  getValue = None

  def __init__(self):
    self.dao = StudentDao()

    self.list = tkinter.Tk()
    self.list.title("Student List")

    self.lbl = tkinter.Label(self.list, text="Student List")
    self.lbl.pack()

    self.getValue = None

    # treeview 표
    self.trv = tkinter.ttk.Treeview(self.list,
                                    columns=["stdno", "이름", "ID"],
                                    displaycolumns=["stdno", "이름", "ID"])
    self.trv.pack()

    self.trv.column("#0", width=100)
    self.trv.heading("#0", text="index")

    self.trv.column("#1", width=100, anchor="center")
    self.trv.heading("stdno", text="stdno", anchor="center")

    self.trv.column("#2", width=150, anchor="center")
    self.trv.heading("이름", text="이름", anchor="center")

    self.trv.column("#3", width=150, anchor="center")
    self.trv.heading("ID", text="ID", anchor="center")

    self.trv.bind('<ButtonRelease-1>', self.click_item)

    trv_list = self.dao.get_all()
    if trv_list != None:
      for i in range(len(trv_list)):  # iid =index id
        self.trv.insert('', 'end', text=i, values=trv_list[i], iid=str(i) + ")")
    tool.center_win(self.list, 540, 300)
    self.list.resizable(False, False)

    getValue = ListWindow.getValue

    self.list.mainloop()

  def click_item(self, event):
    selectedItem = self.trv.focus()
    getValue = self.trv.item(selectedItem).get('values')
    print('getValue:', getValue)

    tmp = f'{getValue[1]},{getValue[2]},{getValue[3]},{getValue[0]}'
    print('tmp:', tmp)
    std = Student.from_str(tmp)
    self.list.destroy()
    UserInfo(std)






# def __del__(self):
#   from student_management.ui.login_wd import LoginWindow
#   LoginWindow()
