# HackerOne company scrape

### Use H1 APIs

HackerOne introduced "hacker" facing APIs in 2021.  This repo uses one of those APIs to find all of the `Public` programs.  

```
GET https://api.hackerone.com/v1/hackers/programs
```

The API does not reveal info about `Private` programs.

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

To expand the spelling mistakes to check for, add them to: `/conf/words.toml`.

```
git update-index --assume-unchanged conf/words.toml
```

### Test

```zsh
poetry run pytest -xvs tests/
```

### Overview

```
| --------------- |      | -------------- |       | -------------- |
| 1. Get H1 info  | -->  | 2. Scrape data |  -->  | 3. Check words | 
| --------------- |      | -------------- |       | -------------- |
```

### References

```
https://www.dcs.bbk.ac.uk/~roger/missp.dat
https://en.wikipedia.org/wiki/Commonly_misspelled_English_words
```
