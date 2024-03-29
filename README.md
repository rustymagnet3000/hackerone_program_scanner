# HackerOne company scrape

### Use H1 APIs

HackerOne introduced "hacker" facing APIs in 2021.  This repo uses one of those APIs to find all of the `Public` programs.  

```
GET https://api.hackerone.com/v1/hackers/programs
```

The API does not reveal info about `Private` programs.


### Usage

```bash
# Set credentials file /.env
H1_USERNAME  = < write email used to log into H1 >
H1_API_TOKEN = < paste API Token from H1 >

# poetry ( inside of /src folder )
poetry run h1-script

# python3
python3 src/__main__.py
```

### Overview

```
| --------------- |      | -------------- |       | -------------- |
| 1. Get H1 info  | -->  | 2. Scrape data |  -->  | 3. Check words | 
| --------------- |      | -------------- |       | -------------- |
```

### Scraping

There was no API to get the contents of a companies HackerOne program.  This meant a scraping approach.

Out of the box, the below won't work.

```
    req = Request('https://hackerone.com/coinbase')
    urlopen(req).read()
```

Logic on H1 was checking for a header before revealing the Company written Bug Bounty policy.  

After trial and error, it was clear that HackerOne was checking the request was made with Javascript.
```
    'X-Requested-With': 'XMLHttpRequest'
```
### Add words

To expand the spelling check add them to: `/conf/words.toml`.

### Test

```zsh
poetry run pytest -xvs tests/
```

### References

```
https://www.dcs.bbk.ac.uk/~roger/missp.dat
https://en.wikipedia.org/wiki/Commonly_misspelled_English_words
```
