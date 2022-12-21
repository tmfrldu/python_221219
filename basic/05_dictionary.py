# 딕셔너리(dictionary) 자료형
# :: key-value
# :: key는 중복불가, value는 중복가능

dic_a = {
  'name': '홍길동',
  'grade': '1',
  'stdNo': '1',
  'mobile': '010',
}
dic_a['score'] = [98, 100, 89]  # 딕셔너리에 key:value 추가
print(dic_a)
print(dic_a['name'])

d1 = {
  0:"꽃", 1:"달", 2:"해"
} # 이런식으로 key값이 순차적일 경우 list를 활용하는 것이 낫다.
d1[0] = 8 # key의 중복으로 인해 해당 키값의 value가 8로 overwrite
d1[10] = 7 # 없는 경우 10:8로 추가(add)
print(d1)

for key in d1:
  print(key, d1[key]) # for문을 활용한 key value 출력

print('여기')
rev = []
for key in d1:
  rev.append(key)
print(rev)
rev.reverse()
print(rev)
print(f'{" 역정렬 ":=^20}')
# 만약 reversed()를 사용하면
# rev = reversed(d1.keys())

for key in rev:
  print(key, d1[key], end="\n")

print(f'{"정렬":=^20}')
rev = sorted(d1.keys())
for key in rev:
  print(key, d1[key], end="\n")


#💥💥 딕셔너리 관련 함수
print(d1.keys()) # d1의 key list 반환
print(d1.values()) # d1의 value list 반환
print(d1.items()) # list 안 (key,value)의 tuple형태로 반환
print(d1.get(2)) # key로 value 반환_ get()
print(d1[0], d1.get(0)) # <- key로 value값 받아오기
print(d1.get(100)) # None 출력
print(d1.get(100, 100)) # 키값이 없을 때 defaul값을 지정하면 그 값을 호출

print(1 in d1)  # 해당 key값이 딕셔너리 안에 있는지 확인하는 함수_in
print(1 not in d1)
