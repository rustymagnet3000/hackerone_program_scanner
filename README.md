# HackerOne company scrape

HackerOne introduced "hacker" facing APIs in 2021.  This repo uses one of those APIs to find all of the `Public` programs.  
```
GET https://api.hackerone.com/v1/hackers/programs
```
The API does not reveal info about `Private` programs.

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