# myscripts
Scripts that make my experience easy enough 

### configuration
Just add the folder `bin` to system path by adding following line to your `bashrc`:

```bash
export PATH=${PATH}:"/home/username/path-to-bin/"
```

### Some Scripts

#### temperature.sh
A bash script to get the temperature info of your cpu

#### earthquake.py
A python script to view the **five** recent earthquakes in Nepal

#### livescore.py
A python script to get the score information

##### usage
- for viewing all the available today's scores:
    ```bash
    python3 livescore.py
    ```

- for searching a specific club/team 
`-s` or `--search`
    ```bash
    python3 livescore.py -s teamname
    ```

#### mangascraper.py
A python script to get the chapter list of manga.

##### usage
```bash
python3 mangascraper.py
```

```bash
python3 mangascraper.py manga name with spaces
```

