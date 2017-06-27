# bibtex2csv
Python script that converts BibTeX entries to CSV.

Howto convert & add fields to extract: Convert single BibTex file (.bib) with the command ./bibtex2csv.py < [.bib file] > [output file]

Convert multiple BibTex files (.bib) with the command cat *.bib | ./bibtex2csv > [output file]

Add extra fields to extract by adding fields to the below code in main program. for entry in entries: doi = entry["DOI"] title = entry["Title"] oa = entry["OA"] -> new_variable = entry["name_from_bibtex_file"]

add \t{} to line for as many new fields as you add
-> print("{}\t{}\t{}".format(doi, title, oa))
