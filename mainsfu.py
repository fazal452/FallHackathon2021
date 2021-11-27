#!/usr/bin/env python
from selenium import webdriver
import time















class booking:

    def __init__(self, day, timeStart, duration):
        #day goes from 0 - 6
        self.day = day

        #time goes form 8.5 to 22.5 increment of .5
        self.timeStart = timeStart

        #duration is in increament of .5 all the way to 2
        self.duration = duration


#book1 = booking(0,7,60)



#Authenticate User Firstly

browser = webdriver.Chrome()
browser.get('https://cas.sfu.ca/cas/login?method=browser%20=%20webdriver.Chrome()%20browser.get(%27http://roombrowser%20=%20webdriver.Chrome()%20browser.get(%27httpbrowser%20=%20webdriver.Chrome()%20browser.get(%27http://roombookings.lib.sfu.ca/studyrooms/day.php?area=1%27)://roombookings.lib.sfu.ca/studyrooms/day.php?area=1%27)bookings.lib.sfu.ca/studyrooms/day.php?area=1%27)POST&service=https://sims.erp.sfu.ca/psp/csprd/EMPLOYEE/SA/s/WEBLIB_SFU.ISCRIPT1.FieldFormula.IScript_Home')

start = False

start = input("enter 1 to start the program: ")

if start:
    #Open up SFU Website
    browser.get('http://roombookings.lib.sfu.ca/studyrooms/day.php?area=1')