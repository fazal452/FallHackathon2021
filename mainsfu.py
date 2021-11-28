#!/usr/bin/env python
from selenium import webdriver
import datetime
import time
from selenium.webdriver.support.ui import Select

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


arr = [["12:00","13:30"],["13:30","15:00"],["12:00","15:00"],["12:00","14:30"],["13:30","15:00"],["12:00","12:30"],["12:00","14:30"],2003]

temp = arr[0]

arr[0] = arr[-1]

arr[-1] = temp

for i in arr:
    if 'm' in arr:
        i = ("10:00","10:00")



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


    listBookings.append(booking(date.year,date.month,date.day,startHours,startMins,arr[0],dura))

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
password.send_keys("")
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


