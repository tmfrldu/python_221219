# 튜플(tuple) 자료형
# :: immutable
# :: ()를 사용
# :: 순서있으며, 중복 허용

t1 = ()
t2 = (1,)  # tuple에서 요소가 하나만 있을 경우 뒤에 꼭 , 를 붙여줘야한다.
t3 = (1, 2)
t4 = 1, 2, 3  # 괄호 생략 가능
t5 = ('a', 'b', ('ab', 'cd'))
print(t5)

for item in t5:
  print(item, end=', ')
print()
for i in range(0, len(t5)):
  print(i, t5[i], sep=")", end=" ")
print()

# t4[0] = 0  #-> error, tuple은 값의 수정 불가
# del t4[0]  # -> error, 삭제 불가
print(t4)

t1 = tuple(range(10))
t1 = tuple(range(2, 10))
t1 = ((0 for col in range(4)) for row in range(3))

print(f'{"이중 for문":=^20}')
for r in t1:
  idx = 0
  for item in r:
    if idx != 0:
      print(",", end=" ")
    idx += 1
    print(item, end=" ")
  print()

t1 = (1, 2, 'a', 'b',)
print(t1[2])  # tuple indexing
print(t1[:2])  # tuple slicing
t2 = 3, 4,
print(t1 + t2)
print(t1)
print(t2)
t1 = t1 + t2  # t1의 값이 바뀌는게 아니라 아예 재할당이 되어버림
print(t1)

print(len(t1))
print(t1 * 2)
