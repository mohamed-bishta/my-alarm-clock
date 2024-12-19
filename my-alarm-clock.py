from tkinter import *
import datetime
import time
import winsound

def alarem(set_alarem):
    while True:
        time.sleep(1)

        courent_time = datetime.datetime.now()
        new = courent_time.strftime("%H:%M:%S")
        date = courent_time.strftime("%d:%m:%Y")
        
        print("the set date", date)
        print(new)
        
        if new == set_alarem:  
            print("time to wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

def set_alarm_time():
    set_alarem = f"{hour.get()}:{main.get()}:{sec.get()}"
    alarem(set_alarem)

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")

time_format = Label(clock, text="Enter time to set alarm", fg="red", bg="black", font="Arial")
time_format.place(x=60, y=120)
date_time = Label(clock, text="Hour   Minute   Second", font=60)
date_time.place(x=110)
time_format = Label(clock, text="Enter time to set alarm", fg="blue", bg="white", font=("Arial", 7, "bold"))
time_format.place(x=0, y=29)

hour = StringVar()
main = StringVar()
sec = StringVar()

hour_time = Entry(clock, textvariable=hour, bg="pink", width=15)
hour_time.place(x=110, y=30)
main_time = Entry(clock, textvariable=main, bg="pink", width=15)
main_time.place(x=150, y=30)
sec_time = Entry(clock, textvariable=sec, bg="pink", width=15)
sec_time.place(x=190, y=30)

submit = Button(clock, text="Set Alarm", fg="red", width=10, command=set_alarm_time)
submit.place(x=110, y=170)

clock.mainloop()
