# Course-Select-Scraper

### This requires Scrapy to be installed on your system.
### This requires a Docker container of Splash to be installed and running on port 8050 to work properly.

At the moment, this gets the seat count by using mouse inputs but that won't work in every case so I have to look into interacting with Javascript without input using scrapy_splash.

Use "scrapy crawl course" on Windows to get number of seats available for your course.

This can easily be repurposed to notify by text or email that a seat is available if some other Python script keeps crawling and updating the seat count.
