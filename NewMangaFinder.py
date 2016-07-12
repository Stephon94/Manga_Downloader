import urllib2 as look
#import requests
import os
from google import search
from bs4 import BeautifulSoup


mangaName = raw_input('What manga are you looking for? (Please type EXACT name of manga)')
for url in search(mangaName+" site:myanimelist.net", stop=1):
    print url[0]

'''mangaName = mangaName.replace(" ", "-")
mangaName = mangaName.lower()
try:
    os.mkdir("C:/Users/Brian/Desktop/Mangas/"+mangaName.upper())
except:
    os.chdir("C:/Users/Brian/Desktop/Mangas/"+mangaName.upper())
    mangaChapter = raw_input('What Chapter? ')
    try:
        os.chdir("C:/Users/Brian/Desktop/Mangas/"+mangaName.upper()+"/"+mangaChapter)
    except:
        os.mkdir("C:/Users/Brian/Desktop/Mangas/"+mangaName.upper()+"/"+mangaChapter)
        os.chdir("C:/Users/Brian/Desktop/Mangas/"+mangaName.upper()+"/"+mangaChapter)
        mangaURL = 'http://www.mangareader.net'

        

        mangaHome = mangaURL+'/'+mangaName

        theManga = mangaHome+'/'+mangaChapter

        soup = BeautifulSoup(look.urlopen(theManga).read(), "html.parser")

        fileNameNum = 0
        pageNum = 2

        nextPage = ("/"+mangaName+"/"+mangaChapter).split('/')

        try:
            while nextPage[2] == mangaChapter:
                for a in soup.find_all('img', src=True):
                    if len(a['src']) > 0:
                        image = a['src']
                        
                

                fileNameNum = fileNameNum + 1
                fileName = '0' + str(fileNameNum) +'.jpg'

                f = open(fileName,'wb')
                f.write(requests.get(image).content)
                f.close()
                nextPage = mangaName+"/"+mangaChapter+"/"
                
                for a in soup.find_all('a', href=True):
                    if nextPage+str(pageNum) in a['href']:
                        
                        nextPage = a['href']

                soup = BeautifulSoup(look.urlopen(mangaURL+nextPage).read(), "html.parser")
                pageNum = pageNum + 1
                print nextPage, "-Successfully Downloaded"

                nextPage = nextPage.split("/")
        except:
            print "Should be finished."

        print "Yup, Finished!"

    else:
        print"Already own Chapter!"
        
else:
    mangaChapter = raw_input('What Chapter? ')
    try:
        os.chdir("C:/Users/Brian/Desktop/Mangas/"+mangaName+"/"+mangaChapter)
    except:
        os.mkdir("C:/Users/Brian/Desktop/Mangas/"+mangaName+"/"+mangaChapter)
        os.chdir("C:/Users/Brian/Desktop/Mangas/"+mangaName+"/"+mangaChapter)
        mangaURL = 'http://www.mangareader.net'

        

        mangaHome = mangaURL+'/'+mangaName

        theManga = mangaHome+'/'+mangaChapter

        soup = BeautifulSoup(look.urlopen(theManga).read(), "html.parser")

        fileNameNum = 0
        pageNum = 2

        nextPage = ("/"+mangaName+"/"+mangaChapter).split('/')

        try:
            while nextPage[2] == mangaChapter:
                for a in soup.find_all('img', src=True):
                    if len(a['src']) > 0:
                        image = a['src']
                        
                

                fileNameNum = fileNameNum + 1
                fileName = '0' + str(fileNameNum) +'.jpg'

                f = open(fileName,'wb')
                f.write(requests.get(image).content)
                f.close()
                nextPage = mangaName+"/"+mangaChapter+"/"
                
                for a in soup.find_all('a', href=True):
                    if nextPage+str(pageNum) in a['href']:
                        
                        nextPage = a['href']

                soup = BeautifulSoup(look.urlopen(mangaURL+nextPage).read(), "html.parser")
                pageNum = pageNum + 1
                print nextPage, "-Successfully Downloaded"

                nextPage = nextPage.split("/")
        except:
            print "Should be finished."

        print "Yup, Finished!"

    else:
        print"Already own Chapter!"'''
        


