# Course-Select-Scraper

### This requires Scrapy to be installed on your system.
### This requires a Docker container of Splash to be installed and running on port 8050 to work properly.

At the moment, this gets the seat count by using mouse inputs but that won't work in every case so I have to look into interacting with Javascript without input using scrapy_splash.

To run the crawler, go to the /course_select directory and execute "./script.py" or "python script.py" to get the number of seats available for your course.

Script.py easily be repurposed to notify by text or email that a seat is available if I really wanted to.
