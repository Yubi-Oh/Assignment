Python 3.13.0a4 (tags/v3.13.0a4:9d34f60, Feb 15 2024, 17:00:30) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import*
>>> from tkinter.filedialog import*
>>> ## 함수 선언 부분##
>>> def func_open():
...     filename=askopenfilename(parent=window,filetypes=(("GIF파일","*.gif"),("모든 파일","*.*")))
...     photo=PhotoImage(file=filename)
...     pLabel.configure(image=photo)
...     pLabel.image=photo
... 
...     
>>> def func_exit():
...     window.quit()
...     window.destroy()
... 
...     
>>> def convert_to_grayscale(image):
...     width=image.width()
...     height=image.height()
...     for x in range(width):
...         for y in range(height):
...             red, green, blue=image.get(x,y)
...             gray=(red+green+blue)//3
...             image.put("#%02x%02x%02x"%(gray, gray, gray), (x,y))
... 
...             
>>> window=Tk()
>>> window.geometry("400x400")
''
>>> window.title("명화 감상하기")
''
>>> photo=PhotoImage()
>>> pLabel=Label(window, image=photo)
>>> pLabel.pack(expand=1, anchor=CENTER)
>>> mainMenu=Menu(window)
>>> window.config(menu=mainMenu)
>>> fileMenu=Menu(mainMenu)
mainMenu.add_cascade(labe="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)
window.mainloop()
