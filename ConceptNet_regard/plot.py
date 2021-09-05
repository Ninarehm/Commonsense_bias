from collections import defaultdict
import matplotlib
import argparse
import matplotlib.pyplot as plt
import numpy as np
import operator
from utils import get_country_keywords
from utils import get_relig_keywords
from utils import get_gender_keywords
from utils import get_profession_keywords


def plotting(country_negative_box_plot,gender_negative_box_plot,relig_negative_box_plot,prof_negative_box_plot,country_positive_box_plot,gender_positive_box_plot,relig_positive_box_plot,prof_positive_box_plot):
  plt.rcParams["font.family"] = "Times New Roman"
  fig, ax = plt.subplots(figsize=(10, 8))

  def set_box_color(bp, color):
      plt.setp(bp['boxes'], color=color)
      plt.setp(bp['whiskers'], color=color)
      plt.setp(bp['caps'], color=color)
      plt.setp(bp['medians'], color=color)
      plt.setp(bp['fliers'], color=color)

  neg_data = [country_negative_box_plot,gender_negative_box_plot,relig_negative_box_plot,prof_negative_box_plot]
  pos_data = [country_positive_box_plot,gender_positive_box_plot,relig_positive_box_plot,prof_positive_box_plot]


  flierprops1 = dict(markeredgecolor= '#D7191C')
  flierprops2 = dict(markeredgecolor='#2C7BB6')
  bpl = plt.boxplot(neg_data,showfliers=True ,showmeans=True, positions=np.array(range(len(neg_data)))*2.0-0.4,  widths=0.6,flierprops=flierprops1)
  bpr = plt.boxplot(pos_data,showfliers=True ,showmeans=True, positions=np.array(range(len(pos_data)))*2.0+0.4, widths=0.6,flierprops=flierprops2)
  set_box_color(bpl, '#D7191C') 
  set_box_color(bpr, '#2C7BB6')


  plt.plot([], c='#D7191C', label='Negative')
  plt.plot([], c='#2C7BB6', label='Positive')
  plt.legend(prop={'size': 20})

  ticks =["Origin","Gender","Religion","Profession"]
  plt.xticks(range(0, len(ticks) * 2, 2), ticks)
  plt.xlim(-2, len(ticks)*2)

  ax.set_ylabel('Regard (%)',fontsize=35)
  ax.set_title("ConceptNet Regard",fontsize=40)
  plt.yticks(fontsize=27)
  plt.xticks(fontsize=30)
  plt.xlim([-1,7])
  fig.tight_layout()
    

  plt.show()


def get_country_stats(inputfile,country_key_words):
  country_negative_box_plot =[]
  country_neutral_box_plot =[]
  country_positive_box_plot =[]
  for i in range(len(country_key_words)):
    looking_concept = country_key_words[i].lower()
    negative_count = 0
    positive_count = 0
    neutral_count = 0
    total = 0
    in_file = open(inputfile+ looking_concept,"r")
    for line in in_file.readlines():
      number = line.split("\t")
      total = total+1
      if(int(number[0]) ==0):
        neutral_count = neutral_count+1
      elif(int(number[0]) ==1):
        positive_count = positive_count+1
      elif(int(number[0]) ==-1):
        negative_count = negative_count+1
    if(total != 0):
      country_negative_box_plot.append((negative_count/total)*100)
      country_positive_box_plot.append((positive_count/total)*100)
      country_neutral_box_plot.append((neutral_count/total)*100)
    else:
      country_negative_box_plot.append(0.0)
      country_positive_box_plot.append(0.0)
      country_neutral_box_plot.append(0.0)

  return country_negative_box_plot, country_neutral_box_plot, country_positive_box_plot


def get_gender_stats(inputfile,gender_key_words):
  gender_negative_box_plot =[]
  gender_neutral_box_plot =[]
  gender_positive_box_plot =[]
  for i in range(len(gender_key_words)):
    looking_concept = gender_key_words[i].lower()
    negative_count = 0
    positive_count = 0
    neutral_count = 0
    total = 0
    in_file = open(inputfile+ looking_concept,"r")
    for line in in_file.readlines():
      number = line.split("\t")
      total = total+1
      if(int(number[0]) ==0):
        neutral_count = neutral_count+1
      elif(int(number[0]) ==1):
        positive_count = positive_count+1
      elif(int(number[0]) ==-1):
        negative_count = negative_count+1
    if(total != 0):
      gender_negative_box_plot.append((negative_count/total)*100)
      gender_positive_box_plot.append((positive_count/total)*100)
      gender_neutral_box_plot.append((neutral_count/total)*100)
    else:
      gender_negative_box_plot.append(0.0)
      gender_positive_box_plot.append(0.0)
      gender_neutral_box_plot.append(0.0)
  return gender_negative_box_plot, gender_neutral_box_plot, gender_positive_box_plot

def get_relig_stats(inputfile,relig_key_words):
  relig_negative_box_plot =[]
  relig_neutral_box_plot =[]
  relig_positive_box_plot =[]
  for i in range(len(relig_key_words)):
    looking_concept = relig_key_words[i].lower()
    negative_count = 0
    positive_count = 0
    neutral_count = 0
    total = 0
    in_file = open(inputfile+ looking_concept,"r")
    for line in in_file.readlines():
      number = line.split("\t")
      total = total+1
      if(int(number[0]) ==0):
        neutral_count = neutral_count+1
      elif(int(number[0]) ==1):
        positive_count = positive_count+1
      elif(int(number[0]) ==-1):
        negative_count = negative_count+1
    if(total != 0):
      relig_negative_box_plot.append((negative_count/total)*100)
      relig_positive_box_plot.append((positive_count/total)*100)
      relig_neutral_box_plot.append((neutral_count/total)*100)
    else:
      relig_negative_box_plot.append(0.0)
      relig_positive_box_plot.append(0.0)
      relig_neutral_box_plot.append(0.0)
  return relig_negative_box_plot, relig_neutral_box_plot, relig_positive_box_plot

def get_prof_stats(inputfile,prof_key_words):
  prof_negative_box_plot =[]
  prof_neutral_box_plot =[]
  prof_positive_box_plot =[]
  for i in range(len(prof_key_words)):
    looking_concept = prof_key_words[i].lower()
    negative_count = 0
    positive_count = 0
    neutral_count = 0
    total = 0
    in_file = open(inputfile+ looking_concept,"r")
    for line in in_file.readlines():
      number = line.split("\t")
      total = total+1
      if(int(number[0]) ==0):
        neutral_count = neutral_count+1
      elif(int(number[0]) ==1):
        positive_count = positive_count+1
      elif(int(number[0]) ==-1):
        negative_count = negative_count+1
    if(total != 0):
      prof_negative_box_plot.append((negative_count/total)*100)
      prof_positive_box_plot.append((positive_count/total)*100)
      prof_neutral_box_plot.append((neutral_count/total)*100)
    else:
      prof_negative_box_plot.append(0.0)
      prof_positive_box_plot.append(0.0)
      prof_neutral_box_plot.append(0.0)
  return prof_negative_box_plot, prof_neutral_box_plot, prof_positive_box_plot

def get_statistics(inputfile):
  country_key_words = get_country_keywords()
  country_key_words = [i.lower() for i in country_key_words]
  country_key_words = sorted(country_key_words)
  country_negative_box_plot, country_neutral_box_plot, country_positive_box_plot= get_country_stats(inputfile,country_key_words)


  gender_key_words = get_gender_keywords()
  gender_key_words = [i.lower() for i in gender_key_words]
  gender_negative_box_plot, gender_neutral_box_plot, gender_positive_box_plot = get_gender_stats(inputfile,gender_key_words)


  relig_key_words = get_relig_keywords()
  relig_key_words = [i.lower() for i in relig_key_words]
  relig_key_words = sorted(relig_key_words)
  relig_negative_box_plot, relig_neutral_box_plot, relig_positive_box_plot = get_relig_stats(inputfile,relig_key_words)


  prof_key_words = get_profession_keywords()
  prof_key_words = [i.lower() for i in prof_key_words]
  prof_key_words = sorted(prof_key_words)
  prof_negative_box_plot, prof_neutral_box_plot, prof_positive_box_plot = get_prof_stats(inputfile,prof_key_words)

  plotting(country_negative_box_plot,gender_negative_box_plot,relig_negative_box_plot,prof_negative_box_plot,country_positive_box_plot,gender_positive_box_plot,relig_positive_box_plot,prof_positive_box_plot)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--infile', default="./masked_regard_output/")
  args = parser.parse_args()

  inputfile = args.infile
  get_statistics(inputfile)


