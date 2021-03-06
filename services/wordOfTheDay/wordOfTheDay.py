import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##    Word of the Day Function     ##
#############################

def getWordData():
    url = 'http://www.merriam-webster.com/word-of-the-day'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        wordHTML = soup.find_all("div", {"class" : "word-and-pronunciation"})[0].h1
        word = str(wordHTML)[4:-5]
        defHTML = soup.find_all("div", {"class" : "wod-definition-container"})[0].p
        definition = (str(defHTML).split("</strong> ")[1])[:-4]

        body = word + ": " + definition
        
    except Exception, e:
        print str(e)
        return "Could not find word of the day data."

    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'This will get the word of the day.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval():
    return getWordData()