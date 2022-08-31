# Spotifast

Spotifast is a straight-forward Python script to download .mp3 files from a complete Spotify playlist in 320kbp/s.

## Installation

Clone this git repository. In addition, you also need to create Spotify developer credentials. This can easily be done if you have a regular Spotify account at https://developer.spotify.com/ Use these credentials in the python script.

## Usage

Change these in the file (important: keep as strings so do not remove the quotation marks):

```
cid = "PUT SPOTIFY CLIENT ID HERE"
secret = "PUT SPOTIFY SECRET KEY HERE"
playlist_LINK = "PUT SPOTIFY PLAYLIST LINK HERE (such as https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=f22367f331da414b)"
```

then run
```
python main.py
```

## Todo
-Easier user experience (GUI, no need for spotify developer credentials, choose download destination folder)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 

Credits go to myfreemp3juices.cc because this script uses their database.
