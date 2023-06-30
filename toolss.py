from tkinter import *
import os
root=Tk()
root.title("shutdown")
root.geometry("580x780")


def restarttime():
    os.system("shutdown /r /t 30")
def shutdownn():
    os.system("shutdown /s /t 5")

def restart():
    os.system("shutdown /r /t 1")
def logout():
    os.system("shutdown -l")

# first button
restart_time_button = PhotoImage(file="restartnew.png")
# button(root,image)

firstbutton= Button(root,image=restart_time_button,borderwidth=0,cursor='hand2', command=restarttime)
firstbutton.place(x=10,y=10)
#2ndbutton
closeButtonimage =PhotoImage(file="closenew.png")
secondbutton= Button(root,image=closeButtonimage, borderwidth=0, cursor="hand2", command=root.destroy)
secondbutton.place(x=280,y=10)
#third button
shutdown=PhotoImage(file="shutt.png")
thirdButton = Button(root,image=shutdown ,borderwidth=0, cursor="hand2",command=shutdownn)
thirdButton.place(x=10,y=290)
#fourth button
restart= PhotoImage(file="restart.png")
fifthButton =Button(root,image=restart,borderwidth=0,cursor="hand2", command=restart)
fifthButton.place(x=280, y=290)
#fifth button
logout=PhotoImage(file="logoutnew.png")
fourthButton=Button(root,image=logout, borderwidth=0,cursor="hand2", command=logout)
fourthButton.place(x=10, y=540)
root.mainloop()