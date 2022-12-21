# 자료형(변수)의 종류
# 기본 자료형
# - bool
# - 정수형_int, 실수형_float  <- 숫자형
# - str_문자열

# 변수명 규칙
# 예약어 안됨
# _, 영문자 시작(숫자 안됨)
# 특수문자, 공백 불가
# CamelCase는 클래스에 적용
# snake_case는 변수나 함수에 적용

print('# 숫자형')
a = 10  # int
a = 10.234  # float
a = 0b101  # 0b or 0B로 시작하면 2진수(Binary)
a = 0O12  # 0o or 0O로 시작하면 8진수(Octal)
a = 0x2a  # 0x or 0X로 시작하면 16진수(Hexadecimal)
a = 123e2  # en or En로 시작하면 10의 n승
a = 123E-2  # 1.23 123*10-2승
print(a)
print(type(a))
print()

# 10진수_decimer를 2진수로 변경
print('10진수 10을 2진수 값으로 반환:', bin(10))
# 10진수를 8진수로 변경
print('10진수 10을 8진수 값으로 반환:', oct(10))
# 10진수를 16진수로 변경
print('10진수 10을 16진수값으로 반환:', hex(10))
# n진수를 10진수로 변경
print('8진수 17을 10 진수값으로 반환:', int('017', 8))
print('2진수 0b101 10진수값으로 반환:', int('101', 2))
print('16진수 0xa1 10진수값으로 반환:', int('a1', 16))
print('int(num, n)은 n진수의 num 값을 10진수의 값으로 반환한다')
print()

print(format(10, 'b'))  # binary
print(format(10, 'o'))  # octa
print(format(10, 'x'))  # hexa
print(format(10, 'X'))  # hexa(capital)
print(format(10, 'd'))  # decimal
print(format(10, '#b'))  # python의 진수표기법
print(format(10, '#o'))
print(format(10, '#x'))
print(format(10, '#X'))
print(format(10, 'd'))
print()

print('#사칙 연산 +,-,*,/')
b = 10;
c = 20;
print(b + c);
print("몫 연산자 //", end=" :: ")
print(3 / 2)  # <- 일반 나눗셈 연산 1.5 출력
print(3 // 2)  # 1 몫인 1만 반환
print("나머지 연산자 %", end=" :: ")
print(3 % 2)
print("제곱 연산자 **", end=" :: ")
print(3 ** 2, 10 ** 3, "x**y")  # x의 y 제곱 값 출력
print("#비트 연산자 &", end=" :: ")
print(bin(0b010 & 0b101))  # 논리곱 & 1&1만 true(1)
print("#비트 연산자 |", end=" :: ")
print(bin(0b010 | 0b101))  # 논리합 | 둘중에 하나만 1이어도 true(1)
print("#비트 연산자 ^", end=" :: ")
print(bin(0b010 ^ 0b101))  # 배타적논리합 ^ 두값이 서로 달라야 true(1)
print("#비트 연산자 ~", end=" :: ")
print(bin(~0b101))  # 반전연산자 보수 어쩌고 이해 못함

print("#shift 연산자 >>,<<")
print("%s<<2 => %s" % (bin(2), bin(2 << 2)))  # shift

power = True
print(power, type(power))
print("#비교 연산자(>,<,>=,<=,==)와 논리 연산자(and, or, not)")
print(3 < 1 or 2 > 1)  # js의 ||와 동일
print(not power)  # js의 !와 동일

print()
print()

print('# 문자열 str')
a = "Hello Python"  # 쌍따옴표, 홑따옴표 다 문자열
print(type(a))  # str
# a[1] = 'a' -> error발생_문자열 배열은 immutable 자료형으로 안의 value값의 수정이 불가

print('# 문자열 연산자')
print(a + " hello world")  # str의 plus 연산
# print(a + 123) #<- str+숫자 -> TypeError, python에서는 같은 type의 연산만 가능하다.
print('go' * 3)  # go가 3번 출력됨 -> gogogo
print("Hello Python"[0])  # indexing 배열의 0번째 value값 출력 -> H
print("Hello Python"[-1])  # 배열의 끝은 -1 -> n
# print("Hello Python"[20]) # out of range error 발생

# slicing:: 문자열 슬라이싱
print("Hello Python"[0:4])  # slicing 배열의 0에서 4의 자리 앞부분까지 _JS의 substring이랑 같음
print("Hello Python"[6:])  # 6부터 끝까지
print("Hello Python"[:5])  # 0에서 4까지
print("Hello Python"[0:20])  # error 미발생, 그냥 다 출력

print(len("Hello Python"))
print("I eat %s" % 'apple')  # 1개의 값 넣기
print("I eat %d %s" % (3, 'apple'))  # 2개이상 값 넣기
ch = 'A'
print("%s Asccii Code is %d" % (ascii(ch), ord(ch)))
print("%d is %s" % (ord(ch), chr(ord(ch))))
print(ascii('''

\n

'''))  # 줄바꿈은 \n으로 표기
print(ord('\n'))  # \n은 ascii code로 10
print(ord('\t'))  # \t은 ascii code로 9

# 문자열 포맷 코드
num = 10
print("%d의 8진수는 %o, 16진수는 %x" % (num, num, num))
print('%c 는 문자 1개입니다.' % 'z')  # %c는 문자 1개만 대입
print('Error is %d%%' % 98)  # 문자열포맷코드를 사용하면서 %를 표기하고 싶으면 %%로 처리
print("%10s|" % 'hi')  # 10칸의 자리에 마지막에 hi 출력
print("%-10s|" % 'hi')  # 10칸의 자리 중 앞에 hi출력
print('%0.4f' % 3.141592)  # 소수점의 네번째 짜리까지 출력, 5자리에서 반올림 처리
print('%10.4f' % 3.141592)  # 10은 총 자릿수(. 포함)
# format 함수를 사용한 포매팅
print("I eat {0}".format('apple'))
print("I eat {0} {1}".format(3, 'apple'))
print("I eat {num} {item}".format(num=3, item='apple'))
print()
# 공백(10칸) 내 정렬
print("|{0:=^20}|".format(' format '))
print("|{0:<10}|".format('hi'))
print("|{0:>10}|".format('hi'))
print("|{0:^10}|".format('hi'))
# 공백 채우기
print("|{0:=^10}|".format('hi'))  # |====hi====| -> 가운데정렬 공백은 =
print("|{0:0>8}|".format('10'))  # |00000010| -> 오른쪽정렬 공백은 0
print("|{0:10.4f}|".format(3.141592))  # 총 10자리 중 소수점은 4자리까지 표현
print("{{}}는 클래스이다.".format())

print(f'{" f문자열 포매팅 ":=^20}')
# f문자열 포매팅
city = 'Seongnam'
print(f"나의 살던 고향은 \"{city}\"") # JS의 ``표기법 같은 느낌 Python 3.6부터 가능
d = {'city': '부산', 'gu': '부산진구'} # 딕셔너리 활용
print(f"내가 사는 곳은 {d['city']} {d['gu']} 입니다")
print(f"|{3.141592:0.4f}|")
print(f"|{3.141592:10.4f}|")
print(f"{{}}는 클래스이다.")
print()

print('===문자열 관련 함수===')
print("hello world".count('l')) # l의 갯수 counting
print("hello world".find('l'))  # l의 위치 index 반환, 없으면 -1 반환
print("hello world".index('l')) # l의 위치 index 반환, 없으면 error 발생
print(",".join('12345'))  #문자열 사이에 ,를 삽입
print('hello'.upper())  # 소문자 -> 대문자
print('WORLD'.lower())  # 대문자 -> 소문자
print('hello world'.capitalize()) #첫문자만 대문자로 출력
print('hello world'.split(' ')) # 공백을 기준으로 문자열을 나눔, split 후에는 list 자료형 됨
# split() 괄호 안에 아무값도 없으면 공백(스페이스, 탭, 엔터 등)을 기준으로 나눔
l = 'hello world'.split(' ')
for i in l:
  print(i.capitalize(), end=" ") # 단어의 첫자를 대문자로 변경하는 for문
print()

print('   strip word   '.strip())  # strip() 양쪽의 공백을 없앰
print('   strip word   '.lstrip()) # lstrip() 왼쪽의 공백을 없앰
print('   strip word   '.rstrip()) # rstrip() 오른쪽의 공백을 없앰



