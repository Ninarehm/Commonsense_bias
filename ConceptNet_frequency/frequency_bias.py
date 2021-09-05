import pandas as pd
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import argparse

def plotting(key_words,frequencies):

	plt.rcParams["font.family"] = "Times New Roman"
	
	x = np.arange(len(key_words)) 

	fig, ax = plt.subplots(figsize=(5,4))
	rects1 = ax.bar(x, frequencies, 0.5, label='#Triples')
	ax.set_ylabel('Number of Triples',fontsize=20)
	ax.set_xticks(x)
	axis_labels = [i.replace('_', ' ').lower() for i in key_words]
	ax.set_xticklabels(axis_labels, fontsize=21)
	ax.legend(prop={'size': 10})
	ax.set_title('Profession',fontsize=20)

	plt.yticks(fontsize=20) 
	plt.xlim([-0.4,1.4])

	fig.tight_layout()
	plt.show()

def get_statistics(inputfile,category):
	num_dic = defaultdict(dict)
	frequencies = []
	if category == "origin":
		key_words=['british','saudi_arabian']
	elif category == "gender":
		key_words=['woman','gentlemen']
	elif category == "profession":
		key_words=['doctor','software_developer']
	else:
		key_words=['bible','quran']
	key_words = [i.lower() for i in key_words]

	for i in key_words:
	  infile = open(inputfile+i,"r")
	  temp_counter = 0
	  for line in infile.readlines():
	    temp_counter = temp_counter+1

	  num_dic[i]=temp_counter
	  frequencies.append(temp_counter)

	plotting(key_words,frequencies)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--infile', default="./../ConceptNet_regard/masked_regard_output/")
  parser.add_argument('--category', default="origin")
  args = parser.parse_args()

  inputfile = args.infile
  get_statistics(inputfile,args.category)


