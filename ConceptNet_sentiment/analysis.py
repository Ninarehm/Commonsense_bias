import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from utils import get_keywords
from utils import relation_mapping

def write_results(outfile,looking_concept,total,neg_count,pos_count,neut_count):
  outfile.write(looking_concept + "\n")
  if(total !=0):    
    outfile.write("_____________________________________________________"+ "\n")
    outfile.write("negative_count: "+ str( (neg_count/total) *100)+ "\n")
    outfile.write("positive_count: "+ str( (pos_count/total) *100) + "\n")
    outfile.write("neutral_count: "+ str( (neut_count/total) *100)+ "\n")



    print(looking_concept)    
    print("_____________________________________________________")
    print("negative_count: "+ str( (neg_count/total) *100))
    print("positive_count: "+ str( (pos_count/total) *100))
    print("neutral_count: "+ str( (neut_count/total) *100))

  else:
    outfile.write("_____________________________________________________"+ "\n")
    outfile.write("negative_count: "+ '0'+ "\n")
    outfile.write("positive_count: "+ '0' + "\n")
    outfile.write("neutral_count: "+ '0'+ "\n")



    print(looking_concept) 
    print("_____________________________________________________")
    print("negative_count: "+ '0')
    print("positive_count: "+ '0')
    print("neutral_count: "+ '0')
      

def masking(concept,looking_concept):
  concept = concept.replace(looking_concept+" ","this person ")
  concept = concept.replace(" " +looking_concept," this person")
  concept = concept.replace(" "+looking_concept+" "," this person ")
  return concept

def sentiment_analyzer(key_words,all_concepts_long):
  sid_obj = SentimentIntensityAnalyzer() 
  for i in range(len(key_words)):
    looking_concept = key_words[i].lower()

    colnames = ["relations"]

    outfile = open("./masked_sentiment_output/" + looking_concept,"w")

    pos_count = 0.0
    neg_count = 0.0
    neut_count = 0.0
    total = 0.0

    for line_con in all_concepts_long: 
      words = line_con.lower().strip("\n").split(" ")
      if(words[1]=='externalurl'):
        continue
      if(words[1]=='dbpedia'):
        continue
      if(looking_concept in words):
        total = total+1
        concept = words[0] + " " + words[1] + " " + words[2]

        concept = masking(concept,looking_concept)
        mapped_concept = relation_mapping(words,concept)

        sentiment_dict = sid_obj.polarity_scores(mapped_concept) 
        if sentiment_dict['compound'] >= 0.05 : 
          pos_count = pos_count+1 
        elif sentiment_dict['compound'] <= - 0.05 : 
          neg_count = neg_count+1     
        else : 
          neut_count = neut_count+1

        outfile.write(mapped_concept + " " + str(sentiment_dict['compound'])+ "\n")
    write_results(outfile,looking_concept,total,neg_count,pos_count,neut_count)
    


if __name__ == "__main__":
  all_concepts_long =[]
  infile = open("./../data/ConceptNet_data","r")
  for line in infile.readlines():
    all_concepts_long.append(line)


  key_words= get_keywords()
  sentiment_analyzer(key_words,all_concepts_long)

