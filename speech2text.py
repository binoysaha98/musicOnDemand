from __future__ import unicode_literals
from bs4 import BeautifulSoup
from playsound import playsound
			
import speech_recognition as sr
import pyaudio
import os
import urllib.request
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3'
    }],
}

r = sr.Recognizer()

with sr.Microphone() as source:
	print('say something')
	audio = r.listen(source)
	
try: 
	print('Google thinks you said ')
	print(r.recognize_google(audio))
	textToSearch = r.recognize_google(audio)
	query = urllib.request.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html,"html.parser")
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
	    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    		ydl.download(['https://www.youtube.com' + vid['href']])
    		playsound('edm.webm')

	    break
except:
	pass