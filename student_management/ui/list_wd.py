import tkinter
import tkinter.ttk

root = tkinter.TK()
root.title("Student")
root.geometry('540x300+100+100')               # 위치와 사이즈
root.resizable(False, False)

lbl = tkinter.Label(root, text="Student List")
lbl.pack()

tv = tkinter.ttk.Treeview(root,
                                columns=["순번", "이름", "ID", "Password"],
                                  displaycolumns=["순번", "이름", "ID", "Password"])
tv.column("#0", width=100,)
tv.heading("#0", text="index")
