import random
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
a=random.randint(0,20)
bac="0."+str(a) if a>=10 else "0.0"+str(a)
bac=float(bac)

ccc = ["pink4"]
cc=["#FFFFFF"]
def pro(root):
    from tkinter.ttk import Progressbar
    #root = Tk()
    #root.title("Analysing...")
    # Progress bar widget

    progress = Progressbar(root, orient=HORIZONTAL,
                           length=100, mode='indeterminate')
    lbll = Label(root, text="Analysing...", font=('Times New Roman', 15, 'bold'),
                 bg=ccc[0], fg=cc[0])
    lbll.pack()
    # Function responsible for the updation
    # of the progress bar value
    def bar(lbll):
        import time
        progress['value'] = 20
        root.update_idletasks()
        time.sleep(0.5)

        progress['value'] = 40

        root.update_idletasks()
        time.sleep(0.5)

        progress['value'] = 50
        root.update_idletasks()
        time.sleep(0.5)

        progress['value'] = 60
        root.update_idletasks()
        time.sleep(0.3)

        progress['value'] = 80
        root.update_idletasks()
        time.sleep(0.4)

        progress['value'] = 100
        root.update_idletasks()
        time.sleep(0.1)

        progress['value'] = 80
        root.update_idletasks()
        time.sleep(0.5)

        progress['value'] = 70
        root.update_idletasks()
        time.sleep(0.3)

        progress['value'] = 50
        root.update_idletasks()
        time.sleep(0.2)

        progress['value'] = 40
        root.update_idletasks()
        time.sleep(0.1)

        progress['value'] = 20
        root.update_idletasks()
        time.sleep(0.2)
        progress['value'] = 0
        lbll.config(text="Completed...")
        time.sleep(0.3)
    # This button will initialize
    # the progress bar
    #bar()
    progress.pack(pady=10)
    bar(lbll)
    # infinite loop
    #root.destroy()
topp = Tk()
topp.title("BAC Device")
ccc = ["pink4"]
cc=["#FFFFFF"]
topp.configure(background=ccc[0], bd=20, relief=SUNKEN)
topp.geometry("300x280+0+0")
lbl = Label(topp, text="Please blow I have \nto analyse your breath\n\n", font=('Times New Roman', 15, 'bold'), bg=ccc[0], fg=cc[0])
lbl.pack()

def bookc():
    global topp, lbl, butt
    messagebox.showinfo("Booking a cab", "Paired up with your phone!\nPlease check your phone for the cab ride\nBooking to XXXaddress complete")
    topp.destroy()

def callc():
    global topp, lbl, butt
    messagebox.showinfo("Calling Family",
                        "Paired-up with your phone!\nSpeaker mode enable\nBruh you're dead!")
    topp.destroy()
def emer():
    global topp, lbl, butt
    bb=messagebox.askyesno("Emergency",
                        "Is someone there nearby who can drop you?")
    if bb==0:
        nn=messagebox.askyesno("Emergency",
                            "I would highly recommend to call someone or book a cab\nWhat's your opinion?")
        if nn==0:
            messagebox.showinfo("Emergency",
                                "I'll allow you to drive since your \nmind is clear enough to answer my questions\n\nBut I won't allow you to cross 40km/hr\nDrive safely!!")
            topp.destroy()
    else:
        messagebox.showinfo("Emergency",
                            "Thank you!\nPlease show your address to that person\n XXX street...\nXXXArea...XXXcity")

def start():
    global topp,lbl,butt
    a = random.randint(0, 1)
    if a==1:
        lbl.config(text="I'm not a straw. Please blow")
        butt.config(text="Restart")
    else:
        pro(topp)
        if bac == 0:
            print("You're not drunk")
            messagebox.showinfo("Result","You're not drunk")
            topp.destroy()
        elif (bac < 0.05 and bac > 0):
            print("Your Blood alcohol content is", bac)
            print("You can drive since it's within the legal limit")
            print("You'll sober up within %.1f" % (bac / (0.015)), "hours")
            messagebox.showinfo("Result","Your Blood alcohol content is "+str(bac)+"\nYou can drive since it's within the legal limit"
                                                                                   +"\nYou'll sober up within %.1f hours" % (bac / (0.015)))
            topp.destroy()
        elif (bac >= 0.05 and bac <= 0.08):
            print("Your Blood alcohol content is", bac, "slightly high!")
            print("You'll sober up within %.1f" % (bac / (0.015)), "hours")
            print("It's within the legal limit, but are you sure that you can drive?")
            m=messagebox.askyesno("Result", "Your Blood alcohol content is " + str(
                bac) + " slightly high!\nYou'll sober up within %.1f hours\nIt's within the legal limit, but are you sure that you can drive?" % (bac / (0.015)))
            if m==0:
                for i in topp.winfo_children():
                    i.destroy()
                topp.geometry("265x100+0+0")

                but = Button(topp, text="Book a cab", font=('arial', 12, 'bold'), bg=ccc[0], fg=cc[0], command=bookc,
                             bd=9)
                but.grid(row=0, column=0)
                buut = Button(topp, text="Call family", font=('arial', 12, 'bold'), bg=ccc[0], fg=cc[0], command=callc,
                              bd=9)
                buut.grid(row=0, column=1)
            else:
                topp.destroy()
        elif (bac > 0.08):
            print("Your Blood alcohol content is", bac, "super high!")
            print("Sorry, I can't allow you to start the vehicle")
            print("You'll sober up only after %.1f" % (bac / (0.015)), "hours")
            print("Cab or call family or emergency")
            for i in topp.winfo_children():
                i.destroy()
            topp.geometry("650x200+0+0")
            lb = Label(topp, text="Your Blood alcohol content is " + str(
                bac) + " super high!\nSorry, I can't allow you to start the vehicle\nYou'll sober up only after %.1f hours\n\nWhat do you want to do?" % (bac / (0.015)),
                        font=('Times New Roman', 15, 'bold'), bg=ccc[0], fg=cc[0])
            lb.grid(row=0,column=1)
            but = Button(topp, text="Book a cab", font=('arial', 12, 'bold'), bg=ccc[0], fg=cc[0], command=bookc, bd=9)
            but.grid(row=1,column=0)
            buut = Button(topp, text="Call family", font=('arial', 12, 'bold'), bg=ccc[0], fg=cc[0], command=callc, bd=9)
            buut.grid(row=1, column=1)
            bbut = Button(topp, text="Emergency", font=('arial', 12, 'bold'), bg=ccc[0], fg=cc[0], command=emer, bd=9)
            bbut.grid(row=1, column=2)


butt=Button(topp, text="Start", font=('arial', 16, 'bold'), bg=ccc[0], fg=cc[0], command=start, bd=9)
butt.pack()
topp.mainloop()