## BCB '22

This year there are no named tracks. (perhaps I cannot access all of them?).  For this year, we will go based on the submission ID. The code is changed for this.

## Posters Enhanced CSV

The 13 accepted posters are:

- 1,2,4,46,51,53,58,63,105,126,170,171,172

Download the files from EasyChair (`submission-full.csv` and `author.csv`).  

```
python3 ../convert.py poster-submission.csv poster-authors.csv poster 1,2,4,46,51,53,58,63,105,126,170,171,172 ACM-BCB-2022-posters.csv
```

Output:

```
Pulling these columns from the submissions CSV file: #,title,decision
  found 13 decisions of type accept
13 accepted titles processed
Pulling these columns from the authors CSV file: submission #,first name,last name,email,country,affiliation,corresponding?
authors from 13 accepted submisssions processed
Wrote to ACM-BCB-2022-posters.csv
```

To check the number of submissions that are in the enhanced CSV (there should be 13):

```
cut -d "," -f 2 ACM-BCB-2022-posters.csv  | sort -u | wc -l
```

## Full Papers Enhanced CSV

The full paper IDs are:

- TBD

both files list full and short papers as track 1.

```
python3 ../convert.py 1 submission-full.csv author.csv ACM-BCB-2022-full-papers.csv [UPDATE]
```

Output:

```
```

To check the number of submissions that are in the enhanced CSV (there should be TBD):

```
cut -d "," -f 2 ACM-BCB-2022-full-papers.csv  | sort -u | wc -l
```

To check that none of the submissions are short papers (this shouldn't return anything):

```
cut -d "," -f 1-3 ACM-BCB-2022-full-papers.csv  | sort -u | grep -f short.txt
```


## Short Papers Enhanced CSV

The short papers are

- TBD

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
