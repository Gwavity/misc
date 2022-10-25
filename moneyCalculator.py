import tkinter
import time

gui = tkinter.Tk(className=" ")

gui.geometry("200x100")

def openwindow():
    root_x = gui.winfo_rootx()
    root_y = gui.winfo_rooty()
    popup = tkinter.Toplevel(gui)
    popup.tkraise(gui)
    popup.geometry(f'+{root_x}+{root_y}')
    tkinter.Label(popup,text=f"You will wake up with ${getLabel()} tomorrow morning!!").pack(side="top",fill="x",pady=10)

def buttonPress():
    amountLabel.config(text="Calculating...")
    amountLabel.place(rely=0.5)
    gui.geometry("200x25")
    calculate.destroy()
    ending = ""
    for i in range(3):
        if len(ending) < 1:
            ending = str(3-i)
        else:
            ending += " " + str(3-i)
        gui.after(500,gui.update())
        amountLabel.config(text= f"Calulating... {ending}")
    gui.update()
    time.sleep(.5)
    openwindow()

amountEntry = tkinter.Entry(gui)
amountEntry.pack(side="top",pady=30)

amountLabel = tkinter.Label(gui,text="How much money do you have?")
amountLabel.place(relx=0.5,rely=0.15,anchor=tkinter.CENTER)

def getLabel():
    return amountEntry.get()

calculate = tkinter.Button(text="Calculate",command=buttonPress)
calculate.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

gui.mainloop()
