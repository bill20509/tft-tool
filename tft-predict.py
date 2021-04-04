from tkinter import *
from functools import partial

window = Tk()
window.title('TFT Predict')
window.geometry('800x600')
window.configure(background='white')
list1 = []
list2 = []
def submit():
    list1.clear()
    list2.clear()
    
    list1.append(p1_text.get())
    list1.append(p2_text.get())
    list1.append(p3_text.get())
    list1.append(p4_text.get())
    list1.append(p5_text.get())
    list1.append(p6_text.get())
    list1.append(p7_text.get())
   
    refresh()
    refresh2()
    
def refresh():

    face1.grid_remove()
    face2.grid_remove()
    face3.grid_remove()
    face4.grid_remove()
    face5.grid_remove()
    face6.grid_remove()
    face7.grid_remove()


    face1_text.set(list1[0])
    face1.grid()
    if (len(list1) == 1): return
    face2_text.set(list1[1])
    face2.grid()
    if (len(list1) == 2): return
    face3_text.set(list1[2])
    face3.grid()
    if (len(list1) == 3): return
    face4_text.set(list1[3])
    face4.grid()
    if (len(list1) == 4): return
    face5_text.set(list1[4])
    face5.grid()
    if (len(list1) == 5): return
    face6_text.set(list1[5])
    face6.grid()
    if (len(list1) == 6): return
    face7_text.set(list1[6])
    face7.grid()
    if (len(list1) == 7): return

    

def refresh1(name):
    
    list1.remove(name.get())
    list2.insert(0,name.get())
    if (len(list1) < 3) :
        list1.append(list2[-1])
        del list2[-1]

    
    refresh()
    refresh2()
def refresh2():
    nface1.grid_remove()
    nface2.grid_remove()
    nface3.grid_remove()
    nface4.grid_remove()
    nface5.grid_remove()
    nface6.grid_remove()
    nface7.grid_remove()

    if (len(list2) == 0): return
    nface1_text.set(list2[0])
    nface1.grid()
    if (len(list2) == 1): return
    nface2_text.set(list2[1])
    nface2.grid()
    if (len(list2) == 2): return
    nface3_text.set(list2[2])
    nface3.grid()
    if (len(list2) == 3): return
    nface4_text.set(list2[3])
    nface4.grid()
    if (len(list2) == 4): return
    nface5_text.set(list2[4])
    nface5.grid()
    if (len(list2) == 5): return
    nface6_text.set(list2[5])
    nface6.grid()
    if (len(list2) == 6): return
    nface7_text.set(list2[6])
    nface7.grid()
    if (len(list2) == 7): return
def reset():
    list1.clear()
    list2.clear()
    nface1.grid_remove()
    nface2.grid_remove()
    nface3.grid_remove()
    nface4.grid_remove()
    nface5.grid_remove()
    nface6.grid_remove()
    nface7.grid_remove()

    face1.grid_remove()
    face2.grid_remove()
    face3.grid_remove()
    face4.grid_remove()
    face5.grid_remove()
    face6.grid_remove()
    face7.grid_remove()

    p1_entry.delete(0, END)
    p2_entry.delete(0, END)
    p3_entry.delete(0, END)
    p4_entry.delete(0, END)
    p5_entry.delete(0, END)
    p6_entry.delete(0, END)
    p7_entry.delete(0, END)

#P1~P4
p1_text = StringVar()
p1_label = Label(window, text='P1', font=('bold', 14), pady=5)
p1_label.grid(row=0, column=0, sticky=E)
p1_entry = Entry(window, textvariable=p1_text)
p1_entry.grid(row=0, column=1)

p2_text = StringVar()
p2_label = Label(window, text='P2', font=('bold', 14), pady=5)
p2_label.grid(row=0, column=2, sticky=W)
p2_entry = Entry(window, textvariable=p2_text)
p2_entry.grid(row=0, column=3)

p3_text = StringVar()
p3_label = Label(window, text='P3', font=('bold', 14), pady=5)
p3_label.grid(row=0, column=4, sticky=W)
p3_entry = Entry(window, textvariable=p3_text)
p3_entry.grid(row=0, column=5)

p4_text = StringVar()
p4_label = Label(window, text='P4', font=('bold', 14), pady=5)
p4_label.grid(row=0, column=6, sticky=E)
p4_entry = Entry(window, textvariable=p4_text)
p4_entry.grid(row=0, column=7)

p5_text = StringVar()
p5_label = Label(window, text='P5', font=('bold', 14), pady=5)
p5_label.grid(row=1, column=0, sticky=E)
p5_entry = Entry(window, textvariable=p5_text)
p5_entry.grid(row=1, column=1)

p6_text = StringVar()
p6_label = Label(window, text='P6', font=('bold', 14), pady=5)
p6_label.grid(row=1, column=2, sticky=W)
p6_entry = Entry(window, textvariable=p6_text)
p6_entry.grid(row=1, column=3)

p7_text = StringVar()
p7_label = Label(window, text='P7', font=('bold', 14), pady=5)
p7_label.grid(row=1, column=4, sticky=W)
p7_entry = Entry(window, textvariable=p7_text)
p7_entry.grid(row=1, column=5)

submit_btn = Button(window, text='Submit', width=12, command=submit)
submit_btn.grid(row=1, column=7, sticky=W)

face =  Label(window, text='Will Face', font=('bold', 14), pady=5)
face.grid(row=2, column=0)

face1_text = StringVar()
face1 = Button(window, textvariable=face1_text,  command=partial(refresh1,face1_text))
face1.grid(row=3, column=0)
face1.grid_remove()

face2_text = StringVar()
face2 = Button(window, textvariable=face2_text, command=partial(refresh1,face2_text))
face2.grid(row=3, column=1)
face2.grid_remove()

face3_text = StringVar()
face3 = Button(window, textvariable=face3_text, command=partial(refresh1,face3_text))
face3.grid(row=3, column=2)
face3.grid_remove()

face4_text = StringVar()
face4 = Button(window, textvariable=face4_text, command=partial(refresh1,face4_text))
face4.grid(row=3, column=3)
face4.grid_remove()

face5_text = StringVar()
face5 = Button(window, textvariable=face5_text, command=partial(refresh1,face5_text))
face5.grid(row=3, column=4)
face5.grid_remove()

face6_text = StringVar()
face6 = Button(window, textvariable=face6_text, command=partial(refresh1,face6_text))
face6.grid(row=3, column=5)
face6.grid_remove()

face7_text = StringVar()
face7 = Button(window, textvariable=face7_text, command=partial(refresh1,face7_text))
face7.grid(row=3, column=6)
face7.grid_remove()

not_face =  Label(window, text='Will Not Face', font=('bold', 14), pady=5)
not_face.grid(row=4, column=0)
    
nface1_text = StringVar()
nface1 = Label(window, textvariable=nface1_text)
nface1.grid(row=5, column=0)
nface1.grid_remove()

nface2_text = StringVar()
nface2 = Label(window, textvariable=nface2_text)
nface2.grid(row=5, column=1)
nface2.grid_remove()

nface3_text = StringVar()
nface3 = Label(window, textvariable=nface3_text)
nface3.grid(row=5, column=2)
nface3.grid_remove()

nface4_text = StringVar()
nface4 = Label(window, textvariable=nface4_text)
nface4.grid(row=5, column=3)
nface4.grid_remove()

nface5_text = StringVar()
nface5 = Label(window, textvariable=nface5_text)
nface5.grid(row=5, column=4)
nface5.grid_remove()

nface6_text = StringVar()
nface6 = Label(window, textvariable=nface6_text)
nface6.grid(row=5, column=5)
nface6.grid_remove()

nface7_text = StringVar()
nface7 = Label(window, textvariable=nface7_text)
nface7.grid(row=5, column=6)
nface7.grid_remove()

reset_btn = Button(window, text='reset', width=12, command=reset)
reset_btn.grid(row=10, column=0, sticky=S)


window.mainloop()
