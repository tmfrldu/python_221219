# casting_형변환 함수
# 형변환 함수
print(int("52"))
print(str(3.141592))

# print(int("3.141592"))  # float이므로 typeError 발생
print(float("3.141592"))
print(int(3.141592))  # float -> int 소수점 자리는 절삭
print(int(3.7))  # float -> int 소수점 자리는 절삭
print()

# math 함수
import math

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sum(a))  # list 요소 다 더함
print(max(a))  # list 요소 중 가장 큰값 반환
print(min(a))  # list 요소 중 가장 작은값 반환

print(math.ceil(3.141592))  # 절상 4출력
print(math.ceil(-3.141592))  # 절상 -3출력

print(math.floor(3.141592))  # 절삭
print(math.floor(-3.141592))  # 절삭

# str 타입의 숫자의 홀수 짝수 구분
num = '-100'
print('짝수' if num[-1] in '02468' else '홀수')
print('음수' if num[0] == '-' else '양수')

# 숫자 일때 홀수 짝수 구분
num = 30
print('짝수' if num % 2 == 0 else '홀수')

print(f'{" Date 날짜/시간 관련 ":=^20}')
import datetime as dt

now = dt.datetime.now()
print("{}년".format(now.year))
print("{}월".format(now.month))
print("{}일".format(now.day))
print("{}시".format(now.hour))
print("{}분".format(now.minute))
print("{}초".format(now.second))

print("{}년 {}월 {}일".format(now.year, now.month, now.day))
print(now.strftime("%Y-%m-%d %I:%M:%S %A"))
# %H는 24시, %I는 12시, %B 영어 월, %h 영어 월 줄인거
# %a 영어요일 짧게, %p am/pm
print("월화수목금토일"[now.weekday()])
print(" 월화수목금토일"[now.isoweekday()])

from datetime import date

d = date.fromordinal(15200)
print(d)
d1 = dt.date(2022, 12, 25)
print(d1.isoweekday())
