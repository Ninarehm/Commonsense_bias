The datasets corresponding to the analysis can be found under te data directory.

Analysis to reporduce ConceptNet results for sentiment and regard can be found under ConceptNet_sentiment and ConceptNet regard directories.

Analysis to reproduce ConceptNet frequency results can be found under ConceptNet_frequency directory.

Human annotations for different models and konwledge-bases can be found under the mturk_labels directory.

To reproduce the results on ConceptNet sentiment:

cd ConceptNet_sentiment

# this will produce the files and labels from sentiment classifier for each of the target groups. You can ultimately use files in the masked_sentiment_output which are the results from running this script.
python3 analysis.py --infile location_to_ConceptNet_data

#this will produce the plots for the sentiment analysis on ConceptNet. You can ultimately use files in the masked_sentiment_output to plot the results without running the previous step.
python3 plot.py --infile location_to_analysis_output

To reproduce the results on ConceptNet regard:

cd ConceptNet_regard

#to reproduce the labels from the regard classifier you can use regard classifier from (sheng et al. 2019) However the masked_regard_output contains these labels in a format easily usable for plotting and further analysis.

#to plot the results for ConceptNet results using regard classifier.
python3 plot.py

To reproduce the frequency analysis results on ConceptNet:
cd ConceptNet_frequency
python3 frequency_bias.py --infile ./../ConceptNet_regard/masked_regard_output/ --category origin
#in which category can be replaced by either of the 4 studied categories in the paper.
