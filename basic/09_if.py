# if 조건:
#   실행문
a = 100
# a = int(input('점수를 입력하세요'))
result = ''
if a > 100:
  result = '잘못된 점수가 입력되었습니다'
elif a >= 90:
  result = 'A'
elif a >= 80:
  result = 'B'
elif a >= 70:
  result = 'C'
elif a >= 60:
  result = 'D'
else:
  result = 'F'
print('학점: ', result)

# and, or, not

a = 1
if a in (1,2,3) and a != 0:
  pass  # 조건은 설정했지만 수행할 동작이 아직 미정일때 활용
  raise NotImplementedError  # 동작이 미정인 곳에 강제적으로 에러 발생
  # print('포함')
else:
  print('부재')

print('부재' if a not in [1,2,3] else '포함')  # list
print('부재' if a not in (1,2,3) else '포함')  # tuple
print('부재' if 'money' not in ['show','me','the','money'] else '포함')  # 문자열 list

message = '포함' if a in [1,2,3] else '부재'
print(message)