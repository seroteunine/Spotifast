import requests, os, sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Spotify setup
cid = "PUT SPOTIFY CLIENT ID HERE"
secret = "PUT SPOTIFY SECRET KEY HERE"
playlist_LINK = "PUT SPOTIFY PLAYLIST LINK HERE (such as https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=f22367f331da414b)"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
playlist_URI = playlist_LINK.split("/")[-1].split("?")[0]
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#Setup driver
browser = webdriver.Chrome(ChromeDriverManager().install())

#Create download folder in current wd
parent_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
path = os.path.join(parent_dir, "Downloaded at " + time.strftime("%Y-%m-%d  %H %M %S"))
os.mkdir(path)

#Get playlist
songlist = []
for track in sp.playlist_tracks(playlist_URI)["items"]:
    track_name = track["track"]["name"]
    artist_name = track["track"]["artists"][0]["name"]
    songlist.append(artist_name + ' - ' + track_name)

#Loop over songs, acces myfreemp3, search, get href of first result, acces href
numDownloaded = 0
for song in songlist:
    browser.get("https://myfreemp3juices.cc/") 
    query = browser.find_element(By.ID, 'query')
    query.send_keys(song)
    query.send_keys(Keys.ENTER)
    time.sleep(2)
    a = browser.find_elements(By.CLASS_NAME, 'name')
    if a:
        href = a[0].get_attribute('href')
        time.sleep(1)
        r = requests.get(href)  
        with open(os.path.join(path, song + ".mp3"), 'wb') as f:
            f.write(r.content)
        numDownloaded += 1
    
browser.quit()
print('Finished. Number of downloaded songs:', str(numDownloaded), 'Missed:', str(len(songlist) - numDownloaded))