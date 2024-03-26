Python 3.13.0a4 (tags/v3.13.0a4:9d34f60, Feb 15 2024, 17:00:30) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#연습문제 1번
score=int(input("점수를 입력하세요:"))
점수를 입력하세요: 80
if score >=90 :
    print("장학생", end='')
elif score >=60 :
    print("합격", end='')
else :
    print("불합격", end='')

합격
#연습문제 2번
## 답은 3번, res = '짝수' if num %2==0 else'홀수'

#연습문제 3번
nn=[100, 200, 300, 400, 500]
nn[1]=777
print(nn)
[100, 777, 300, 400, 500]
nn[1]=[444, 555]
print(nn)
[100, [444, 555], 300, 400, 500]
nn[1:4]=[444, 555]
print(nn)
[100, 444, 555, 500]
nn[2:]=[]
print(nn)
[100, 444]

#연습문제 4번
a=0
for num in range(3333, 10000):
    if num % 1234==0:
        continue
    if a+num>=100000:
        break
    a+=num

...     
>>> print(a)
97063
>>> 
>>> #연습문제 5번
>>> hap=0
>>> n=1234
>>> while n<=4567:
...     if n%444==0:
...         hap+=n
...     n+=1
... 
...     
>>> print(hap)
23088
>>> #연습문제6번(심화)
>>> mydata=[[n*m for n in range(1,3)] for m in range(2,4)]
>>> #저장된 값은 [2,4] ; [3,6] 이다.
>>> 
>>> #연습문제 7번(마지막 문제)
>>> nn=[100,200,300,400,500]
>>> nn[4]
500
>>> nn[-1]
500
>>> nn[-2]
400
>>> nn[1:4]
[200, 300, 400]
>>> nn[0:1]
[100]
>>> nn[2:-1]
[300, 400]
>>> nn[0::2]
[100, 300, 500]
>>> nn[::-1]
[500, 400, 300, 200, 100]
>>> nn[::-2]
[500, 300, 100]
