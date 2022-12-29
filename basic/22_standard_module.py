from my_util import *

# 파이썬의 모듈(표준모듈, 외부모듈)

# 내장형 함수
print(abs(-10))  # 절대값 돌려주는 함수
# all 모두 만족할때
print("all([1, 2, 3]):", all([1, 2, 3]))  # 모든 요소가 true(!=0)일때 true를 반환
print("all([0, 2, 3])", all([0, 2, 3]))
# any 하나라도 만족할때
print('any([0, 0, 3])', any([0, 0, 3]))  # 하나의 요소라도 true이면 true반환
print('any([0, 0, 0])', any([0, 0, 0]))  # 모두 False여야 False를 반환

# chr 아스키 코드값을 문자로 출력
print(chr(97))

# dir_ 매개변수의 타입에 따라 가지고 있는 변수나 함수를 출력
# print(dir([1,2,3]))  # list가 갖고 있는 메서드 보여줌
# print(dir({'key':'value'}))

# divmod(a,b)  a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
pr("divmod(10,3)")

# enumerate
for i, item in enumerate([1, 2, 3]):
  print(f'{i}:{item}')

pr("eval('all([1, 2, 3])')")

pr('hex(234)')

# list [1,2,3,4]의 전체 요소에 2를 곱한 리스트 출력하기
# 1) 함수처리
def two_times(l):
  result = []
  for i in l:
    result.append(i * 2)
  return result

print(two_times([1, 2, 3, 4]))

# 2) map() 활용_ 콜백함수 처리
def two_times(x):
  return x * 2

print(list(map(two_times, [1, 2, 3, 4])))

# 2) map()과 lambda 식 활용
print(list(map(lambda x: x * 2, [1, 2, 3, 4])))

print(max([1,2,3]))

# import tkinter as tk
# from tkinter import simpledialog
#
# application_window = tk.Tk()
#
# answer = simpledialog.askstring(
#   "Input", "What is your first name?",
#   parent=application_window)
# print('answer: ',answer)

# from tkinter import messagebox

# messagebox.showinfo("알림","정보")
# messagebox.showerror("에러","문제")
# messagebox.showwarning("경고","조심")


import math

print(math.sin(1))
