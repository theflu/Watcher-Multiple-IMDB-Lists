#!/usr/bin/python
import json
import requests
import xml.etree.ElementTree as ET

# Watcher info
w_host = '192.168.1.100'
w_port = '9090'
w_subdir = ''
w_api_key = '00000000000000000000000000000000'
w_ssl = False

# IMDB lists to check
imdb_lists = [
'http://rss.imdb.com/user/ur00000000/watchlist',
'http://rss.imdb.com/list/ls000000000/'
]

# Dedupe list
def uniq(seq):
  seen = set()
  seen_add = seen.add
  return [x for x in seq if not (x in seen or seen_add(x))]

# Get lists from IMDB
imdb_ids = []

for url in imdb_lists:
  r = requests.get(url)
  list = ET.fromstring(r.text)
  
  for item in list[0]:
    if item.tag == 'item':
	  movie = item[2].text.split('/')
	  imdb_ids.append(movie[len(movie)-2])

imdb_ids = uniq(imdb_ids)

# Build API url
if w_ssl:
  url = 'https://'
else:
  url = 'http://'
  
url = url+w_host+':'+w_port
  
if len(w_subdir) > 0:
  url = url+'/'+w_subdir

url = url+'/api?apikey='+w_api_key

# Get current movies in Watcher
r = requests.get(url+'&mode=liststatus')
liststatus = json.loads(r.text)
current_movies = []

for movie in liststatus['movies']:
  current_movies.append(movie['imdbid'])

# Add movies to Watcher
for id in imdb_ids:
  if id not in current_movies:
    r = requests.get(url+'&mode=addmovie&imdbid='+id)