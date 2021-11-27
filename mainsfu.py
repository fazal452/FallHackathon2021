#!/usr/bin/env python
from selenium import webdriver
import time















class booking:

    def __init__(self, year, month, day, hour, minute, room):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.room = room




#book1 = booking(0,7,60)

#
# #Authenticate User Firstly
# browser = webdriver.Chrome()
# browser.get('https://cas.sfu.ca/cas/login?method=browser%20=%20webdriver.Chrome()%20browser.get(%27http://roombrowser%20=%20webdriver.Chrome()%20browser.get(%27httpbrowser%20=%20webdriver.Chrome()%20browser.get(%27http://roombookings.lib.sfu.ca/studyrooms/day.php?area=1%27)://roombookings.lib.sfu.ca/studyrooms/day.php?area=1%27)bookings.lib.sfu.ca/studyrooms/day.php?area=1%27)POST&service=https://sims.erp.sfu.ca/psp/csprd/EMPLOYEE/SA/s/WEBLIB_SFU.ISCRIPT1.FieldFormula.IScript_Home')
#
# start = False
#
# start = input("enter 1 to start the program: ")
#
# if start:
#     #Open up SFU Website
#     browser.get('http://roombookings.lib.sfu.ca/studyrooms/day.php?area=1')


testBook = booking(2021,11,27,20,0,28)

listBookings = [booking(2021,11,27,20,0,28),booking(2021,11,28,20,0,28),booking(2021,11,29,20,0,28),booking(2021,11,30,20,0,28)]

driver = webdriver.Chrome()

for i in listBookings:

    bookID = "http://roombookings.lib.sfu.ca/studyrooms/add/"+"edit_entry.php?area=1&room=" + str(testBook.room) +"&hour=" + str(testBook.hour)+"&minute="+str(testBook.minute)+"&year="+ str(testBook.year) +"&month="+str(testBook.month)+"&day=" + str(testBook.day)

    #go to booking step
    driver.get(bookID)

    sessionName = driver.find_element_by_name("name")

    sessionName.send_keys("some text")

    timeDuration = driver.find_element_by_name("duration")

    saveButton = driver.find_element_by_name("save_button")

    saveButton.click()


