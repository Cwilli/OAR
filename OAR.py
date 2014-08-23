from lxml import html
import requests
import csv
from collections import Counter
import re

# Goes to the webpage where the song is located

page = requests.get('https://lyrics.wikia.com/O.A.R.:I_Feel_Home')
lyrics = html.fromstring(page.text)

# Pulls the song lyrics for "Home"

song_lyrics = lyrics.xpath('//div[@class="lyricbox"]/text()')

# writes the song to a text file

songfile = open('Song_Lyrics.txt', 'w')
songfile.write(repr(song_lyrics))
songfile.close()

# Takes the Song List File, splits the words
# And makes them lower case

filename = "Song_Lyrics.txt"
textfile = open(filename, 'r')
wordlist = re.split('\W+', file(filename).read().lower())

# Prints out the top X Words

print Counter(wordlist).most_common(15)
