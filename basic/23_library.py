import sys
print(sys.argv)
print('sys')
# sys.exit()

print('강제종료 안됨')

print(sys.path)

import pickle

f = open('test.txt', 'wb')  # wb=write buffer
data = {1: 'python', 2: 'tkinter'}
pickle.dump(data, f)
f.close()

f = open('test.txt', 'rb')
data = pickle.load(f)
print(data)

import os

os.chdir('c:')
print(os.getcwd())
f = os.popen("dir")
print(f.read())

import calendar

calendar.prmonth(2022, 12)
print(calendar.monthrange(2023, 2))
