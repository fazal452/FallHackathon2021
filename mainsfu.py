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

        timeDuration = driver.find_element_by_xpath("/html/body/form/fieldset/div[4]/select/option[4]")
        timeDuration.selected = "seleted"

        saveButton = driver.find_element_by_name("save_button")

        saveButton.click()
        time.sleep(2)


    except:
        return("Failed to book, Already booked for the day")

    try:
        rep = (driver.find_element_by_xpath('/html/body/h2').text)

    except:
        rep = "null"

    if "conflict" in rep.lower():
        return("Failed to book, Scheduling Conflict")

    else:
        return("Succesfully Booked")



# year, month, day, hour, minute, room
listBookings = [booking(2021,12,1,20,0,28),booking(2021,12,2,20,0,28),booking(2021,12,3,20,0,28),booking(2021,12,4,20,0,28),booking(2021,12,5,20,0,28)]


for testBook in listBookings:

    print(book(testBook))

driver.close()


