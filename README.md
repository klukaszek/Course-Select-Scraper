# Course-Select-Scraper

## Dependencies

#### This script requires Scrapy to be installed on your system: 
`pip install scrapy`

#### This script requires Scrapy_Splash to be installed on your system: 
`pip install scrapy-splash`

#### This script requires BeautifulSoup4 to be installed on your system: 
`pip install beautifulsoup4`

### This script requires Sendgrid API to be installed on your system:
`pip install sendgrid`

### You will need to have a Sendgrid API Key set as an environment variable titled SENDGRID_API_KEY, you should probably put it in .bashrc if you are using a Unix based OS.
`export SENDGRID_API_KEY=YOUR_PERSONAL_API_KEY` 

#### This requires a Docker container of Splash to be installed and running on port 8050 to work properly.
Once installed: `docker run -p 8050:8050 scrapinghub/splash`

## Example Execution
`python script.py cis4820 sampleemail@email.net`

The course code provided should be in lowercase with no spaces.

## Notes
At the moment, this gets the seat count by using mouse inputs but that won't work in every case so I have to look into interacting with Javascript without input using Splash LUA scripting and some Javascript.

To run the crawler, go to the /course_select directory and run `./script.py {Course Code} {Sendgrid Email}` or `python script.py {Course Code} {Sendgrid Email}` to get the number of seats available for your course.

The {Sendgrid Email} provided will send an email to itself when a seat is available so you should make sure that the Sendgrid Email you have set up can receive mail.
