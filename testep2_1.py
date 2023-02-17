from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI=Tk() #หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกเรียนพื้นฐาน Python 101')#ชื่อของโปรแกรม
GUI.geometry('500x400') #ขนาดของโปรแกรม

L1=Label(GUI,text='Python 101 พื้นฐาน Python 16 ชั่วโมง (ภาคเช้า) by Uncle Engineer',fg='red')
L1.place(x=10,y=20)


#######################
def Button1():
    text='แนะนำวิธีการติดตั้ง Python และพื้นฐานการเขียนโปรแกรมโปรแกรมควบคุม Turtle'
    messagebox.showinfo('เนื้อหา Ep1',text)

FB1=Frame(GUI)#คล้ายกระดาน
FB1.place(x=20,y=50)
B1=ttk.Button(FB1,text='EP 1',command=Button1)
B1.pack(ipadx=5,ipady=5)

#######################

#######################
def Button2():
    text='https://www.youtube.com/watch?v=j1GCwOiACqw'
    messagebox.showinfo('Link บทเรียน Ep1',text)

FB2=Frame(GUI)#คล้ายกระดาน
FB2.place(x=250,y=50)
B2 = ttk.Button(FB2,text='Link Ep1',command=Button2)
B2.pack(ipadx=5,ipady=5)

#######################


#######################
def Button3():
    text='พื้นฐาน Python สำหรับการประยุกต์ใช้ในการเขียนโปรแกรม GUI แบบง่ายๆ '
    messagebox.showinfo('เนื้อหา Ep2',text)

FB3=Frame(GUI)#คล้ายกระดาน
FB3.place(x=20,y=100)
B3=ttk.Button(FB3,text='EP 2',command=Button3)
B3.pack(ipadx=5,ipady=5)

#######################

#######################
def Button4():
    text='https://www.youtube.com/watch?v=4sj5bS2LVGQ'
    messagebox.showinfo('Link บทเรียน Ep2',text)

FB4=Frame(GUI)#คล้ายกระดาน
FB4.place(x=250,y=100)
B2 = ttk.Button(FB4,text='Link Ep2',command=Button4)
B2.pack(ipadx=5,ipady=5)

#######################

GUI.mainloop()
