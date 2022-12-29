print("Life" "is" "Good")
print("Life"+"is"+"Good")
print("Life","is","Good")  # 문자열과 띄어쓰기를 할때는 ,이용

f = open('./hello.txt', 'r')  # 읽기모드
while True:
  line = f.readline()
  if not line:
    break
  print(line)

f.close()

f = open('./hello.txt', 'w')  # 쓰기모드
str = 'Happy New Year \n'
f.write(str)
f.close()

f = open('./hello.txt', 'a') # 추가모드
str = '건강하세요 \n'
f.write(str)
f.close()

with open('./hello.txt', 'w') as f:
  f.write("The File")

def fopen(filename):
  f = open(filename, 'r')
  lines = f.readlines()
  for line in lines:
    print(line)
  f.close()

def fwirte(filename, str):
  with open(filename, 'w') as f:
    f.write(str + '\n')

def fadd(filename, str):
  with open(filename, 'a') as f:
    f.write(str + '\n')

fopen('./hello.txt')

fwirte('./hello.txt', "fwrite")
fadd('./hello.txt', "fappend")

fopen('./hello.txt')