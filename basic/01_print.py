# print()
# help(print) # <- 기능 모르겠는 함수들은 help(함수)치면 알려줌
print(52)
print(52, 273, "Hello Python")
print(10,20,30)
print("Hello", "My name is", "KSG")
print()  # 한줄 띄우기

print("\t # printf처럼 사용하기")
print("number={0}, name={1}".format(1000, 'KSG'))
print ("%d %s" % (1000,"KSG"), end='.\n')
print("동해물과 백두산이 마르고 닳도록\n"
      "하느님이 보우하사 우리나라 만세")
print("""무궁화 삼천리 화려강산
      대한사람 대한으로 우리나라 만세""")  # 화면 그대로 출력

# print()의 속성(end, sep,
print(10,20, end="끝 \n") # end의 끝에 \n안해주면 다른 print()가 붙어서 출력
# import time
# for i in range(10):
#       print(i, end = ' ')
#       time.sleep(1)
print()
print(10,20,30,40,50, sep="💘") # sep은 약간 구분자 느낌
with open('./hello.txt', 'w') as f:
      print('Hello Python', file=f)
f = open('./hello.html', 'r')
lines = f.readlines()
for line in lines:
      print(line)
f.close()
# flush 스트림을 강제할 것인지에 대한 여부 (True, False)
# output이 Flushed(True)인지 Buffered(False)인지 지정. 기본값은 False
print("#특수문자(escape letter)" )
print("# \\n 줄바꿈 \\t 탭 \\' \\\\ \\\" ")
print("'Ice Americano'", '"얼죽아"') #print로 쌍따옴표, 따옴표 출력
print("\"쌍따옴표\"\'escape문자\' \\") # \뒤에 특수문은 그대로 출력되는듯


