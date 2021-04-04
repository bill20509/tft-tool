from tkinter import *
import math
window = Tk()
window.title('TFT cal')
window.geometry('400x200')
window.configure(background='white')
list1 = [[100,0,0,0],
         [100],
         [70.30,0,0,0],
         [50,35,15,0,0],
         [35,40,20,5,0],
         [20,35,35,10,0],
         [14,30,40,15,1],
         [14,20,35,25,6],
         [10,15,25,35,15]
         ]
list2 = [29, 22, 16 ,12,10]
list3 = [12, 12, 12, 9, 7]
def callback(event):
    cal()
    
def cal():
    level = int(level_entry.get())
    cost = int(cost_entry.get())
    uni = list2[cost-1] #用不到 monkaS
    kind = list3[cost-1]
    x = round(list1[level-1][cost-1] * 0.01 ,2 )
    print(x, uni, kind)
    res = (x * (1/kind)) * 5 
    print (res)
    ev = 1 / res * 2
    text.set( str(round(res*100,3)) + "% " + str(round(ev, 2)) + "元")

level_frame = Frame(window)
level_frame.pack(side=TOP)
level_label = Label(level_frame, text='Level')
level_label.pack(side=LEFT)
level_entry = Entry(level_frame)
level_entry.pack(side=LEFT)

cost_frame = Frame(window)
cost_frame.pack(side=TOP)
cost_label = Label(cost_frame, text='Cost')
cost_label.pack(side=LEFT)
cost_entry = Entry(cost_frame)
cost_entry.pack(side=LEFT)

res_frame = Frame(window)
res_frame.pack(side=TOP)
text= StringVar()
res_label = Label(res_frame, textvariable=text)
res_label.pack(side=LEFT)

calculate_btn = Button(window, text='Cal',command=cal)
calculate_btn.pack()

window.bind('<Return>', callback)
window.mainloop()
