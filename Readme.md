
## Twitter Sentiment Analysis

__Objective__:

This project is done as a part of coursework. It uses Twitter to understand how people are feeling about any given topic. For the purpose of this analysis the topic chosen is 'MondayMotivation'. It includes a script for the following:
1. Stream tweets of particular user/hashtag/term
2. Store entire tweets of a user in a txt file
3. Perform sentimental analysis on a tweet and identify most frequent positive and negative words for a topic

__Data Overview__:

The topic for this particular analysis is 'MondayMotivation'. Tweets pertaining to this topic have been scraped from Twitter using the script uploaded in the repository. The script for extraction has been developed by guidance from Prof. Michele Samorani.

__Analysis Approach__:

The analysis to identify if the general sentiment of the topic is positive or negative is done in two parts:
* Part 1: Overall analysis of the topic by calculating total number of positive and negative words identified using list of positive and negative words from lexicon and intrepreting the general sentiment of the topic.
* Part 2: Analysis of tweets and categorizing them as positive, negative or neutral tweets to intrepret the sentiment of the overall topic. Also includes identifying most frequently used positive and negative word.

__Intrepretation:__

__Part 1__:

The overall analysis of the tweets suggests that the general sentiment is __Strongly Positive__. This is inferred based on the my understanding of the difference between the number of positive and negative words which is huge. Approximately 85% of words in the tweets are positive based on the list of positive words from lexicon. Also, as only 904 tweets are being analysed, the difference suggests higher percentage of tweets with positive sentiment.

This is also inline with the theoretical expectation of the sentiment for the topic "MondayMotivation"

___Note:___ The analysis lacks inclusion of the emoticons (which might also indicate sentiments) and of not removing all the special characters.</i></li></ul>

<b>Part 2:</b>

The number of positive tweets (58% of total tweets) are comparatively greater than the negative tweets(10% of total tweets), which suggests the general sentiment to be positive. However, the number of neutral tweets accounts for around 30% of total tweets which couldnt be identified in part 1.

Thus, it can be inferred from both part 1 and 2 that the general sentiment is <b>Moderately Positive</b> but further analysis would be required to determine the degree of positivity.

___Note:___ The limitation of the analysis is similar to part 1.

The result also indicates that for MondayMotivation most frequently used positive word and negative word is 'Win' and 'Evil' respectively.

__Installation__

Download the data

* Clone this repo to your computer.
* Get into the folder using cd Twitter-Sentiment-Analysis-Python-master.
* Set up a twitter account and get the access token
* Replace the keys and tokens in config.cfg file
* Install tweepy 
* Run the program with the desired topic term (e.g. MondayMotivation)
    - python tweetering.py MondayMotivation
* Save the extracted tweets as a text file in the data dictionary. (The data dictionary already contains positive and negative word list downloaded. You can replace it if required)

__Usage__

* Run twitter_sentiment.py which will result in the desired outcome
