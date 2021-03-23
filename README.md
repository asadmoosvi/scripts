# scripts

- omdb (get information about a movie)
    - need a valid OMDB api key (set it in the `OMDB_KEY` env var)
- tastedive (get similar shows/movies using the tastedive api)
    - need a valid TASTEDIVE key (set it in the `TASTEDIVE_KEY` env var)
    - imdb based search results will be shown if OMDB key is also present
- search-torrent (search for torrents on piratebay)
- hn.py (fetch the top hackernews links of the day)
- word.py (get the definition of a word)
    - this is provided by the unofficial google api at [dictionaryapi.dev](https://dictionaryapi.dev/)
- clone-repos (clone a github user's repos)
- pull-all.py (git pull all repos that can be found in `~/Code/github/`)
- wttr (helper script to get weather info from wttr.in)
- websearch (search for something on one of several websites and open in browser)
- play-songs (search for songs using youtube-dl then play their audio using mpv)
- fake-ua (get a fake user agent)
- get-ghdir (download a specific directory from a repo on github)


## where to get the keys?

- [OMDB API Key](http://www.omdbapi.com/apikey.aspx)
- [Tastedive API Key](https://tastedive.com/read/api)
