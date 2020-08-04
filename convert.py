## This script converts EasyChair submission and author information into ACM's required meta information for generating copyright permissions.
## @author Anna Ritz, Reed College, aritz@reed.edu
## This script modified from Di Wu, Texas A&M University, wudi930320@tamu.edu
##
## Refer to instructions here: https://www.acm.org/publications/gi-proceedings

# coding:utf-8
from __future__ import division,print_function # in case someone needs Python2
import csv
import re
import sys

def main(paper_csv_file, author_csv_file, output_file):

	## TO MODIFY DECISIONS TO TRACK use optional decitions_to_track argument, e.g.,
	titles = get_titles(paper_csv_file,decisions_to_track = ['accept'])
	#titles = get_titles(paper_csv_file)
	print('%d accepted titles processed' % len(titles))

	authors = get_authors(author_csv_file,titles.keys())
	print('authors from %d accepted submisssions processed' % len(authors))

	## TO MODIFY PAPER TYPE, use optional paper_type arguemnt, e.g.,
	#write_output(titles,authors,output_file,paper_type='Abstract')
	write_output(titles,authors,output_file)
	print('Wrote to %s' % (output_file))

	return

'''
Processes the paper CSV file, retaining paper id and title.
Inputs: paper CSV filename, and an optional list of decisions to track.
Returns: Dictionary keyed by paper ids with titles as values.
'''
def get_titles(paper_csv_file, decisions_to_track = ['accept','probably accept']):
	titles  = {}
	decision_counter = {d:0 for d in decisions_to_track}

	paper_id_index = 0
	title_index = 1
	decision_index = 7
	with open(paper_csv_file,'r',encoding='mac_roman') as tsvfile:
		reader = csv.reader(tsvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		header = next(reader)
		print('Pulling these columns from the submissions CSV file: %s' % ','.join([header[i] for i in [paper_id_index,title_index,decision_index]]))

		for line in reader:
			paper_id = line[paper_id_index]
			title = line[title_index]
			decision = line[decision_index]
			if decision in decisions_to_track: ## add this submission
				decision_counter[decision]+=1
				titles[paper_id] = title

	for d in decision_counter:
		print('  found %d decisions of type "%s"' % (decision_counter[d],d))

	return titles

'''
Processes the authors CSV file, retaining names, affiliations, emails, and corresponding author info.
Inputs: author CSV filename; list/iterator of paper ids
Returns: Dictionary of authors keyed by paper id with a list of 3-element tuples (name & affil, email, corresponding) as values.
'''
def get_authors(author_csv_file,paper_ids):
	authors = {}
	paper_id_index = 0
	first_name_index = 1
	last_name_index = 2
	email_index = 3
	affil_index = 5
	corresponding_index = 8
	with open(author_csv_file,'r') as tsvfile:
		reader = csv.reader(tsvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		header = next(reader)
		print('Pulling these columns from the authors CSV file: %s' % ','.join([header[i] for i in [paper_id_index,first_name_index,last_name_index,email_index,affil_index,corresponding_index]]))

		for line in reader:
			paper_id = line[paper_id_index]
			if paper_id in paper_ids: # keep this author
				first_name = line[first_name_index].strip("\" ")
				last_name = line[last_name_index].strip("\" ")
				email = line[email_index].strip()
				affiliation = line[affil_index].strip()
				if line[corresponding_index].strip() == 'yes':
					corresponding =  True
				else:
					corresponding = False
				if paper_id not in authors:
					authors[paper_id] = []  # tuple of (name+affil, email, corresponding)
				## authors are in the table sorted by order list.
				authors[paper_id].append(['%s %s:%s' % (first_name,last_name,affiliation),email,corresponding])
	return authors

'''
Writes output according to ACM-specified CSV formats.
https://www.acm.org/publications/gi-proceedings
'''
def write_output(titles,authors,output_file, paper_type='Full Paper'):
	with open(output_file,'w+') as csvout:
		writer = csv.writer(csvout, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		header = ["Paper Type","Title","Lead Author:Affiliation;Author2:Affiliation;Author3:Affiliation;etc.","Lead Author e-mail","Author e-mail;Author e-mail"]
		writer.writerow(header)

		## **Please note that papers of 5 pages in length or longer are considered Full Papers.
		## default args: all papers are of type 'Full Paper'

		for paper_id in sorted(titles.keys()):
			author_list = ';'.join([author[0] for author in authors[paper_id]])
			corresponding_emails = [author[1] for author in authors[paper_id] if author[2]==True]
			lead_email = corresponding_emails[0]
			others_email = ';'.join([author[1] for author in authors[paper_id] if author[1] != lead_email])
			output = [paper_type,titles[paper_id],author_list,lead_email,others_email]
			writer.writerow(output)

	return


if __name__ == '__main__':
	if len(sys.argv) != 4:
		sys.exit('usage: python3 convert.py <submission.csv> <authors.csv> <outfile.csv>')
	main(sys.argv[1],sys.argv[2],sys.argv[3])
