Python 3.13.0a4 (tags/v3.13.0a4:9d34f60, Feb 15 2024, 17:00:30) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#1
>>> ss= 'Python'
>>> for i in range (0, len(ss)) :
...      print(ss[i] + '$', end = '')
... 
...      
P$y$t$h$o$n$
>>> #2
>>> def filter_korean_and_english(input_str):
...     filtered_str = ''.join(char for char in input_str if char.isalpha() or char.isspace())
...     return filtered_str
... 
>>> 
>>> input_str = input("문자열: ")
문자열: thank you!! ㅋ
>>> filtered_str = filter_korean_and_english(input_str)
>>> print("zzzz", filtered_str)
zzzz thank you ㅋ
>>> #3 빈칸 답 : inStr[strLen-i-1]
>>> 
>>> #4 나선형 코딩
>>> import turtle
>>> import random
>>> import math
>>> swidth, sheight = 500, 500
>>> radius = 200
>>> txtSize = 20
>>> decrease_rate = 10
>>> turtle.title('나선형으로 문자열 쓰기')
>>> turtle.setup(width=swidth + 50, height=sheight + 50)
>>> turtle.screensize(swidth, sheight)
>>> turtle.penup()
>>> inStr = input("문자열을 입력하세요: ")
문자열을 입력하세요: 나 보기가 역겨워 가실 때에는 말없이 고이 보내 드리오리다
>>> count = len(inStr)
>>> angle = (360 * 2) / count
>>> turtle.left(90)
>>> for i in range(count):
...     radian = math.radians(angle * i)
...     current_radius = radius - (txtSize / decrease_rate) * (i + 1)  
...     tX = current_radius * math.cos(radian)
...     tY = current_radius * math.sin(radian)
...     r=random.random();g=random.random();b=random.random()
...    
...     turtle.goto(tX, tY)
... 
...   
...     turtle.pencolor((r, g, b))
...     turtle.write(inStr[i], font=('맑은고딕', txtSize, 'bold'))
... 
...     
>>> turtle.done()
>>> 
>>> #5
>>> #빈칸 1= *args, 빈칸 2= return result
>>> 
>>> #6 출력되는 값 예상
>>> #답 : f1()=100, f2()=10
>>> 
>>> #7 재귀 함수 코드
>>> def addNumber(num) :
...     if num == 1 :
...         return 1
...     return num + addNumber(num -1)
... 
>>> print(addNumber(100))
5050
>>> #8 매개변수 기본값을 2개 설정하는 코드
>>> def myFunc(p1, p2=2, p3=2) :
...     ret = p1+p2+p3
...     return ret
... 
>>> #8 매개변수 기본값을 2개 설정하는 코드(수정 및 답)
>>> def myFunc(p1=2, p2=2, p3=2) :
...     ret = p1+p2+p3
...     return ret

