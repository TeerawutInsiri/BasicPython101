#vacab.py

from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
import random

#########DataBase#########

conn = sqlite3.connect('vocab.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS vocab (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
		vocab text,
		meaning text,
		score int)""")

def insert_vocab(vocab,meaning):
    ID = None
    score=0
    with conn:
        c.execute("""INSERT INTO vocab VALUES (?,?,?,?)""",
                  (ID,vocab,meaning,score))
    conn.commit()
    print('Data was inserted')

def view_vocab():
    with conn:
        c.execute("SELECT * FROM vocab")
        allvocab = c.fetchall()
        print(allvocab)

    return allvocab

#########Main GUI#########

GUI=Tk()
GUI.geometry('550x550+600+200') #กำหนดตำแหน่งที่จะให้แสดง ที่x600 y200 ทุุกคร้ัง
GUI.title('โปรแกรมท่องจำคำศัพท์อัจฉริยะ')

FONT1=('Angsana New',20)
FONT2=('Angsana New',25)

###########Notebook###########

Tab=ttk.Notebook(GUI)

T1=Frame(Tab)
T2=Frame(Tab)
T3=Frame(Tab)

Tab.pack(fill=BOTH,expand=1)
Tab.add(T1,text='Add Vocab')
Tab.add(T2,text='All Vocab')
Tab.add(T3,text='Flashcard')

#*********Tab 1 *************#

########### Vocab#############
L1=ttk.Label(T1,text='คำศัพท์',font=FONT1)
L1.pack()

v_vocab=StringVar()
E1=ttk.Entry(T1,textvariable=v_vocab,font=FONT1,width=30)
E1.pack()

##########Meaning##########
L2=ttk.Label(T1,text='คำแปล',font=FONT1)
L2.pack()

v_meaning=StringVar()
E2=ttk.Entry(T1,textvariable=v_meaning,font=FONT1,width=30)
E2.pack()

###########Button##########
def SaveVocab(event=None):
    global addvocab
    vocab=v_vocab.get()
    meaning=v_meaning.get()
    if len(vocab)>0 and len(meaning)>0:
        insert_vocab(vocab,meaning)
        print('V:{} M:{}'.format(vocab,meaning))
        v_vocab.set('')
        v_meaning.set('')
        E1.focus()
        ##Clear old Data##
        vocabtable.delete(*vocabtable.get_children())
        ##Update table##
        
        addvocab=view_vocab()
        for v in addvocab:
            vocabtable.insert('','end',value=v)
        print('------------')
    else:
        messagebox.showinfo('ไม่มีข้อมูล','ต้องมีช่องคำศัพท์และคำแปล หากไม่มีไม่สามารถบันทึกได้')
    
B1=ttk.Button(T1,text='Save Vocab',command=SaveVocab)
B1.pack(ipadx=20,ipady=10,pady=15)

E2.bind('<Return>',SaveVocab)


#*********Tab 2 *************#

header=['ID','Vocab','Meaning','Score']
hdsize=[50,200,200,50]
        
vocabtable=ttk.Treeview(T2,columns=header,show='headings',height=20)
vocabtable.place(x=20,y=50)

for h,s in zip(header,hdsize):
    vocabtable.heading(h,text=h)
    vocabtable.column(h,width=s)

        
#*********Tab 3 *************#

rv_vocab=StringVar()
rv_vocab.set('---คำศัพท์---')
rv_meaning=StringVar()
rv_meaning.set('---คำแปล---')

R1=ttk.Label(T3,textvariable=rv_vocab,font=FONT2,foreground='red')
R1.pack(pady=25)

R2=ttk.Label(T3,textvariable=rv_meaning,font=FONT2,foreground='red')
R2.pack(pady=25)

BRF=Frame(T3)
BRF.pack()

vcurrent=[]

def NextButton():
    global vcurrent
    current=random.choice(addvocab)
    vcurrent=current
    rv_vocab.set(current[1])
    rv_meaning.set('---คำแปล---')

def ShowButton():
    rv_meaning.set(vcurrent[2])
    

BR1=ttk.Button(BRF,text='Next',command=NextButton)
BR1.grid(row=0,column=0,ipadx=20,ipady=10,padx=5)
BR2=ttk.Button(BRF,text='Show',command=ShowButton)
BR2.grid(row=0,column=1,ipadx=20,ipady=10,padx=5)
BR3=ttk.Button(BRF,text='Score')
BR3.grid(row=0,column=2,ipadx=20,ipady=10,padx=5)               

#*****Initial Program*******#

global addvocab
addvocab=view_vocab()
if len(addvocab)>0:
    for v in addvocab:
        vocabtable.insert('','end',value=v)
    

GUI.mainloop()
