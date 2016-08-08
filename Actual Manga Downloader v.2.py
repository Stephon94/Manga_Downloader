import urllib2 as look
import requests
import os
from bs4 import BeautifulSoup
import sqlite3

print "Welcome and Thank You for using my personal Manga Downloader!\nWhenever you are finished using it, just press 'Ctrl' + 'C' for Windows & 'Cmnd' + 'C' for Macs to close the program"
print"__________________________________________"
print"__________________________________________"

website = 'http://www.mangareader.net'
DIR = os.path.dirname(os.path.dirname(__file__))

def mangaSetup():
    #Gets all the mangas hosted on the site
    pageOfMangas = 'http://www.mangareader.net/alphabetical'
    soup = BeautifulSoup(look.urlopen(pageOfMangas).read(), "html.parser")

    mangaDict = {}
    refineMangaDict ={}
    for col in soup.findAll("div", { "class" : "series_col" }):
        for li in col.findAll('li'):
            mangaDict[li.a.string.title()] = li.a['href']
            
   #Obtains name of Manga 
    mangaName = raw_input('What manga are you looking for? ').title()

    if len(mangaName) == 0:
            print "Please enter a manga name"
            print"__________________________________________"
            print"__________________________________________"
            mangaSetup()
    #Either displays all the mangas with the name you entered, and asks which one you want to download OR if only one manga has that name, downloads it.
    if len(mangaName) >= 1:
        mangas = 0
        for key in mangaDict.keys():
            if key.startswith(mangaName):
                mangas += 1
                refineMangaDict[key] = mangaDict.get(key)

        if mangas > 1:
            for key in refineMangaDict.keys():
                print key

            mangaName = raw_input("Which manga do you want to download from?").title()
            mangaLink = mangaDict.get(mangaName)

            manga_DIR = os.path.join(DIR, 'Mangas', mangaName)
                    

        else:
            mangaLink = refineMangaDict[refineMangaDict.keys()[0]]
            
            print mangaLink
                    
            manga_DIR = os.path.join(DIR, 'Mangas', mangaName)        
            

    
    #Initializing a variable that holds the mangas home page
    mangaHome = website+mangaLink
    
    #Checking if the users input exists or is correct
    try:
        soup = BeautifulSoup(look.urlopen(mangaHome).read(), "html.parser")
    except:
        print "Something went wrong, check entry and try again!"
        mangaSetup()
    #Checking if User already has a directory for said manga. If yes, change into that directory.
    try:
        os.chdir(manga_DIR)
    #If User doesn't have a directory for said manga, one is created then changed into.
    except:
        os.mkdir(manga_DIR)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        os.chdir(manga_DIR)
            

        
    while True:
        decision = raw_input("Do you want the whole manga? y or n: ").lower()
        if decision == "y":
            entireManga(mangaLink, mangaHome, mangaName, manga_DIR)
        elif decision == "n":
            while True:
                mangaChapter = raw_input("What manga chapter would you like? ")
                try:
                    int(mangaChapter)
                    break
                    
                except:
                    print "Please enter a number"
                    continue
        else:
            continue

              
        oneChapter(mangaLink, mangaHome, mangaName, manga_DIR, mangaChapter)
        break 

def entireManga(mangaLink, mangaHome, mangaName, manga_DIR):
    
    #Going to set manga chapter to 1, since were starting from the beginning
    mangaChapter = 1
    
    #Just like the manga name, checking if you already have the 1st chapter (most likely you won't, but just a failsafe)
    try:
        os.chdir(os.path.join(manga_DIR, str(mangaChapter)))
        
    #If I can't change into the directory, it doesn't exist. So it's created then changed into.
    except:
        os.mkdir(os.path.join(manga_DIR, str(mangaChapter)))
        os.chdir(os.path.join(manga_DIR, str(mangaChapter)))
        
    #Initializing the variable which will be used for the naming of each manga page
    fileNameNum = 0
    
    #initializing a variable that holds what would be considered the "next page" of the manga
    nextPage = mangaLink+"/"+str(mangaChapter)
    
    try:
        #Initializes a variable that holds the beginning of the manga, then passes it through Beautiful Soup for parsing   
        mangaBegins = mangaHome+'/'+str(mangaChapter)
        soup = BeautifulSoup(look.urlopen(mangaBegins).read(), "html.parser")
        
        #Initializes a variable that holds the chapter number for each page being downloaded   
        chapterNum = int(nextPage.split("/")[2])
        
        #Starts a loop so that each page will be downloaded.   
        while chapterNum == mangaChapter:
            #Starts another loop that finds the manga pages image link & sets it a variable
            for a in soup.find_all('img', src=True):
                        if len(a['src']) > 0:
                            image = a['src']
                            
                            #Taking the same variable for each manga page and making sure it adds one for each page downloaded.
                            fileNameNum += 1
                            
                            #Initializes variable for the actual name of the downloaded manga page
                            fileName = '0' + str(fileNameNum) +'.jpg'
                            
                            #This creates the file, saves the manga page as this file, then closes the file.
                            f = open(fileName,'wb')
                            f.write(requests.get(image).content)
                            f.close()
                            
                            #Just letting the user know their progress, showing what's been downloaded so far
                            print nextPage, 'Successfully downloaded!'
                        
            #Parses the the html look for the specific link for the next page and sets it to the recently made nextPage variable            
            for span in soup.find_all('span', {'class' : "next"}):
                nextPage = span.a['href']

                #Checking each page to know when the next chapter starts.
                chapterNum = int(nextPage.split("/")[2])
                if chapterNum != mangaChapter + 1:
                    nextPage = nextPage
                    soup = BeautifulSoup(look.urlopen(website+nextPage).read(),"html.parser")
                    
                else :
                    #Changing the variable for the current Chapter being downloaded to the next one so the while loop will continue
                    mangaChapter = chapterNum
                    nextPage = nextPage
                    soup = BeautifulSoup(look.urlopen(website+nextPage).read(),"html.parser")

                    #Checking to see if a manga image is present at the beginning of the chapter, if there's none, we know that chapter wasn't released yet
                    image = soup.find("img", { "id" : "img" })
                    
                    
                    #If there is an image, then we know that chapter is downloadable, so a folder is made for that chapter and changed into.
                    if image != None:
                        try:
                            os.chdir(os.path.join(manga_DIR, str(mangaChapter)))
                        except:
                            os.mkdir(os.path.join(manga_DIR, str(mangaChapter)))
                            os.path.join(manga_DIR, str(mangaChapter))

                        #File number reset because this is a new chapter
                        fileNameNum = 0
                    else:
                        print"Entire", mangaName.title(),"series up to date has been downloaded.....enjoy!"
                        mangaSetup()   
    #Just printing out any errors without actually breaking the code.               
    except Exception,e:
        print str(e)



def oneChapter(mangaLink, mangaHome, mangaName, manga_DIR, mangaChapter):
    #Just like the manga name, checking if you already have the 1st chapter (most likely you won't, but just a failsafe)
    try:
        os.chdir(os.path.join(manga_DIR, str(mangaChapter)))
        print "Hi"
        
    #If I can't change into the directory, it doesn't exist. So it's created then changed into.
    except:
        os.mkdir(os.path.join(manga_DIR, str(mangaChapter)))
        os.chdir(os.path.join(manga_DIR, str(mangaChapter)))
        
    #Initializing the variable which will be used for the naming of each manga page
    fileNameNum = 0
    print fileNameNum
    #initializing a variable that holds what would be considered the "next page" of the manga
    nextPage = mangaLink+"/"+str(mangaChapter)
    print "Hi"

    #Initializes a variable that holds the beginning of the manga, then passes it through Beautiful Soup for parsing   
    mangaBegins = mangaHome+'/'+str(mangaChapter)
    
    soup = BeautifulSoup(look.urlopen(mangaBegins).read(), "html.parser")
    
    
    #Initializes a variable that holds the chapter number for each page being downloaded   
    chapterNum = int(nextPage.split("/")[2])
    
    #Starts a loop so that each page will be downloaded.   
    while chapterNum == int(mangaChapter):
        #Starts another loop that finds the manga pages image link & sets it a variable
        for a in soup.find_all('img', src=True):
                    if len(a['src']) > 0:
                        image = a['src']
                        
                        #Taking the same variable for each manga page and making sure it adds one for each page downloaded.
                        fileNameNum += 1
                        
                        #Initializes variable for the actual name of the downloaded manga page
                        fileName = '0' + str(fileNameNum) +'.jpg'
                        
                        #This creates the file, saves the manga page as this file, then closes the file.
                        f = open(fileName,'wb')
                        f.write(requests.get(image).content)
                        f.close()
                        
                        #Just letting the user know their progress, showing what's been downloaded so far
                        print nextPage, 'Successfully downloaded!'
                    
        #Parses the the html look for the specific link for the next page and sets it to the recently made nextPage variable            
        for span in soup.find_all('span', {'class' : "next"}):
            nextPage = span.a['href']

            #Checking each page to know when the next chapter starts.
            chapterNum = int(nextPage.split("/")[2])
            if chapterNum != int(mangaChapter) + 1:
                nextPage = nextPage
                soup = BeautifulSoup(look.urlopen(website+nextPage).read(),"html.parser")
            else:
                print "Enjoy your manga chapter!"
                mangaSetup()
        
mangaSetup()
