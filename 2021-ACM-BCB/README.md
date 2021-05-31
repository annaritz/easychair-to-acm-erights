## BCB '21 Tracks

- 1 - "Main Conference Track (Papers)","ACM BCB 2021 Main Conference Track (Papers)"
- 2 - "Highlights Track","ACM BCB 2021 Highlights Track"
- 3 - "Workshop Proposals Track","ACM BCB 2021 Workshop Proposals Track"
- 4 - "Tutorials Track","ACM BCB 2021 Tutorials Track"
- 5 - "Posters Track","ACM BCB 2021 Posters Track"

## Posters Enhanced CSV

Download the files from EasyChair (`submission.csv` and `author.csv`).  Get the posters (track 5).

```
python3 ../convert.py 5 submission.csv author.csv ACM-BCB-2021-posters.csv
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

To check the number of submissions that are in the enhanced CSV:

```
cut -d "," -f 2 ACM-BCB-2021-posters.csv  | sort -u | wc -l
```
