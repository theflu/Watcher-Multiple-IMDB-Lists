# Watcher Multiple IMDB Lists
Sync multiple IMDB lists/watchlists with Watcher
Only tested with Watcher3

## Setup

Add your watcher config
```python
# Watcher info
w_host = '192.168.1.100'
w_port = '9090'
w_subdir = ''
w_api_key = '00000000000000000000000000000000'
w_ssl = False
```

Add your lists
```python
# IMDB lists to check
imdb_lists = [
'http://rss.imdb.com/user/ur00000000/watchlist',
'http://rss.imdb.com/list/ls000000000/'
]
```

Add to cron to run automatically or run it manually

Note:
Make sure your IMDB lists are set to public.
