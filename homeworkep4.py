### Homework EP4 #####

from tkinter import *
from tkinter import ttk,messagebox
from datetime import datetime
import csv
import tkinter as tk

##############CSV###############

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']


def readcsv():
     
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
     
 
    return data

#########Main GUI#########

GUI=Tk()
GUI.geometry('550x750+600+100') #กำหนดขนาดและตำแหน่งที่จะให้แสดงที่x600 y200 ทุุกคร้ัง
GUI.title('โปรแกรมบันทึกข้อมูล')

FONT1=('Angsana New',12)
FONT2=('Angsana New',16)
FONT3=('Angsana New',20)

Ti1 = Label(GUI,text='โปรแกรมบันทึกข้อมูล',font=FONT3,fg='green')
Ti1.place(x=10,y=10)

####### Add Data#####

UpF1= Frame(GUI)
UpF1 = LabelFrame(GUI,text='กรอกข้อมูลที่ต้องการบันทึก',font=FONT2)
UpF1.place(x=20,y=100)


v_data = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(UpF1,textvariable=v_data,font=FONT1,width=70)
E1.pack(pady=10,padx=10)


def SaveData(event=None):
#    log_data.delete('1.0', tk.END)
    t = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    if len(data)>0: # เช็คข้อมูลในช่องกรอก มี=บันทึก  ไม่มี=แจ้งตือน
        writecsv(text) #บันทึกลง csv
        v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

        log_data.delete('1.0',END) #เคลียร์ข้อมูล ไม่ให้แสดงซ้ำ

#--------- ให้แสดงข้อมูลใหม่ หลังกดปุ่มบันทีก ทันที----#
        data = readcsv()
       
        for v in data:
            log_data.insert(END,v)
            log_data.insert(END,'\n')
            
    else:
        messagebox.showinfo('ไม่มีข้อมูล','ต้องมีข้อมูล หากไม่มีข้อมูลไม่สามารถบันทึกได้') 

B1 = ttk.Button(UpF1,text='บันทึก',command=SaveData)
B1.pack(ipadx=10,ipady=10)

E1.bind('<Return>',SaveData)  # กด enter= กดปุ่มบันทึก      



####### Show Data#####

LwF1=Frame()
LwF1 = LabelFrame(GUI,text='แสดงข้อมูลที่บันทึก',font=FONT2)
LwF1.place(x=20,y=300)

log_data = Text(LwF1,font=FONT1, height=15, width=80)
log_data.pack(pady=10, padx=20)


##---แสดงข้อมูลเดิม ที่บันทึกก่อนหน้า----##

data = readcsv()
    
for v in data:
    log_data.insert(END,v)
    log_data.insert(END, "\n")    




GUI.mainloop()
