import sys, time, threading, random

import tkinter as tk
from tkinter import simpledialog


class Bomb(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.life = random.randint(1, 2)
    self.state = False

  def run(self):
    for i in range(10, 0, -1):
      if self.state: break
      print(i)
      time.sleep(0.3)
    print("BBoom!!")
    sys.exit()

  def choose(self, line):
    try:
      line = int(line)
    except Exception as e:
      line = 1
    print(f'{line}을 선택했습니다.')
    if (self.life == line):
      print("살았습니다.")
    else:
      print("으악")
    self.state = True


