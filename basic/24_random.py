import random

choice = random.random()  # 0~1 사이의 랜덤의 소수값을 줌
choice = random.randint(1, 100)
print(choice)

set_a = set([])  # list를 set으로 변환
set_b = {1, 2, 3}
# while문을 써서 로또 길이 6보다 작을 때 계속 번호 추출하도록
lotto = set()  # set을 선언

while len(lotto) < 6:
  ball = random.randint(1, 45)
  lotto.add(ball)
lotto = sorted(lotto)
print(lotto)

# shuffle 함수를 이용한 로또번호 생성기
lotto = []
for i in range(1, 46):
  lotto.append(i)
print(lotto)

for i in range(45):
  rand = random.randint(0, 44)
  lotto[i], lotto[rand] = lotto[rand], lotto[i]
print(lotto[0:6])

# shuffle 메서드를 활용한 로또번호 생성기
random.shuffle(lotto)
print(lotto[0:6])