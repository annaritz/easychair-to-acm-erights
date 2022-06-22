## This script converts EasyChair submission and author information into ACM's required meta information for generating copyright permissions.
## @author Anna Ritz, Reed College, aritz@reed.edu
## This script modified from Di Wu, Texas A&M University, wudi930320@tamu.edu
## updated 2021 for their Enhanced CSV format
## Refer to instructions here: https://www.acm.org/publications/gi-proceedings-current

# coding:utf-8
from __future__ import division,print_function # in case someone needs Python2
import csv
import re
import sys

def main(paper_csv_file, author_csv_file, paper_type, ids, output_file):
	if paper_type not in ["Full Paper", "Poster", "Short Paper"]:
		sys.exit('Error: paper_type "%s" not acceptable.' % (paper_type))
	decisions_to_track = ['accept']

	titles = get_titles(paper_csv_file,ids,decisions_to_track)
	print('%d accepted titles processed' % len(titles))

	authors = get_authors(author_csv_file,titles.keys())
	print('authors from %d accepted submisssions processed' % len(authors))

	write_output(titles,authors,output_file,paper_type)
	print('Wrote to %s' % (output_file))

	return

'''
Processes the paper CSV file, retaining paper id and title.
Inputs: paper CSV filename, and an optional list of decisions to track.
Returns: Dictionary keyed by paper ids with titles as values.
'''
def get_titles(paper_csv_file, ids, decisions_to_track):
	titles  = {}
	decision_counter = {d:set() for d in decisions_to_track}

	paper_id_index = 0
	title_index = 1
	decision_index = 7
	with open(paper_csv_file,'r',encoding='mac_roman') as tsvfile:
		reader = csv.reader(tsvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		header = next(reader)
		print('Pulling these columns from the submissions CSV file: %s' % ','.join([header[i] for i in [paper_id_index,title_index,decision_index]]))
		for line in reader:
			paper_id = line[paper_id_index]
			if paper_id in ids: # if this is an ID to collect...
				title = line[title_index]
				decision = line[decision_index]

				# this ID should be in a decision to track...
				assert decision in decisions_to_track

				decision_counter[decision].add(paper_id)
				titles[paper_id] = title

		# make sure we've seen all IDs.
		assert len(ids) == sum([len(decision_counter[k]) for k in decision_counter.keys()])

	for d in decision_counter:
		print('  found %d decisions of type %s' % (len(decision_counter[d]),d))

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
	country_index = 4
	affil_index = 5
	corresponding_index = 8
	with open(author_csv_file,'r') as tsvfile:
		reader = csv.reader(tsvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		header = next(reader)
		print('Pulling these columns from the authors CSV file: %s' % ','.join([header[i] for i in [paper_id_index,first_name_index,last_name_index,email_index,country_index,affil_index,corresponding_index]]))
		counts = {}
		for line in reader:
			paper_id = line[paper_id_index]
			if paper_id in paper_ids: # keep this author
				first_name = line[first_name_index]#.strip("\" ")
				last_name = line[last_name_index]#.strip("\" ")
				email = line[email_index].strip()
				country = line[country_index].strip()
				affiliation = line[affil_index].strip()
				corresponding = line[corresponding_index].strip()
				if paper_id not in authors:
					authors[paper_id] = []
					counts[paper_id] = 1
				authors[paper_id].append([first_name,last_name,counts[paper_id],corresponding,email,affiliation,country])
				counts[paper_id]+=1
	return authors

'''
Writes output according to ACM-specified CSV formats.
https://www.acm.org/publications/gi-proceedings
'''
def write_output(titles,authors,output_file, paper_type):
	event_id = 12711 # hard-coded for BCB '22

	# empty columns
	prefix = ''
	middle_name = ''
	suffix = ''
	ACM_profile_id = ''
	ACM_client_no = ''
	orcid = ''
	department_school_lab = ''
	city = ''
	state_province = ''
	secondary_department_school_lab = ''
	secondary_institution = ''
	secondary_city = ''
	secondary_state_province = ''
	secondary_country = ''
	section_title = ''
	section_seq_no = ''
	published_article_number = ''
	start_page  = ''
	end_page  = ''
	article_seq_no = ''
	with open(output_file,'w+') as csvout:
		writer = csv.writer(csvout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for paper_id in sorted(titles.keys(),key=int):
			the_title = titles[paper_id]
			for first_name,last_name,author_sequence_no,contact_author,email,institution,country in authors[paper_id]:
				output = [event_id,paper_id,paper_type,the_title, \
					prefix,first_name,middle_name,last_name,suffix, \
					author_sequence_no,contact_author,ACM_profile_id,ACM_client_no,orcid, \
					email,department_school_lab,institution,city, state_province,country, \
					secondary_department_school_lab,secondary_institution, \
					secondary_city,secondary_state_province,secondary_country, \
					section_title,section_seq_no,published_article_number, \
					start_page,end_page,article_seq_no]
				writer.writerow(output)
	return

if __name__ == '__main__':
	if len(sys.argv) != 6:
		sys.exit('usage: python3 convert.py <submission.csv> <authors.csv> <paper-type> <ids> <outfile.csv>\n\tpaper-type is one of Poster, Full Paper, etc.\n\tids are comma delimited.')
	main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4].split(','),sys.argv[5])
