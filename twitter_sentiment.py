# Topic : Twitter Sentiment analysis : Sentiment Analysis of tweets related to "Monday Motivation"
# Author : Dakshata Jain 

# Project: To identify if the general sentiment of the topic is positive or negative. The analysis is done in two parts:
# Part 1: Overall analysis of the topic by calculating total number of positive and negative words and intrepreting the general sentiment of the topic.
# Part 2: Analysis of tweets and categorizing them as positive, negative or neutral tweets to intrepret the sentiment of the overall topic.

# Approach:
# Step 1: Extracted tweets for the topic "#MondayMotivation". Number of tweets = 959
# Step 2: Extracted positive('positive word list')and negative('negative word list') word lists from lexicon.com
# Step 3: Converting the positive word list text file into dictionary in order to increase the processing speed


#Importing the libraries
from itertools import islice
from prettytable import PrettyTable
import prettytable
import os
import re
import settings

#Function to print few elements from the dictionary
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

# Creating a function that creates dictionary from the text file with the word as key and increment number as value:
def createdict(file,n):
    with open(os.path.join(settings.DATA_DIR, file), 'r') as f: 
        f_text = f.read().split('\n')
        f_dict = {f_text[w]:w for w in range(0,len(f_text))}
    print('Few dictionary words :' + str(take(n,f_dict.items())))

    return f_dict

#Positive word dictionary:
p_dict = createdict('positive word list.txt',3)


# Step 4: Converting the negative word list text file into dictionary similar to p_dict
n_dict=createdict('negative word list.txt',3)


# Step 5: Part 1 : 
# Calculating number of positive and negative words in all the tweets and the difference between the two counters to assess the sentiment of the topic using the following approach:
#   a. Creating 2 increment counters to store positive and negative words in the tweets and setting them to '0'
#   b. Reading the extracted tweets text file.
#   c. Running a for loop to read each line in the file, clean the file for any special characters, convert all the words in lowercase and split each word in the file as an individual string.
#   d. Running nested for loop to read each word in the cleaned file,then check if the word exists in p_dict dictionary created and if so then increment the positive word counter by 1, else repeat the process for negative counter
#   e. Compute the percentage of positive and negative words

#Part 2: 
# Calculating percentage of positive, negative and neutral tweets to assess the sentiment of the topic using the following approach:
#    a. Creating 3 increment counters to store number of positive, negative and neutral tweets and setting them to '0'
#    b. Reading the extracted tweets text file.
#    c. Running a for loop to read each line in the file,create and set the variable,score to 0,clean the file for any special characters, convert all the words in lowercase and split each word in the file as an individual string.
#    d. Running nested for loop to read each word in the cleaned file,then check if the word exists in p_dict dictionary created and if so then add 1 to the variable score and if the word exists in n_dict, add -1 to score. Repeat the process for all the words in the line and compute the final score for each line(tweet) 
#    e. Compare the value of score to 0, and depending on whether equal to, greater than or less than 0, increment the neutral, positive or negative counter respectively
#    f. Compute and compare the percentage of positive, negative and neutral tweets to assess the sentiment

#Function to compute score for all the tweets and each tweet individually:
def score(file,p_dict,n_dict,indicator = 'both'):
    Neg_counter = 0
    Pos_counter = 0
    Neg_tweet_counter = 0
    Pos_tweet_counter = 0
    Neut_tweet_counter = 0
    posi_wordcount = {}
    neg_wordcount = {}
    
    #with open(os.path.join(settings.DATA_DIR, file), 'r') as f:
    with open(file, 'r') as f:
        for line in f:
            score=0
            a = re.sub('[^a-zA-Z0-9 \n\.]','',line)
            for word in a.split(' '):
                if word != ' ' and word != '':
                    if word in p_dict:
                        Pos_counter += 1
                        score += 1
                        if word not in posi_wordcount.keys():
                            posi_wordcount[word] = 1
                        posi_wordcount[word] += 1
                    elif word in n_dict:
                        Neg_counter += 1 
                        score += -1
                        if word not in neg_wordcount.keys():
                            neg_wordcount[word] = 1
                        neg_wordcount[word] += 1
        
            if score==0:                           #if score equals to 0, increment the neutral counter
                Neut_tweet_counter += 1
            elif score>0:                          #else if score is greater than 0, increment the positive counter
                Pos_tweet_counter += 1
            else:                                  #else, increment the negative counter
                Neg_tweet_counter += 1 
    
    pt = prettytable.PrettyTable(['Evaluated','Positive_count','Negative_count','Neutral_count'])
    total = Pos_tweet_counter + Neg_tweet_counter + Neut_tweet_counter
    total2 = Pos_counter + Neg_counter
    r1 = ['Tweet'] + [round((Pos_tweet_counter/total) * 100,2) ] + [round((Neg_tweet_counter/total)*100,2)] + \
    [round((Neut_tweet_counter/total)*100,2)]
    r2 = ['Words'] + [round((Pos_counter/total2)*100,2)] + [round((Neg_counter/total2)*100,2)] + ['N/A'] 
    
    if indicator == 'tweet':
        pt.add_row(r1)
    elif indicator == 'words':
        pt.add_row(r2)
    else:
        pt.add_row(r1)
        pt.add_row(r2)

    print(str(pt)+'\n')
    print("Mostly Frequently Used 'Positive' Word: "+str(max(posi_wordcount, key=posi_wordcount.get))+"\n")
    print("Mostly Frequently Used 'Negative' Word: "+str(max(neg_wordcount, key=neg_wordcount.get)))


#Applying the function:
score('MondayMotivation.txt',p_dict,n_dict)
