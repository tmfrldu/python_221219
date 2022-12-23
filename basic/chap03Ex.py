# 1)
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")  # 여기서 만족하므로 조건문을 빠져나옴
elif "need" in a: print("need")
else: print("none")

# 2)
result = 0
i = 1
while i <= 1000:
  if i % 3 == 0:
    result += i
  i += 1

print(result)
print()

# 3)
i = 0
while True:
  i += 1
  if i > 5: break
  print('*' * i)
print()
print()

# 4)
for i in range(1, 101):
  print(i)

print()

# 5)
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
# for score in A: total += score
total = sum(A)  # list내 요소의 값을 다 더해주는 함수 sum() 이용가능
average = total / len(A)

import statistics
average = statistics.mean(A) # list내 요소값의 평균을 구하는 함수_statistics.mean()

print(f'total: {total}, average: {average}')
print()

# 6) 조건을 활용한 리스트 내포_(List comprehension)
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
  if n % 2 == 1:
    result.append(n * 2)
print(result)

numbers = [1, 2, 3, 4, 5]
result = [(n * 2) for n in numbers if n % 2 == 1]  # python에만 있는 리스트내포(List comprehension)
fruits = ['사과', '자두', '초콜렛', '바나나', '체리']
output = [fruit for fruit in fruits if fruit != '초콜렛']
print(output)
print(result)
