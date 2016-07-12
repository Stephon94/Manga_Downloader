import urllib2
from bs4 import BeautifulSoup

url = urllib2.urlopen('http://www.mangareader.net/alphabetical').read()
soup = BeautifulSoup(url, "html.parser")

mangaList = []
mangaListLnks = []

for li in soup.find_all('li'):
    try:
        if li.a.string != None and len(li.a.string) > 1:
            print li.a.string
            mangaList.append(li.a.string)
            #mangaList = tuple(mangaList)
            
            mangaListLnks.append(li.a['href'])
            #mangaListLnks = tuple(MangaListLnks)
            
    except:
        pass

for mangas in mangaList:
    try:
        if "pokemon" in str(mangas).lower():
            print mangas
            indexx = mangaList.index(mangas)
            print indexx
            print mangaListLnks[indexx]
    except:
        pass



