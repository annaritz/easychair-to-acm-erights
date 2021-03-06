# easychair-to-acm-erights

Scripts and instructions for converting ACM-BCB EasyChair submissions into ACM eRights metadata.  Chairs and organizers must convert their metadata information into an XML or CSV file for uploading to ACM.  

## 2020 ACM-BCB Instructions

Anna will handle main conference papers, poster abstracts, and highlight abstracts.  For **Workshop Organizers**, follow these instructions.

1. **Generate a CSV file** of author metadata.  From ACM's [General Instructions for Proceedings](https://www.acm.org/publications/gi-proceedings), this CSV includes paper type, affiliations, and emails.  Only one author gets this copyright notification - we have decided that the **first corresponding author** receives this info. See below for instructions about generating the CSV file.

2. **Send the CSV file to Conference Catalysts** (Kerstin Bonicard, kbonicard@conferencecatalysts.com). Kerstin and Conference Catalysts will upload the file, review the grid, and send automated notifications for authors.  They will also monitor copyright submission status on a weekly basis.

3. Workshop organizers need to either give Conference Catalysts EasyChair permissions for them to monitor the camera-ready submissions, or need to monitor the camera-ready submissions themselves.  

## Instructions for Generating the CSV file

### Option 1: Manually build a CSV file

If you do not have many submissions, it might be easiest to manually build this CSV file. The following is a screenshot of the relevant information from ACM's [General Instructions for Proceedings](https://www.acm.org/publications/gi-proceedings):

![CSV instruction screen shot](../csv-formatting.png)

### Option 2: Run the `convert.py` script

For this option, you download two CSV files from EasyChair and then run `convert.py`.  Download a submission table and the authors table using the Premium tab on EasyChair; deselect "include empty tables" and select "include table headers":

![Downloading screen shot](../downloading.png)

Next, you may need to manually change two lines in `convert.py`:

- `decisions_to_track`: default values are to include `accept` and `probably accept` decisions. Modify the `main()` function to include different decisions, e.g.

```
titles = get_titles(paper_csv_file,decisions_to_track = ['accept'])
```

- `paper type`: default value is to set all submissions as `Full Paper`. Modify the `main()` function to include a different type according to the ACM-accepted values, e.g.,

```
write_output(titles,authors,output_file,paper_type='Poster')
```
The following is a screenshot of the possible paper types from ACM's [General Instructions for Proceedings](https://www.acm.org/publications/gi-proceedings); note that papers of 5 pages in length or longer are considered Full Papers.

![paper types](../paper-types.png)
