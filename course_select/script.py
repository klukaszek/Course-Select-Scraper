import os
import sys
from time import sleep
from datetime import datetime

#import Sendgrid API
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

#Get course code
try:
    course = str(sys.argv[1])
except:
    print("Please input a valid UoG course code as the first argument.")
    exit(1)

#Get user email
try:
    user_email = str(sys.argv[2])
except:
    print("Please input your email that is a valid Sendgrid sender as the second argument.\nThis email will send a message to itself when a seat is available.")
    exit(1)


count = 0

#Get api key from envvar
key = os.environ.get('SENDGRID_API_KEY')

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
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Time =", current_time)

            #Initialize mail
            sg = sendgrid.SendGridAPIClient(api_key=key)
            from_email = Email(user_email)
            to_email = To(user_email)
            subject = "Course Select Scraper Notification"
            content = Content("text/plain", "A seat in {} is now available at {}. Act fast before someone takes it.".format(course, current_time))
            mail = Mail(from_email, to_email, subject, content)

            #Get mail as json
            mail_json = mail.get()

            #Post request using JSON to send email
            response = sg.client.mail.send.post(request_body=mail_json)
            print(response.status_code)

            #If email is successful, increase count by 1
            if(int(response.status_code) == 202):
                count+=1
            
            #This just ensures that for whatever reason you can't exceed the 100 free emails per day if you leave the script running for too long
            if(count > 50):
                exit(0)
            
    except:
        print("notify() failed")

def main():

    print("Running Seat Scraper...\n")

    #Pass url as first command line argument to script
    f = open("course.txt", 'w+')
    f.write(course)
    f.close()

    #go to correct directory
    os.system("cd course_select")
    filename = "course capacity.txt"

    while True:
        #run the crawler, you could set this to /dev/null on Unix but I'm gonna keep it as NUL just so I can see the any Scrapy errors
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