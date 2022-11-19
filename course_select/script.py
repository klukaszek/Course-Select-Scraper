#! python

import os
import sys
from time import sleep

def notify(text):

    try:
        #split text into a list with / as the delimiter
        token_list = text.split(" / ")
        #convert token_list content to integers
        try:
            available = int(token_list[0])
        except:
            print("int conversion failed this time\n")

        print("Seats Available: {}\nSeats Occupied: {}\nSeats Waitlisted: {}\n".format(token_list[0], token_list[1], token_list[2]))

        #if the course has an available seat, notify the user
        if(available > 0):
            print("THERE IS A SEAT AVAILABLE\n")
    except:
        print("notify() failed")

def main():

    print("Running Seat Scraper...\n")

    #Pass url as first command line argument to script
    f = open("course.txt", 'w+')
    f.write(str(sys.argv[1]))
    f.close()

    #go to correct directory
    os.system("cd course_select")
    filename = "course capacity.txt"

    while True:
        #run the crawler
        os.system("scrapy crawl course 2>NUL")
        
        #wait 15 seconds
        sleep(15)

        #open and read file contents to get course seat information
        f = open(filename, 'r')
        text = f.read()
        f.close()

        #print course seat information
        if text:
            notify(text)

main()