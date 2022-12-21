# 리스트(list) 자료형
#  :: muttable
#  :: 순서 있으며, 중복 허용

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_a = ['Life', 'is', 'Good', 'and', 'Happy']
list_a = ['홍길동', '90', '100', '90']

print('list_a:', list_a)
print(list_a[0])
for key in list_a:
  print(key)

for i in range(0, len(list_a)): print(str(i) + ")", list_a[i])  # 명령이 하나일때는 한줄로 축약가능

print(list_a[1:30])  # slicing은 인덱스 범위가 벗어나도 출력이 되지만
# print(list_a[30]) # 해당 인덱스를 찾을때는 out of range로 error

list_b = list(range(0, 10))
print(list_b)

list_a[0] = '고길동'
print(list_a)  # list_a[0]의 value가 바뀐것을 확인할수 있다. list:: muttable
# list는 자료에 대한 추가, 수정이 가능하다.

lists = [
  ['홍길동', '90', '100', '90'],
  ['고길동', '91', '90', '90'],
  ['강길동', '89', '95', '90'],
  ['김길동', '70', '92', '90']
]
print(lists[0])
print(lists[1][3])  # 이중 리스트의 내부 인덱스 값에 접근할때 (lists내 첫번째 리스트의 3번째 인덱스 값)
print()

for i in range(0, len(lists)):
  sum = 0
  for j in range(0, len(lists[i])):
    if j != 0:
      print(",", end="")
      sum += int(lists[i][j])

    # print("%3s" % lists[i][j], end="")  # %3s -> 3칸의 공백에 글자는 오른쪽 정렬 _문자열 포맷코드 활용
    print("{0:>3}".format(lists[i][j]), end="")  # 모두 동일한 화면 출력_ format함수활용
    # print(f"{lists[i][j]:>3s}", end="")  # f 문자열 포매팅 활용
  print(", %3d" % sum)

# 2차 배열
lists2 = [[0 for col in range(5)] for row in range(5)]
for i in range(0, len(lists)):
  for j in range(0, len(lists[i])):
    lists2[i][j] = lists[i][j]
    if j != 0:
      lists2[i][len(lists[i])] += int(lists[i][j])
      lists2[len(lists)][j] += int(lists[i][j])
      lists2[len(lists)][len(lists[i])] += int(lists[i][j])

for i in range(0, len(lists2)):
  for j in range(0, len(lists2[i])):
    if j != 0:
      print(",", end="")
    if i == len(lists2) - 1 and j == 0:
      lists2[i][j] = "합계"
      print("{0:6^}".format(lists2[i][j]), end="")
    else:
      print("{0:>5}".format(lists2[i][j]), end="")

  print()

a = [1, 2, 3]
b = list(range(3, 7))
print(a, '', b)
print(a + b)  # list 더하기_ 중복허용, 순서가 있음
print(b + a)
c = a + b
c = b + a
print(c)

print(a * 3)  # list는 곱셈 연산도 된다_ list의 반복

print(len(a))  # list의 길이 구하는 함수:: len()

b[0] = 0
print(b)  # list 수정
# list 삭제
del b[0]  # 함수 del을 사용
print(b)
del b[:1]  # slicing을 활용해 list 요소 삭제
print(b)
print()

# list 관련 함수들
print(f'{"list 관련 함수":=^20}')
print()
b.append(4)  # list의 마지막에 추가 _ JS의 push와 동일한듯
print(b)

b.sort()  # list의 요소를 순서대로 정렬
print(b)

list_a = ['Life', 'is', 'Good', 'and', 'Happy']
list_a.sort()  # 문자도 정렬
print(list_a)  # asciicode 순서대로 정렬

list_a.reverse()  # 현재의 list를 그대로 뒤집음
print(list_a)  # ['is', 'and', 'Life', 'Happy', 'Good']

print(list_a.index('Life'))  # index(요소)함수는 요소의 위치 값을 반환
print(c)
print(c.index(3))
a.insert(0, 4)  # insert 함수:: list 0번째 위치에 4 삽입
print(a)
a.insert(0, 4)
print(a)
a.insert(2, 6)
a.insert(20, 6)  # list의 인덱스가 넘으면 끝자리로 반영
print(a)
a.remove(6)  # list의 첫 6을 삭제
print(a)  # [4, 4, 1, 2, 3, 6]
# pop()은 매개변수 없을 시, 맨 끝요소를 반환 후 list 내에서 삭제
print(a.pop())  # 6 출력
print(a)  # [4, 4, 1, 2, 3] 맨 끝의 6이 삭제된 것을 확인할수 있음
print(a.pop(0))  # 매개변수 있을 시 지정요소 리턴과 삭제 _ index[0]=4 리턴 및 삭제
print(a)    # [4, 1, 2, 3]
print(a.count(1)) # list에 포함된 요소 1의 개수 counting
print(c, c.count(3)) # [3, 4, 5, 6, 1, 2, 3] 2

# list 확장(extend)
d = []
d.extend(a) # extend(a) 에서 괄호안은 list만 넣을 수 있다.
# d += a
print(d)
print(1 in d) # d의 요소로 1이 있는지 -> True 반환
print(1 not in d) # d의 요소로 1이 없냐 -> False 반환

d.clear() # list 내부를 싹 비워버림
print(d)
