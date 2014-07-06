import sys
import tweetutil


def getAllSentiment(words, tweets):
    scores = tweetutil.initScores(words)
    tweet_text = tweetutil.initTweets(tweets)
    
    allSentiment = []
    for t in tweet_text:
        sentiment = tweetutil.getTweetSentiment(scores, t)
        allSentiment.append( sentiment)
    return  allSentiment

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    allSentiment = getAllSentiment(sent_file, tweet_file)
    tweetutil.printArray(allSentiment)

if __name__ == '__main__':
    main()