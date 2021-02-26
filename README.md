# myscripts
Scripts that make my experience easy enough 

### configuration
Just add the folder `bin` to system path by adding following line to your `bashrc`:

```bash
export PATH=${PATH}:"/home/username/path-to-bin/"
```


## temperature.sh
A bash script to get the temperature info of your cpu

## earthquake.py
A python script to view the **five** recent earthquakes in Nepal

## livescore.py
A python script to get the score information

### usage
- for viewing all the available today's scores:
    ```bash
    python3 livescore.py
    ```

- for searching a specific club/team 
`-s` or `--search`
    ```bash
    python3 livescore.py -s teamname
    ```

## mangascraper.py
A python script to get the chapter list of manga.

### usage
```bash
python3 mangascraper.py
```

```bash
python3 mangascraper.py manga name with spaces
```

## vianet.py
A python script to get the current status of my vianet plan

## paradoxnet.py
A python script to scan and connect to nearby networks.  
Uses `iwlist` to scan the network and `nmcli` for connecting.

```bash
python3 paradoxnet.py
```

### usage
- scan nearby wifi networks
    ```bash
    python3 paradoxnet.py -s
    ```
- connect to wifi secured networks
    ```bash
    python3 -n net_name -p password_here
    ```
- connect to wifi open networks
    ```bash
    python3 -n net_name
    ```

## sc.py
A simple soundcloud track downloader. It needs your client id which you should get from the soundcloud api.


## scmd

A naive tool to search over my cmd logs.

I usually store every command I type in the terminal at `~/.logs/` direcotory. 

#### Usage
`python scmd.py <token1> <token2> ... `

The arguments are **ANDed**. That is, for each line in the log, if all the token are found, it's a match.

More the tokens, more concise is the search.

This script can be put in the system path.
