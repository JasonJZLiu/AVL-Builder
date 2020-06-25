import AVL
from utilities import *

def test_languages(fname):
	data = open(fname, 'r')
	print("Testing tree building")
	languages = AVL.Languages()
	data_by_year = languages.build_trees_from_file(data)
	data.close()
	
	
	
	query = 'Yiddish'
	data_by_name = languages.query_by_name(query)
	
	print("The statistics for English in Canada, by year:")
	print(data_by_name)


	threshold = 12973810-1

	data_by_count = languages.query_by_count(threshold)
		
	print("The statistics for English in Canada, by year:")
	print(data_by_count)
	
	#data_by_year[1931].printout()
	print(data_by_year[1931].is_balanced())
	
	return data_by_year


if __name__ == "__main__":
	ca_data_fname = 'data/ca_languages.csv'
	ca_data_by_year = test_languages(ca_data_fname)
	print (ca_data_by_year)
