#!/usr/bin/env python
from selenium import webdriver















class booking:

    def __init__(self, day, timeStart, duration):
        #day goes from 0 - 6
        self.day = day

        #time goes form 8.5 to 23.5 increment of .5
        self.timeStart = timeStart

        #duration is in increament of .5 all the way to 2
        self.duration = duration


#book1 = booking(0,7,60)





#Open up SFU Website
browser = webdriver.Chrome()
browser.get('http://roombookings.lib.sfu.ca/studyrooms/day.php?area=1')