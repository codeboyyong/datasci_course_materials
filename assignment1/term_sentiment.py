import sys
 
import tweetutil


def fillNewTermSentiment(scores, new_terms, tweet, score):
    tweet_word = tweet.split()
    for word in tweet_word:
        if word not in scores.keys(): #Look up each token which is not present in the scores dict
            new_score = score #Define a variable that would contain the tweet score
            if word in new_terms.keys(): #Check whether the term is present in the new_terms dict
                new_terms[word] = new_terms[word] + new_score
            else:
                new_terms[word] = new_score

def getNewTermSentiment(sent_file, tweet_file):
    scores = tweetutil.initScores(sent_file)               
    tweet_text =  tweetutil.initTweets(tweet_file)          

    new_terms = {}                               
    for tweet in tweet_text:                           
        score = tweetutil.getTweetSentiment(scores, tweet)      #If the term matches, assign the term score and calculate the total score of each tweet    
        fillNewTermSentiment(scores, new_terms, tweet, score)                   

    return new_terms
 

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    new_terms=getNewTermSentiment(sent_file, tweet_file)
    tweetutil.printTermScore(new_terms)
if __name__ == '__main__':
    main()