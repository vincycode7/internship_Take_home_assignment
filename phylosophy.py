#import packages
import urllib.request,re,time
from bs4 import BeautifulSoup

#Initialize some useful variables
url = input('Input a link: ')
vst_lnk = dict()
link = "https://en.wikipedia.org"

#Begin the Click Loop
while True:
    
    #send a request
    html = urllib.request.urlopen(url)
    time.sleep(0.5)
    soup = BeautifulSoup(html,'html.parser')

    #using beatufulsoup package to bringout <p>
    ptags = soup('p')

    titletage = str(soup('title')[0].contents[0].split('-')[0])
    if titletage == 'Philosophy' or titletage in list(vst_lnk.keys()): break
    print(titletage)

    #saving both the title and url to check if stuck in a loop
    vst_lnk[titletage] = html

    #regex to parse links
    aa = re.findall('.*?(<a.*?>.*?</a>).*?', str(ptags))

    #code to asign the first link to url
    for i in aa:
        if len(re.findall('.*?<a.*?>(.*])</a>.*?', i)) == 0:
            url = link+re.findall('.*?<a href="(.*?)".*?>.*</a>.*?', i)[0]
            break
        continue