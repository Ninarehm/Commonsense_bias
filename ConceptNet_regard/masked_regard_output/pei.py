from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


category ='country'
width = 0.25  # the width of the bars
plot_format = 'sentiment'
bar_num =2
output_name ="./country_masked"
inputfile = "./nina_regard_masked_results/"

if(category=='country'):
	key_words = ['Persian', 'Armenian', 'American', 'Filipino', 'Mexican','Russian','Swedish','Irish','Chinese','German','English','British','French','Norwegian','Dutch','Scottish','Italian','Arab','African','Israeli','Japanese','Egyptian']
	key_words = sorted(key_words)
elif(category=='gender'):
	key_words =['Woman','Man','Female','Male','He','She','Father','Mother']
	key_words = sorted(key_words)
elif(category=='relig'):
	key_words = ['Muslim','Christian']
	key_words = sorted(key_words)
elif(category=='sex_orient'):
	key_words = ['Homosexual','Heterosexual']
	key_words = sorted(key_words)


line_counter = 0
all_lines = []
num_dic = defaultdict(dict)
toxic_dic = defaultdict(dict)
for i in range(len(key_words)):
  looking_concept = key_words[i].lower()
  negative_count = 0
  positive_count = 0
  neutral_count = 0
  total = 0
  in_file = open(inputfile+ looking_concept+ "_predictions.txt","r")
  toxic_dic[looking_concept] =[]
  for line in in_file.readlines():
  	number = line.split("\t")
  	total = total+1
  	print(number)
  	if(int(number[0]) ==0):
  		neutral_count = neutral_count+1
  	elif(int(number[0]) ==1):
  		positive_count = positive_count+1
  	elif(int(number[0]) ==-1):
  		negative_count = negative_count+1
  num_dic[looking_concept]['negative'] = (negative_count/total)*100
  num_dic[looking_concept]['positive'] = (positive_count/total)*100
  num_dic[looking_concept]['neutral'] = (neutral_count/total)*100
  line_counter = 0
  for j in all_lines:
  	line_counter = line_counter+1
  	if(line_counter < len(all_lines)-9):
  		toxic_dic[looking_concept].append(j.split(" ")[-1].strip("\n"))
  all_lines = []


print(num_dic)
import statistics 
if(plot_format=='toxicity'):
	overall_data = []
	for elements in key_words:
		data = []
		for el in toxic_dic[elements.lower()]:
			data.append(float(el))
		overall_data.append(data)
		print(statistics.median(data) )

	fig, ax = plt.subplots()
	plt.subplots_adjust(bottom=0.2)
	ax.set_xticklabels(key_words, fontsize=7,rotation='vertical')
	ax.legend()
  
	# Creating plot 
	bp = ax.boxplot(overall_data,showfliers=False) 
	#plt.show()
	plt.savefig(output_name)
else:
	x = np.arange(len(key_words))  # the label locations

	fig, ax = plt.subplots()
	if(plot_format=='sentiment'):
		Negative = []
		Positive = []
		Neutral =  []
		for element in key_words:
			Negative.append(float(num_dic[element.lower()]['negative']))
			Neutral.append(float(num_dic[element.lower()]['neutral']))
			Positive.append(float(num_dic[element.lower()]['positive']))
		if(bar_num==3):
			rects1 = ax.bar(x - width, Negative, width, label='Negative')
			rects2 = ax.bar(x , Positive , width, label='Positive')
			rects3 = ax.bar(x + width, Neutral, width, label='Neutral')
		else:
			rects1 = ax.bar(x - width/2, Negative, width, label='Negative')
			rects2 = ax.bar(x + width/2, Positive , width, label='Positive')
		ax.set_ylabel('regard percentage')
		if(category=="country"):
			ax.set_title('Regard percentage by country demographics')
		elif(category=="relig"):
			ax.set_title('Regard percentage by religion')
		elif(category=="gender"):
			ax.set_title('Regard percentage by gender')
		elif(category=="sex_orient"):
			ax.set_title('Regard percentage by sexual orientation')
	elif(plot_format=='hate_speech'):
		rects1 = ax.bar(x - width/2, hate, width, label='hate')
		rects2 = ax.bar(x + width/2, offensive , width, label='offensive')
		ax.set_ylabel('hate percentage')
		ax.set_title('Toxicity Scores by country demographics')
	elif(plot_format=='toxicity'):
		toxic = []
		for element in key_words:
			toxic.append(float(num_dic[element.lower()]['toxicity']))
		rects1 = ax.bar(x , toxic , width, label='toxicity')
		ax.set_ylabel('Toxicity Scores')
		ax.set_title('Toxicity Scores by country demographics')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_xticks(x)
	ax.set_xticklabels(key_words, fontsize=7,rotation='vertical')
	ax.legend()


	def autolabel(rects):
	    """Attach a text label above each bar in *rects*, displaying its height."""
	    for rect in rects:
	        height = rect.get_height()
	        ax.annotate('{}'.format(height),
	                    xy=(rect.get_x() + rect.get_width() / 2, height),
	                    xytext=(0, 3),  # 3 points vertical offset
	                    textcoords="offset points",
	                    ha='center', va='bottom')


	# autolabel(rects1)
	# autolabel(rects2)

	fig.tight_layout()

	#plt.show()
	plt.savefig(output_name)

