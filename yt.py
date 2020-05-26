import pafy
from urllib.parse import *
from bs4 import BeautifulSoup
import urllib.request
import random
import time
import os
import pyglet

print("Welcome!!\n You can download songs or listen  to them.\n Press ctrl+c while the song is playing to enter another song.\n Enjoy!!")

while True:
  try:
    os.remove('song.m4a')
  except:
    pass

  search = input("Which song is on your mind: ")
  search_url = "https://www.youtube.com/results?search_query="+urllib.parse.quote_plus(search)
  try:
    response = urllib.request.urlopen(search_url)
  except:
    print("Make sure you have an active internet connection")
    continue
  html = response.read()
  soup = BeautifulSoup(html, 'lxml')
  #print(soup.prettify())
  titles = soup.find_all('h3',{"class":"yt-lockup-title"})
  tags= soup.findAll(attrs={"class":"yt-uix-tile-link"})[0:5]
  results={}

  for tag in tags:
      results[tag['title']]='https://www.youtube.com'+tag['href']

  for i,title in enumerate(list(results.keys())):
      print(f"{i+1}."+f" {title}")
  i=input("These are the top 5 results. Which one out of these? ")
  m = input("type d to download or l to listen now: ")
  url = list(results.values())[int(i)-1]
  video = pafy.new(url)
  audio = video.getbestaudio(preftype="m4a")
  duration = video.length

  if m=='l':
    audio.download('song.m4a', quiet=True)
    song = pyglet.media.load('song.m4a')
    player = pyglet.media.Player()
    player.queue(song)
    #player.play()
    print(duration)
    timeout = time.time()+duration
    try:
      while time.time()<timeout:
        player.play()
        star='*'
        i= random.randint(1,50)
        print(star*i)
        print(star*i)
        time.sleep(0.05)
     
    except KeyboardInterrupt:
        player.pause()
        continue 
  elif m=='d':
    audio.download(list(results.keys())[int(i)-1]+'.m4a')
    continue

  player.pause()
  try:
    os.remove('song.m4a')
  except:
    pass

  #continue
