## BCB '21 Tracks

- 1 - "Main Conference Track (Papers)","ACM BCB 2021 Main Conference Track (Papers)"
- 2 - "Highlights Track","ACM BCB 2021 Highlights Track"
- 3 - "Workshop Proposals Track","ACM BCB 2021 Workshop Proposals Track"
- 4 - "Tutorials Track","ACM BCB 2021 Tutorials Track"
- 5 - "Posters Track","ACM BCB 2021 Posters Track"

## Posters Enhanced CSV

Download the files from EasyChair (`submission-full.csv` and `author.csv`).  Get the posters (track 5).

```
python3 ../convert.py 5 submission-full.csv author.csv ACM-BCB-2021-posters.csv
```

Output:

```
Pulling these columns from the submissions CSV file: #,title,decision
Checking that track # == 5
  found 22 decisions of type "accept"
22 accepted titles processed
Pulling these columns from the authors CSV file: submission #,first name,last name,email,country,affiliation,corresponding?
authors from 22 accepted submisssions processed
Wrote to ACM-BCB-2021-posters.csv
```

To check the number of submissions that are in the enhanced CSV (there should be 22):

```
cut -d "," -f 2 ACM-BCB-2021-posters.csv  | sort -u | wc -l
```

## Full Papers Enhanced CSV

Download the files from EasyChair (`submission.csv` and `author.csv`).  Split `submission.csv` into `submission-full.csv` and `submission-short.csv`. The 17 short papers are

- 151, 68, 83, 74, 128, 17, 152, 31, 77, 100, 111, 140, 9, 67, 78, 82, 84.

both files list full and short papers as track 1.

```
python3 ../convert.py 1 submission-full.csv author.csv ACM-BCB-2021-full-papers.csv
```

Output:

```
Checking that track # == 1
  found 40 decisions of type "accept"
40 accepted titles processed
Pulling these columns from the authors CSV file: submission #,first name,last name,email,country,affiliation,corresponding?
authors from 40 accepted submisssions processed
Wrote to ACM-BCB-2021-full-papers.csv
```

To check the number of submissions that are in the enhanced CSV (there should be 40):

```
cut -d "," -f 2 ACM-BCB-2021-full-papers.csv  | sort -u | wc -l
```

To check that none of the submissions are short papers (this shouldn't return anything):

```
cut -d "," -f 1-3 ACM-BCB-2021-full-papers.csv  | sort -u | grep -f short.txt
```


## Short Papers Enhanced CSV

Again, the 17 short papers are

- 151, 68, 83, 74, 128, 17, 152, 31, 77, 100, 111, 140, 9, 67, 78, 82, 84.

both files list full and short papers as track 1.

```
python3 ../convert.py 1 submission-short.csv author.csv ACM-BCB-2021-short-papers.csv
```

Output:

```
Pulling these columns from the submissions CSV file: #,title,decision
Checking that track # == 1
  found 17 decisions of type "accept"
17 accepted titles processed
Pulling these columns from the authors CSV file: submission #,first name,last name,email,country,affiliation,corresponding?
authors from 17 accepted submisssions processed
Wrote to ACM-BCB-2021-short-papers.csv
```

**Replace "Full Paper" with "Short Paper" in the final CSV file.** To check the number of submissions that are in the enhanced CSV (there should be 17):

```
cut -d "," -f 2 ACM-BCB-2021-short-papers.csv  | sort -u | wc -l
```

To check that none of the submissions are short papers (there should be 17):

```
cut -d "," -f 1-3 ACM-BCB-2021-short-papers.csv  | sort -u | grep -f short.txt
```
