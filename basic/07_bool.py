# bool
# :: True, False를 나타내는 자료형

a = True
print(type(a))

print(f'{"자료형의 참과 거짓":=^20}')
# str의 True, False
print('str', bool(''))  # False
print('str', bool('hello'))  # True
# list의 True, False
print('list', bool([1]))  # True
print('list', bool([]))  # False
# tuple의 True, False
print('tuple', bool((1,)))  # True
print('tuple', bool(()))  # False
# 숫자의 경우 0이 아닌 숫자는 모두 False를 반환
print('number', bool(0))  # False
print('number', bool(-123456))  # True
# dictionary
print('dic', bool({}))  # False
print('dic', bool({'a': 'b', 'b': 20, 'c': 10}))  # True
# set
print('set', bool(set([1, 2, 3])))  # True
print('set', bool(set()))  # False

print('비교연산자',2>1) # 비교연산자
print('조건문', bool(1 and 0 or 0 and 1) ) # 조건문

a = [1,2,3,4]
while a:
  print(a.pop(), end=' ')
