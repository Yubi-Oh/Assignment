Python 3.13.0a4 (tags/v3.13.0a4:9d34f60, Feb 15 2024, 17:00:30) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 연습문제 1, 답 4번
>>> print("100");print(100);print(50+50);print("50+50")
100
100
100
50+50
>>> #연습문제 2, 답 3번
>>> print('%d / %d = %d' % (5, 10, 5/10))
5 / 10 = 0
>>> #연습문제 3
>>> print("%04d" % 876);print("%5s" % "CookBook");print("%1.1f" % 123.45)
0876
CookBook
123.5
>>> #연습문제 4, 답 3번
>>> print("{2:d}{0:d}{1:d}". format(111, 222, 333))
333111222
>>> #연습문제 11
>>> print(int('1011', 2)) # (1)
11
>>> print(int('1A', 16)) # (2)
26
>>> #연습문제 13
>>> # 1번, 2번, 3번 오류. 각 진수 별 표현할 수 있는 숫자 및 문자 초과
>>> 
>>> #연습문제 15
>>> a=12345678
>>> print(int(a));print(hex(a));print(oct(a));print(bin(a))
12345678
0xbc614e
0o57060516
0b101111000110000101001110
