#! python

import os
import sys
from time import sleep

def notify(text):

    token_list = text.split(" / ")
    seats = [int(token_list[0]), int(token_list[1]), int(token_list[2])]

    print("Seats Available: {}\nSeats Occupied: {}\nSeats Waitlisted: {}\n".format(seats[0], seats[1], seats[2]))


def main():

    #Pass url as first command line argument to script
    f = open("url.txt", 'w+')
    f.write(str(sys.argv[1]))
    f.close()

    #go to correct directory
    os.system("cd course_select")
    filename = "course capacity.txt"

    while True:
        #run the crawler
        os.system("scrapy crawl course 2>NUL")
        
        #wait 15 seconds
        sleep(10)

        #open and read file contents to get course seat information
        f = open(filename, 'r')
        text = f.read()
        f.close()

        #print course seat information
        notify(text)

main()