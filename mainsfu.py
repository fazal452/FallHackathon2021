#!/usr/bin/env python
from selenium import webdriver
import datetime
import time
from selenium.webdriver.support.ui import Select

import tkinter as tk
from PIL import ImageTk

sun = []
mon = []
tues = []
wed = []
thurs = []
fri = []
sat = []
week = [sun, mon, tues, wed, thurs, fri, sat]


window = tk.Tk()
w = 640;
h = 360
canvas = tk.Canvas(window, width=w, height=h)
canvas.pack()

##ENTER LOCATION OF YOUR JPG
img = ImageTk.PhotoImage(file="/home/fazal/Desktop/git/FallHackathon2021/bg.jpg")
canvas.create_image(w / 2, h / 2, image=img)

loc = tk.IntVar()
s_time_menu = []
e_time_menu = []
s_time = []
e_time = []
OPTIONS = ["Time", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
           "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30",
           "20:00", "20:30", "21:00", "21:30",
           "22:00", "22:30"]
ROOMS = ["Select","2004", "2006", "2007", "2102", "2103", "2106", "2107", "2108", "2109", "2110", "2111", "2112", "2113", "2114"]





for i in range(7):
    s_time.append(tk.StringVar())
    s_time[i].set(OPTIONS[0])  # default value
    e_time.append(tk.StringVar())
    e_time[i].set(OPTIONS[0])  # default value

    s_time_menu.append(tk.OptionMenu(window, s_time[i], *OPTIONS))
    s_time_menu[i].config(width=5, font=('Calibri', 7))

    e_time_menu.append(tk.OptionMenu(window, e_time[i], *OPTIONS))
    e_time_menu[i].config(width=5, font=('Calibri', 7))

    canvas.create_window((102 + ((i + 1) * 72)), 185, anchor='ne', window=s_time_menu[i])
    canvas.create_window((102 + ((i + 1) * 72)), 224, anchor='ne', window=e_time_menu[i])


submit_button = tk.Button(window, text="Submit", command=window.quit, anchor='w', width=10, activebackground="#33B5E5")
submit_button_window = canvas.create_window(w-30, 300, anchor='ne', window=submit_button)


room = tk.StringVar()
room.set(ROOMS[0])  # default value
room_menu = tk.OptionMenu(window, room, *ROOMS)
room_menu.config(width=10, font=('Calibri', 10))
canvas.create_window((200), 109, anchor='ne', window=room_menu)

window.mainloop()

def write(*message, end="\n", sep=" "):
    text = ""
    for item in message:
        text += "{}".format(item)
        text += sep
    text += end
    console.insert(tk.INSERT, text)


for i in range(7):
    week[i].append(s_time[i].get())
    week[i].append(e_time[i].get())

week.append(room.get())

######################################################################

results = []

class booking:

    def __init__(self, year, month, day, hour, minute, room,duration):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.room = room
        self.duration = duration


arr = week

temp = arr[0]

arr[0] = arr[-1]

arr[-1] = temp

for i in range(len(arr)):
    if "i" in arr[i][0] or "i" in arr[i][1]:
        arr[i] = ["10:10","10:10"]

# for i in arr:
#     if "i" in i[0] or "i" in i[1]:
#         i = ["10:10","10:10"]

print(arr)


#should be [room, mon, tues.....sun]


# year, month, day, hour, minutes, room
listBookings = []


now = datetime.datetime.now()


date = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute,now.second)

for day in range(13):
    # ["1200","1300"]

    weekdate = arr[date.weekday() + 1]

    start = weekdate[0]

    startHours = weekdate[0][0:2]
    startMins = weekdate[0][3:5]

    end = weekdate[1]
    endHours = weekdate[1][0:2]
    endMins = weekdate[1][3:5]


    dura = float((float(endHours) - float(startHours)) + (float(endMins)-float(startMins))/60)

    if int(arr[0]) == 2004:
        nameroom = 28
    if int(arr[0]) == 2006:
        nameroom = 14
    if int(arr[0]) == 2007:
        nameroom = 15
    if int(arr[0]) == 2102:
        nameroom = 3
    if int(arr[0]) == 2103:
        nameroom = 4
    if int(arr[0]) == 2106:
        nameroom = 5
    if int(arr[0]) == 2107:
        nameroom = 6
    if int(arr[0]) == 2108:
        nameroom = 7
    if int(arr[0]) == 2109:
        nameroom = 8
    if int(arr[0]) == 2110:
        nameroom = 9
    if int(arr[0]) == 2111:
        nameroom = 10
    if int(arr[0]) == 2112:
        nameroom = 11
    if int(arr[0]) == 2113:
        nameroom = 12
    if int(arr[0]) == 2114:
        nameroom = 13

    listBookings.append(booking(date.year,date.month,date.day,startHours,startMins,nameroom,dura))

    date += datetime.timedelta(days=1)




#Authenticate User Firstly
driver = webdriver.Chrome()
driver.get('https://cas.sfu.ca/cas/login?method=POST&service=https://sims.erp.sfu.ca/psp/csprd/EMPLOYEE/SA/s/WEBLIB_SFU.ISCRIPT1.FieldFormula.IScript_Home')

start = False

##Log User in
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
submit = driver.find_element_by_name("submit")

username.send_keys("fra22")
password.send_keys("Password")
submit.click()



start = input("enter 1 to start the program: ")

if start:
    #Open up SFU Website
    driver.get('http://roombookings.lib.sfu.ca/studyrooms/day.php?area=1')




def book(testbook):

    bookID = "http://roombookings.lib.sfu.ca/studyrooms/add/" + "edit_entry.php?area=1&room=" + str(
        testBook.room) + "&hour=" + str(testBook.hour) + "&minute=" + str(testBook.minute) + "&year=" + str(
        testBook.year) + "&month=" + str(testBook.month) + "&day=" + str(testBook.day)

    # go to booking step
    driver.get(bookID)

    time.sleep(2)

    try:
        sessionName = driver.find_element_by_name("name")

        sessionName.send_keys("CREATOR BOT")

        timeDuration = Select(driver.find_element_by_id('duration'))

        timeDuration.select_by_value(str(testbook.duration))

        saveButton = driver.find_element_by_name("save_button")

        saveButton.click()
        time.sleep(2)


    except:
        results.append(1)
        return("Failed to book, Already booked for the day")

    try:
        rep = (driver.find_element_by_xpath('/html/body/h2').text)

    except:
        rep = "null"

    if "conflict" in rep.lower():
        results.append(2)
        return("Failed to book, Scheduling Conflict")

    else:
        results.append(0)
        return("Succesfully Booked")




for testBook in listBookings:

    if testBook.duration < 0:
        results.append(2)

    if testBook.duration > 2:
        results.append(2)


    if testBook.duration > 0 and testBook.duration < 2:
        print(book(testBook))

driver.close()

###########################################################

temp = tk.Tk()

console = tk.Text(window, width=80, height=3, font=('Calibri', 10))
console.pack(side = tk.TOP)


for i in results:
  if i == 0:
    write("Success")
  elif i == 1:
    write("Fail - Room already booked")
  elif i == 2:
    write("Fail - Scheduling Conflict")


temp.mainloop()