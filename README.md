### Movie Trailer Project

This repository has a movie trailer project code.
When the code gets run, it opens up a browser and shows the list of movies.
Each movie has a link to YouTube trailer.
When a movie image is clicked, the trailer starts in the browser.

### Usage

To see the movie trailer, hit the commend below:

```bash
bin/show.sh
```

All movie informations are saved in a json file, `data/movies.json`.
The code reads the data from `data/movies.json` and creates a html file.


### Directory structure

This repository has files below:

```
.
├── README.md
├── assets
│   └── brick_wall.png
├── bin
│   └── show.sh
├── data
│   └── movies.json
├── media
│   ├── __init__.py
│   ├── core.py
│   ├── fresh_tomatoes.py
│   └── movie.py
└── tests
    ├── __init__.py
    └── basic_test.py
```

- README.md: this file
- assets: assets directory, background image exists
- bin: executable commands directory, `show.sh` is here
- data: data directory, movie data in json format is in this directory
- media: source directory
- tests: test code directory


### Tests

To run test, go to the top directory and type the command below:

```bash
python tests/basic_test.py
```
