# 변수는 객체이다.
# python의 변수 할당은 call by ref.방식 _ value와 속성이 같으면 동일 ref로 할당되는듯

s1 = 'hello'
s4 = str('hello')
print(id(s1))
print(id(s4))
print(s1 is s4)
print('isalnum()',"TraninA10".isalnum()) # X.isalnum()문자열이 알파벳과 숫자로만 이루어졌는지 확인해주는 함수
print('isalpha()',"TraninA10".isalpha()) # 알파벳으로만 이루어졌는지
print('isadentifier()',"Tranin@A10".isidentifier())
# python내 유효한 식별자인지 확인_ 예약어x, 문자 or _로 시작, 문자, 숫자, _로만 이루어져야함
print('isdecimal()',"Tranin@A10".isdecimal()) # 문자열내 모든 문자가 10진수인지 확인
print('isdigit()',"3.141592".isdigit()) # 숫자로만 이루어졌는지, 소수점 안됨
print('isspace()'," ".isspace()) # 공백 여부 확인, '', ""은 안됨
print('islower()',"hello".islower()) # 문자열이 모두 소문자로 이루어졌는지 확인
print('isupper()',"HELLO".isupper()) # 문자열이 모두 대문자로 이루어졌는지 확인

i1 = 10
i2 = 20  # 숫자의 경우 value가 동일하면 동일한 ref를 갖게됨
print(i1, id(i1))
print(i2, id(i2))

a = [1, 2, 3]
print(id(a))
b = a  # shallow copy(종속적) _ ref를 복사 a=b
print(b, id(b))
a.append(4)
print(a, b)

# [:]를 사용해서 list copy
c = a[:]  # deep copy(독립적) _ 데이터만 복사 a!=c
# copy 모듈 사용_
from copy import copy
c = copy(a)       # deep copy_ 데이터만 복사
c = [1, 2, 3, 4]  # 똑같은 값을 넣어줘도 ref는 다름
print('**', a, id(a))
print('**', c, id(c))
a.append(5)
print(a, id(a))
print(c, id(c))
print(b, id(b))

print(f'{"변수선언의 다른 방법":=^20}')
# tuple
x, y = ('hello', 'world')  # 각각 x와 y에 대입 가능
x, y = 'hello', 'world'  # tuple은 괄호 생략 가능
(x, y) = 'hello', 'world'
(x, y) = ('hello', 'world')
print(x, y)
# list
x, y = ['hello', 'world']  # 각각 x와 y에 대입 가능
x, y = 'hello', 'world'
[x, y] = 'hello', 'world'
[x, y] = ['hello', 'world']
print(x, y)

a = b = 10  # 여러개의 변수에 같은 값 대입
print(a, b)

# 두변수의 값 바꾸기
a = 10
b = 20
print(a, b)
a, b = b, a
print(a, b)
