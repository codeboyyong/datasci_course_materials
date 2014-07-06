import sys
 
import tweetutil

def getTermFreqMap(tweet_texts):
    term_freq = {}
        
    for tweet in tweet_texts:
        tweet_words = tweet.split()

        for word in tweet_words:
            if word in term_freq.keys():
                term_freq[word] = term_freq[word] + 1
            else:
                term_freq[word] = 1
    
    return term_freq


def printTermFreqsHistgram(term_freq, total):
    for key in term_freq.keys():
        freq = term_freq[key] / float(total)
        print key + ' ' + str(round(freq, 6))

def main():

    tweet_file = open(sys.argv[1])
    tweet_texts =  tweetutil.initTweets(tweet_file)          

    term_freq = getTermFreqMap(tweet_texts)
    total = sum(term_freq.values())
    
    printTermFreqsHistgram(term_freq, total) 


if __name__ == '__main__':
    main()