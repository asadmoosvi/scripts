# :open_file_folder: Scripts

## :snake: Python Scripts

| Script                 | Description                                                                               | Requirements    |
| ---------------------- | ----------------------------------------------------------------------------------------- | --------------- |
| python/omdb            | get information about a movie                                                             | python          |
| python/tastedive       | get similar shows/movies using the tastedive api                                          | python          |
| python/search-torrent  | search for torrents on piratebay                                                          | python          |
| python/hn              | fetch the top hackernews links of the day                                                 | python          |
| python/word            | get the definition of a word                                                              | python          |
| python/clone-repos     | clone a github user's repositories                                                        | python          |
| python/pull-all        | git pull all repos that can be found in `~/Code/repos/`                                   | python          |
| python/wttr            | helper script to get weather info from wttr.in                                            | python          |
| python/websearch       | search for something on a particular website and open in the browser                      | python          |
| python/fake-ua         | get a fake user agent                                                                     | python          |
| python/get-ghdir       | download a specific directory from a repo on github                                       | python          |
| python/git-ssh-remotes | rename all git remote http origins recursively under current directory to use ssh instead | python          |
| python/mfp             | play music from https://musicforprogramming.net                                           | python          |
| python/download-mfp    | downloads all tracks from https://musicforprogramming.net                                 | python, wget    |
| python/gh-search       | search for a github repo and clone it                                                     | python, gh, fzf |

## :computer: Shell Scripts

| Script               | Description                                                           | Requirements      |
| -------------------- | --------------------------------------------------------------------- | ----------------- |
| shell/fzf/fwiki      | search for articles from the arch wiki in the cli                     | fd, fzf           |
| shell/fzf/fpacman    | search for uninstalled arch linux packages using fzf and install them | fd, fzf, pacman   |
| shell/update-mirrors | update pacman mirrorlist                                              | pacman, reflector |

## :snake: Python Instructions

In order to use the python scripts, make sure to install the required packages listed in `requirements.txt`. You can do that
by running `pip3 install --user -r requirements.txt`.

## :wrench: Adding Scripts to Your Path

In order to add the scripts to your PATH variable so you can run them from anywhere the following bash code may be used.
Make sure to change `scripts_dir` so that it matches where you have stored the repository on your system.

```bash
# add scripts to path
scripts_dir="$HOME/.scripts"
for script_dir in $(find "$scripts_dir" -type d -not -path '*/.git*'); do
  PATH="$PATH:$script_dir"
done
export PATH

```

You may add this code snippet to your `~/.bashrc` file to make it permanent.

## :key: API Keys

- [OMDB API Key](http://www.omdbapi.com/apikey.aspx) for omdb
- [Tastedive API Key](https://tastedive.com/read/api) for tastedive
