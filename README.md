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

Add words to `/conf/words.toml`.

```
git update-index --assume-unchanged conf/words.toml
```

### Usage

```zsh
python3 src/
```

### Overview

```
| --------------- |      | -------------- |       | -------------- |
| 1. Get H1 info  | -->  | 2. Scrape data |  -->  | 3. Check words | 
| --------------- |      | -------------- |       | -------------- |
```

