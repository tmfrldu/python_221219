import bomb
import tkinter as tk
from tkinter import simpledialog

b = bomb.Bomb()
b.start()
print(b.life)

application_window = tk.Tk()
answer = simpledialog.askstring(
  "Input", "1과 2중에 골라라",
  parent=None)
b.choose(answer)