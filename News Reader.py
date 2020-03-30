#watch youtube video you will get to know what actually this code does
# link is given in description

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import os
import playsound
from gtts import gTTS

i = 0


def speak(text):
    global i
    filename = 'voice' + str(i) + '.mp3'
    i += 1
    audio = gTTS(text=text, lang='en')
    audio.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


speak('Welcome User!')
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = dict()
hdline = list()
links = list()
more = list()
# url = input('Enter - ')
url = 'https://www.indiatoday.in/'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html5lib')
# print(soup.prettify())
match = soup.find('ul', class_='itg-listing')
# print(match.li.a.text)
for x in match.findAll('li'):
    try:
        headline = x.a.text
        z = x.a['href']
        link = url + z
        data[headline] = link
        hdline.append(headline)
        links.append(link)

    except Exception as e:
        pass
totalInfo = len(hdline)
print('Total News :', totalInfo)
info = 0
while info < totalInfo:
    ask = input('Enter n to go to next news :  ')
    if ask.lower() == 'n':
        print('News ', info+1)
        print(hdline[info])
        speak(hdline[info])
    ask = input('Do you want to Know More y/n ?')
    if ask.lower() == 'y':
        print('Directing to :', links[info])
        html = urlopen(links[info]).read()
        soup = BeautifulSoup(html, 'html5lib')
        # print(soup.prettify())
        try:
            match = soup.find('div', class_='description')
            count = 0
            for des in match.findAll('p'):
                print(des.text)
                count += 1
                if count >= 2:
                    break
        except Exception as e:
            print('Sorry! Not Found')



    info += 1

print('Thank You!')
