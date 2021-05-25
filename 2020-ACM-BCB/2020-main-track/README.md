In this directory, the `ACM-BCB-2020-submission.csv` and `ACM-BCB-2020-author.csv` files are not committed since they contain sensitive information concerning rejected submissions. Once those are downloaded by following the instructions on the main README.md, the metadata can be generated as follows.

```
python3 ../convert.py ACM-BCB-2020-submission.csv  ACM-BCB-2020-author.csv ACM-BCB-2020-eRights-metadata.csv
```

This outputs

```
Pulling these columns from the submissions CSV file: #,title,decision
  found 40 decisions of type "accept"
  found 17 decisions of type "probably accept"
57 accepted titles processed
Pulling these columns from the authors CSV file: submission #,first name,last name,email,affiliation,person #,corresponding?
authors from 57 accepted submissions processed
Wrote to ACM-BCB-2020-eRights-metadata.csv
```

### Author modifications

These author names were manually altered:

- `Tobias Rubel Janssen --> Tobias Rubel` (member of Anna's group)

### Formatting for web pages

```
python3 ../format-for-webpage.py ACM-BCB-2020-submission.csv  ACM-BCB-2020-author.csv ACM-BCB-2020-main-papers.txt
```
