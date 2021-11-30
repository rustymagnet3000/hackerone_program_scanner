# HackerOne company scrape

### Use H1 APIs

HackerOne introduced "hacker" facing APIs in 2021.  This repo uses one of those APIs to find all of the `Public` programs.  

```
GET https://api.hackerone.com/v1/hackers/programs
```

The API does not reveal info about `Private` programs.

### Scraping

There was no API to get the contents of a companies H1 program.  This meant a scraping approach.

Out of the box, the below won't work.

```
    session = HTMLSession()
    resp = session.get('https://hackerone.com/coinbase')
```
Some logic on H1 was checking for a header before revealing the Company written Bug Bounty policy.  After trial and error, it was clear that H1 was checking the request was made with Javascript.
```
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest'
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

