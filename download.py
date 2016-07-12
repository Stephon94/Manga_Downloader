import requests
import os
from BeautifulSoup import BeautifulSoup

def allthepages(mangaurl):
	images = []
	chapter = 1
	page = 1	
	end = 0 
	while end != 2: 
		try:
			url = requests.get('http://www.mangareader.net'+ mangaurl +'/' + str(chapter) +'/'+ str(page))
			soup = BeautifulSoup(url.text)
			image = soup.find("img", { "id" : "img" })
			print "currently at", chapter, "/", page
			if image is not None:
				images.append(image)
				page += 1
				end = 0
			else:
				page = 1
				chapter += 1
				end += 1
		except:
			print error
	with open(mangaurl[1:]+".html", "wb") as f:
		for image in images:
			f.write(str(image))
		print 'enjoy'
		f.close()

def selectsome(mangaurl, some):
	images = []	 
	for chapter in some:
		page = 1
		while True:
			try:
				url = requests.get('http://www.mangareader.net'+ mangaurl +'/' + str(chapter) +'/'+ str(page))
				soup = BeautifulSoup(url.text)
				image = soup.find("img", { "id" : "img" })
				print "currently at", chapter, "/", page
				if image is not None:
					images.append(image)
					page += 1
				else:
					break
			except:
				print error
	with open(mangaurl[1:]+".html", "wb") as f:
		for image in images:
			f.write(str(image))
		print 'enjoy'
		f.close()	


url = 'http://www.mangareader.net/alphabetical'
r = requests.get(url)
soup = BeautifulSoup(r.text)

animedict = {}
for col in soup.findAll("div", { "class" : "series_col" }):
	for li in col.findAll('li'):
		animedict[str(li.a.string)] = str(li.a['href'])

while True:
	search = raw_input('do you want to search? ')
	if len(search) == 0:
		break
	else:
		for key in animedict.keys():
			if key.startswith(search):
				print key


umanga = raw_input("which manga do you want to download? ").strip()
print umanga 
if umanga in animedict:
	mangaurl = animedict[umanga]
	#format must be '1,2,3,5,6'
	allorselect = raw_input("do you 'all' or enter chapter/s ")
	if allorselect == 'all':
		allthepages(mangaurl)
	else: 
		some = allorselect.split(',')
		selectsome(mangaurl, some)		
else:
	print "can't find it"

 






