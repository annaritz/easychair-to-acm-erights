In this directory, the `submission.csv` and `author.csv` files are not committed since they contain sensitive information concerning rejected submissions. Once those are downloaded by following the instructions on the main README.md, the metadata can be generated as follows.

Change `paper_type='Poster'` and `decisions_to_track = ['accept']` in `convert.py`.

```
python3 ../convert.py submission.csv  author.csv ACM-BCB-2020-eRights-posters-metadata.csv
```

This outputs

```
Pulling these columns from the submissions CSV file: #,title,decision
  found 23 decisions of type "accept"
23 accepted titles processed
Pulling these columns from the authors CSV file: submission #,first name,last name,email,affiliation,corresponding?
authors from 23 accepted submisssions processed
Wrote to ACM-BCB-2020-eRights-posters-metadata.csv
```
### Formatting for web pages

```
python3 ../format-for-webpage.py submission.csv  author.csv ACM-BCB-2020-posters.txt
```
