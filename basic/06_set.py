# 집합(set) 자료형
# :: 중복불허, 순서 없음(출력할때마다 순서 지맘대로 나옴)

s1 = set([1,2,3])

s1 = set("Hello")
print(s1)
for item in s1:
  print(item, end=' ')
print()

c = set(c for c in 'abc')
print(c)

l1 = sorted(s1)
for item in l1:
  print(item, end=' ')
print()

print(f'{"set의 교집합, 합집합, 차집합 구하기":=^30}')
# set의 교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print('합집합',s1 | s2)  # s1과 s2의 합집합
print('union()',s1.union(s2)) # union()를 이용한 합집합
print('교집합',s1 & s2)  # s1과 s2의 교집합
print('intersection()',s1.intersection(s2))  # intersection()을 이용한 교집합
print('차집합',s1 - s2)  # s1에서 s2를 차집합
print('difference()',s1.difference(s2)) # difference()를 이용한 차집합
print('차집합',s2 - s1)  # s2에서 s1를 차집합
print('difference()',s2.difference(s1)) # difference()를 이용한 차집합

# 집합 자료형 관련 함수
s1 = set([1,2,3])
# 한개 값 추가하기_add()
s1.add(4)
s1.add(4)
print(s1) # 중복을 허용하지 않음

# 여러개의 값 추가하기_update()
s1.update([4,5,6])
print(s1)

# 특정 값 제거하기_ remove()
s1.remove(6)  # 없는 값 지우라고하면 에러남
print(s1)