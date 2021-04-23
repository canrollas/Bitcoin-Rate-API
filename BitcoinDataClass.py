
from bs4 import BeautifulSoup as bs

import requests

class BitcoinDataClass:

    def dataPrint(self):
        webExtraction="https://www.google.com/search?q=bitcoin+rate"
        HTML=requests.get(webExtraction)
        soup=bs(HTML.text,'html.parser')

        data=str(soup.find("div" ,attrs={'class':'BNeawe iBp4i AP7Wnd'}).find("div" ,attrs={'class':'BNeawe iBp4i AP7Wnd'}))
        data=data.split(">")
        counter=0
        for i in data:
            if("<" in i):
                data[counter]=i.split("<")
            counter=counter+1
        new_list=list()
        for i in data:
            for seconder in i:
                if(seconder!="" and not("div" in seconder)):
                    new_list.append(seconder)
                    return seconder

