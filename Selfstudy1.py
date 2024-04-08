Python 3.13.0a4 (tags/v3.13.0a4:9d34f60, Feb 15 2024, 17:00:30) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from tkinter import*
import random
btnList=[None]*9
photoList=[None]*9
>>> fnameList=["1.gif","2.gif","3.gif","4.gif","5.gif","6.gif","7.gif","8.gif","9.gif"]
>>> i,k=0,0
>>> xPos,yPos=0,0
>>> num=0
>>> ## 메인 코드 부분##, 사진이 있다는 가정##
>>> window=Tk()
>>> window.geometry("210x210")
''
>>> random.shuffle(fnameList)
>>> for i in range(0,9):
...     photoList[i]=PhotoImage(file="gif/"+fnameList[i])
...     btnList[i]=Button(window, image=photoList[i])
... 
...     
Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    photoList[i]=PhotoImage(file="gif/"+fnameList[i])
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\tkinter\__init__.py", line 4248, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\tkinter\__init__.py", line 4195, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "gif/3.gif": no such file or directory
>>> for i in range(0,3):
...     for k in range(0,3):
...         btnList[num].place(x=xPos,y=yPos)
...         num+=1
...         xPos+=70
...     xPos=0
...     yPos+=70
... 
...     
Traceback (most recent call last):
  File "<pyshell#15>", line 3, in <module>
    btnList[num].place(x=xPos,y=yPos)
AttributeError: 'NoneType' object has no attribute 'place'
>>> window.mainloop()
