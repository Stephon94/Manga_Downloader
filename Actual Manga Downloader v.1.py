import string
import urllib2 as look
import requests
import os
from bs4 import BeautifulSoup
import re
print "**Welcome and Thank You for using my personal Manga Downloader!**\n**Whenever you are finished using it, just press 'Ctrl' + 'C' for Windows & 'Cmnd' + 'C' for Macs to close the program**"
print"**If you want to see all the manga starting with partiular letter, just enter that letter as your search.**"
print"__________________________________________"
print"__________________________________________"
mangaSite = 'http://www.mangareader.net'
def wholeManga(mangaUrl):
	
    mangaChapter = 1
    fileNameNum = 0
    pageNum = 2
    theManga = mangaSite+mangaUrl+"/"+str(mangaChapter)
    nextPage = (mangaUrl+"/"+str(mangaChapter)).split('/')
    soup = BeautifulSoup(look.urlopen(theManga).read(), "html.parser")
    while int(nextPage[2]) == mangaChapter:
        for a in soup.find_all('img', src=True):
            if len(a['src']) > 0:
                image = a['src']
                
        

        fileNameNum = fileNameNum + 1
        fileName = '0' + str(fileNameNum) +'.jpg'

        f = open(fileName,'wb')
        f.write(requests.get(image).content)
        f.close()
        nextPage = mangaUrl+"/"+str(mangaChapter)+"/"
        nextChapter = mangaUrl+"/"+str(mangaChapter + 1)
        for a in soup.find_all('span.a', href=True):
            try:
                if nextChapter in span.a['href']:

                    nextPage = a['href']

            except:
                if nextPage+str(pageNum) in a['href']:
                    
                    nextPage = a['href']
                

        soup = BeautifulSoup(look.urlopen(mangaSite+nextPage).read(), "html.parser")
        pageNum = pageNum + 1
        print nextPage, "-Successfully Downloaded"

        nextPage = nextPage.split("/")
        if int(nextPage[2]) == mangaChapter + 1:
            mangaChapter == int(nextPage[2])
            try:
                os.chdir("C:/Users/Brian/Desktop/Mangas/"+mangaName.upper()+"/"+str(mangaChapter))
            except:
                os.mkdir("C:/Users/Brian/Desktop/Mangas/"+mangaName.upper()+"/"+str(mangaChapter))
                os.chdir("C:/Users/Brian/Desktop/Mangas/"+mangaName.upper()+"/"+str(mangaChapter))
'''except:
    print "Something went wrong"
    pass'''

    
mangaName = raw_input('What manga are you looking for?')
#mangaName = re.sub('[^a-zA-Z0-9 \n\.]', '', mangaName)
mangaName = mangaName.lower().replace(" ", "-")
        
print mangaSite
mangaHome = mangaSite+'/'+mangaName
print mangaHome
url = 'http://www.mangareader.net/alphabetical'
urlAccess = look.urlopen(url).read()
soup = BeautifulSoup(urlAccess, "html.parser")

mangaDict = {}
refineMangaDict ={}
for col in soup.findAll("div", { "class" : "series_col" }):
    for li in col.findAll('li'):
        mangaDict[li.a.string] = li.a['href']
        

if len(mangaName) == 0:
        print "Please enter a manga name"
        print"__________________________________________"
        print"__________________________________________"
        mangaDownloader()

if len(mangaName) >= 1:
    mangas = 0
    for key in mangaDict.keys():
        if key.title().startswith(mangaName.title().replace("-"," ")):
            mangas += 1
            refineMangaDict[key] = mangaDict.get(key)
            
    
                
    if mangas > 1:
        for key in refineMangaDict.keys():
            print key
        
        selectedManga = raw_input("Which manga do you want to download from?")
        mangaUrl = mangaDict.get(selectedManga)
        print mangaUrl
        #return mangaUrl
        

    else:
        mangaUrl = refineMangaDict[refineMangaDict.keys()[0]]
        
        print mangaUrl
        #return mangaUrl
else:
    print"Sorry, we don't seem to have that manga. Try another."
    print"__________________________________________"
    print"__________________________________________"
    #mangaDownloader()

    
#mangaDownloader()
decision = raw_input("Do you want the whole manga?")
#mangaUrl = mangaDownloader()
if decision == "y":
    wholeManga(mangaUrl)
