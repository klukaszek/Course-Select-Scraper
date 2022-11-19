import scrapy
import fileinput
import re
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup

url = "https://colleague-ss.uoguelph.ca/Student/Student/Courses/Search?keyword=cis*4820"

class SplashScraper(scrapy.Spider):

    name = "course"

    lua_script = """
    function main(splash)
        splash.private_mode_enabled = false
        assert(splash:go(splash.args.url))
    
        splash:set_viewport_size(1280, 1080)
        
        splash:wait(1)
        
        splash:mouse_hover(700, 550)
        splash:mouse_click(700, 550)
    
        splash:wait(1)
        return {html = splash:html(), png = splash:png()}
    end
    """

    def start_requests(self):
        yield SplashRequest(url, self.parse, endpoint="execute", args={'lua_source': self.lua_script})

    def parse(self, response):
        filename = "course capacity.txt"

        #use beautiful soup parse html
        soup = BeautifulSoup(response.body, "lxml")

        #remove useless tags
        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text()

        #get seat count
        text = re.findall("[\d]+[ ][\/][ ][\d]+[ ][\/][ ][\d]+", text)

        f = open(filename, 'w+')
        f.write(str(text[0]))
        f.close()

