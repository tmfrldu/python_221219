import tkinter
from tkinter import *
from tkinter.filedialog import *
from tkinter import scrolledtext


def new_file():
  text_area.delete(1.0, END)


def save_file():
  f = asksaveasfilename(
    initialfile='noname.txt',
    defaultextension='.txt',
    filetypes=[('Text Files', '.txt',)])
  save_tmp = str(text_area.get(1.0, END))
  with open(f,'w', encoding='UTF-8') as file:
    file.write(save_tmp + "\n")

def open_file():
  f = askopenfilename(initialdir='/',
                      title="Select a file",
                      filetypes=[('Text Files', '.txt'),
                                 ('Python Files', '.py')])

  text_area.delete(1.0, END)
  with open(f, 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    str = ''
    for line in lines:
      str += line + "\n"
    text_area.pack()
    text_area.insert(tkinter.CURRENT, str)

def info():
  info_view = Toplevel(window)
  info_view.geometry('300x50+350+400')
  info_view.title('Maker: KSG')
  lb = Label(info_view, text="널 위해 준비했어!!")
  lb.pack()


window = Tk()
window.title('MyNotepad')
window.geometry('400x400+300+300')
window.resizable(0, 0)
# 메뉴프레임 생성
menu = Menu(window)
# 첫번째 메뉴
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label='New', command=new_file)
menu_1.add_command(label='Open', command=open_file)
menu_1.add_command(label='Save', command=save_file)
menu_1.add_separator()
menu_1.add_command(label='Close', command=window.destroy)
menu.add_cascade(label='File', menu=menu_1)

# 두번째 메뉴
menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="Info", command=info)
menu.add_cascade(label='help', menu=menu_2)

# 텍스트 추가하기
# text_area = Text(window)
text_area = scrolledtext.ScrolledText(window)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

# 메뉴 본창에 붙이기
window.config(menu=menu)

window.mainloop()
